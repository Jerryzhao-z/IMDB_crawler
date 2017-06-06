import scrapy
from imdb.items import ImdbItem, peopleItem
import re

def remove_return_chariot(text):
    if text[-1] == "\n":
        return text[:-1]
    else:
        return text

def get_fullcast_url(url):
    return url+"fullcredits"

def get_company_url(url):
    return url+"companycredits"

def get_location_url(url):
    return url+"locations"

def get_technical_url(url):
    return url+"technical"

def get_parent_guide_url(url):
    return url+"parentalguide"

def get_keyword_url(url):
    return url+"keywords"

class ImdbSpider(scrapy.Spider):
    name = "imdb"
    #allowed_domains = ["imdb.com"]

    def __init__(self, filename=None):
        if filename:
            with open(filename, 'r') as f:
                self.start_urls = f.read().splitlines()

    def parse(self, response):
        
        fullcast_url = get_fullcast_url(response.url)
        company_url = get_company_url(response.url)
        location_url = get_location_url(response.url)
        technical_url = get_technical_url(response.url)
        parentguide_url = get_parent_guide_url(response.url)
        keyword_url = get_keyword_url(response.url)

        urls = {
            "fullcast":fullcast_url,
            "company": company_url,
            "location": location_url,
            "technical": technical_url,
            "parentguide": parentguide_url,
            "keyword": keyword_url
        }

        film = ImdbItem()
        # main
        film["ttid"] = response.url.split('/')[4]
        film["name"] = response.xpath("//div[@class='title_block']/div[@class='title_bar_wrapper']/div[@class='titleBar']/div[@class='title_wrapper']/h1/text()").extract()[0].strip()
        release_year = response.xpath("//div[@class='title_bar_wrapper']/div[@class='titleBar']/div[@class='title_wrapper']/h1/span[@id='titleYear']/a/text()")
        if release_year and len(release_year.extract()) > 0:
            film["release_year"] = release_year.extract()[0].strip()
        rating = response.xpath("//div[@class='imdbRating']/div[@class='ratingValue']/strong/span/text()")
        if rating and len(rating.extract())>0:
            film["rating"] = response.xpath("//div[@class='imdbRating']/div[@class='ratingValue']/strong/span/text()").extract()[0].strip()
            film["vote"] = response.xpath("//div[@class='ratings_wrapper']/div[@class='imdbRating']/a/span[@itemprop='ratingCount']/text()").extract()[0].strip()
        
        detail_items = response.xpath("//div[@id='main_bottom']/div[@id='titleDetails']/div[@class='txt-block']/h4/text()").extract()
        if "Language:" in detail_items:
            lang_index = detail_items.index("Language:")+1
            languages = response.xpath("//div[@id='main_bottom']/div[@id='titleDetails']/div[@class='txt-block']["+str(lang_index)+"]/a/text()").extract()
            if len(languages) > 0:
                film["primary_language"] = languages[0].strip()
        if "Country:" in detail_items:
            country_index = detail_items.index("Country:")+1
            countries = response.xpath("//div[@id='main_bottom']/div[@id='titleDetails']/div[@class='txt-block']["+str(country_index)+"]/a/text()").extract()
            film["country"] = [country.strip() for country in countries]
        
        storyline_items = response.xpath("//div[@id='main_bottom']/div[@id='titleStoryLine']/div/h4/text()").extract()
        if "Genres:" in storyline_items:
            genre_index = storyline_items.index("Genres:")+2
            genres = response.xpath("//div[@id='main_bottom']/div[@id='titleStoryLine']/div["+str(genre_index)+"]/a/text()").extract()
            film["genre"] = [genre.strip() for genre in genres]
        
        yield scrapy.Request(urls["technical"], callback=self.tech_specification, meta = {'item': film, "urls": urls})

    
    def fullcast_callback(self, response):
        urls = response.meta['urls']
        film = response.meta['item']

        labels = response.xpath("//div[@id='fullcredits_content']/h4[@class='dataHeaderWithBorder']/text()").extract()
        labels = [label.strip() for label in labels if len(label.strip())>0]

        index_gap = 0
        if "Cast" in labels:
            index_gap = -1
            index_of_cast = labels.index("Cast")
        
        if index_gap == 0:
            for label in labels:
                index = labels.index(label)
                film = self.mapDetail(response, label, film, index+1)
        else:
            for label in labels:
                index = labels.index(label)
                if  index < index_of_cast:
                    film = self.mapDetail(response, label, film, index+1)
                elif index > index_of_cast:
                    film = self.mapDetail(response, label, film, index+1+index_gap)
                else:
                    actors = response.xpath("//table[@class='cast_list']//td[@class='itemprop']/a/span[@class='itemprop']/text()").extract()
                    film["actors"] = [actor.strip() for actor in actors]

        #return film
        yield scrapy.Request(urls["company"], callback=self.company_callback, meta = {'item': film, "urls": urls})
        
    def mapDetail(self, response, label, film, index):
        if label == "Directed by":
            film["director"]=[person.strip() for person in response.xpath("//table[@class='simpleTable simpleCreditsTable']["+str(index)+"]//tr/td[@class='name']/a/text()").extract()] 
        elif label == "Writing Credits":
            film["writers"]= [person.strip() for person in response.xpath("//table[@class='simpleTable simpleCreditsTable']["+str(index)+"]//tr/td[@class='name']/a/text()").extract()]
        elif label == "Produced by":
            film["producer"]= [person.strip() for person in response.xpath("//table[@class='simpleTable simpleCreditsTable']["+str(index)+"]//tr/td[@class='name']/a/text()").extract()]
        elif label == "Music by":
            film["music"]= [person.strip() for person in response.xpath("//table[@class='simpleTable simpleCreditsTable']["+str(index)+"]//tr/td[@class='name']/a/text()").extract()]
        elif label == "Cinematography by":
            film["cinematography"]= [person.strip() for person in response.xpath("//table[@class='simpleTable simpleCreditsTable']["+str(index)+"]//tr/td[@class='name']/a/text()").extract()]
        elif label == "Film Editing by":
            film["editor"]= [person.strip() for person in response.xpath("//table[@class='simpleTable simpleCreditsTable']["+str(index)+"]//tr/td[@class='name']/a/text()").extract()]
        elif label == "Casting By":
            film["cast_director"]= [person.strip() for person in response.xpath("//table[@class='simpleTable simpleCreditsTable']["+str(index)+"]//tr/td[@class='name']/a/text()").extract()]
        elif label == "Set Decoration by":
            film["set_design"]= [person.strip() for person in response.xpath("//table[@class='simpleTable simpleCreditsTable']["+str(index)+"]//tr/td[@class='name']/a/text()").extract()]
        elif label == "Costume Design by":
            film["costume_design"]= [person.strip() for person in response.xpath("//table[@class='simpleTable simpleCreditsTable']["+str(index)+"]//tr/td[@class='name']/a/text()").extract()]
        elif label == "Art Direction by":
            film["art_director"]= [person.strip() for person in response.xpath("//table[@class='simpleTable simpleCreditsTable']["+str(index)+"]//tr/td[@class='name']/a/text()").extract()]
        elif label == "Production Design by":
            film["cast_director"]= [person.strip() for person in response.xpath("//table[@class='simpleTable simpleCreditsTable']["+str(index)+"]//tr/td[@class='name']/a/text()").extract()]

        return film

    def company_callback(self, response):
        urls = response.meta['urls']
        film = response.meta['item']
        #company
        product_company = response.xpath("//div[@id='company_credits_content']/h4[@id='production']/text()")
        if product_company and len(product_company.extract())>0 and product_company.extract()[0].strip() == "Production Companies":
            companies = response.xpath("//div[@id='company_credits_content']/ul[@class='simpleList'][1]/li/a/text()").extract()
            film["production_company"] = [company.strip() for company in companies]
        #return film
        yield scrapy.Request(urls["location"], callback=self.filming_location, meta = {'item': film, "urls": urls})

    def filming_location(self, response):
        urls = response.meta['urls']
        film = response.meta['item']
        #location
        filming_loc = response.xpath("//div[@class='article listo']/div[@id='filming_locations_content']//dt/a/text()").extract()
        film["filming_location"] = [location.strip() for location in filming_loc]
        #return film
        yield scrapy.Request(urls["parentguide"], callback=self.parent_guide, meta = {'item': film, "urls": urls})

    def tech_specification(self, response):
        urls = response.meta['urls']
        film = response.meta['item']
        #technical
        film_format = response.xpath("//div[@id='technical_content']/table[@class='dataTable labelValueTable']/tbody/tr[@class='even'][5]/td[@class='label']/text()")
        if film_format and len(film_format.extract()) >0 and film_format.extract()[0].strip() == "Printed Film Format":
            film["film_format"] = [format.strip() for format in response.xpath("//div[@id='technical_content']/table[@class='dataTable labelValueTable']/tbody/tr[@class='even'][5]/td[2]/text()").extract()]
            for f_index in range(len(film["film_format"])):
                index = film["film_format"][f_index].find('\n')
                if index > 0:
                    film["film_format"][f_index] = film["film_format"][f_index][:index].strip()
        yield scrapy.Request(urls["fullcast"], callback=self.fullcast_callback, meta = {'item': film, "urls": urls})
        #return film

    def parent_guide(self, response):
        urls = response.meta['urls']
        film = response.meta['item']
        #parentguide
        certifications = response.xpath("//div[@id='tn15']/div[@id='tn15main']/div[@id='tn15content']/div[@class='info'][2]/h5/text()")
        if certifications and len(certifications.extract()) >0 and certifications.extract()[0].strip()== "Certification:":
            content_rating = response.xpath("//div[@id='tn15content']/div[@class='info'][2]/div[@class='info-content']/a/text()").extract()
            film["content_rating"] = [rating.strip() for rating in content_rating]
        #return film
        yield scrapy.Request(urls["keyword"], callback=self.keyword, meta = {'item': film, "urls": urls})

    def keyword(self, response):
        urls = response.meta['urls']
        film = response.meta['item']
        keywords = response.xpath("//div[@id='keywords_content']/table[@class='dataTable evenWidthTable2Col']/tbody/tr/td/div[@class='sodatext']/a/text()")
        if keywords and len(keywords.extract()) >0:
            film["keywords"] = keywords.extract()
            film["keywords"] = [key.strip() for key in film["keywords"]]
        return film

