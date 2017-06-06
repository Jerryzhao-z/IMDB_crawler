import requests
import re
from lxml import html

def url_film_ttid(ttid):
    return "http://www.imdb.com/title/"+ttid

def url_people_nmid(nmid):
    return "http://www.imdb.com/name/"+nmid

def url_google_cache_nmid(nmid):
    return "http://webcache.googleusercontent.com/search?q=cache:http://www.imdb.com/name/"+nmid

def url_films_release_year(year, page=1):
    return "http://www.imdb.com/search/title?release_date="+str(year)+"&page="+str(page)

def url_films_rating(lower_bound, higher_bound, page=1, min_vote = 1000):
    return "http://www.imdb.com/search/title?num_votes="+str(min_vote)+",&user_rating="+str(lower_bound)+","+str(higher_bound)+"&page="+str(page)

def url_search(year, lower_bound, higher_bound, max_vote, min_vote = 1000, page=1):
    return "http://www.imdb.com/search/title?release_date="+str(year)+"&num_votes="+str(min_vote)+","+str(max_vote)+"&user_rating="+str(lower_bound)+","+str(higher_bound)+"&page="+str(page)

class person_page(object):
    def __init__(self, nmid):
        self.nmid = nmid
        self.url = url_people_nmid(nmid)
        response = requests.get(self.url)
        raw_page = response.content.decode("utf8")
        self.page = html.fromstring(raw_page)
    
    def get_all_related_films(self):
        urls = self.page.xpath("//div[@class='article']/div[@id='filmography']/div[@class='filmo-category-section']/div/b/a/@href")
        ttids = [url.split("/")[2] for url in urls]
        return ttids

    def get_important_films(self):
        urls = self.page.xpath("//div/div[@class='knownfor-title-role']/a[@class='knownfor-ellipsis']/@href")
        ttids = [url.split("/")[2] for url in urls]
        return ttids

class search_page(object):
    def __init__(self, **kwargs):
        self.release_year = kwargs.get('release_year', "")
        self.page_number = kwargs.get('page', 1)
        self.rate_lower_bound = kwargs.get("rate_lower_bound", 0)
        self.rate_higer_bound = kwargs.get("rate_higer_bound", 10)
        self.min_vote = kwargs.get("rate_lower_bound", "")
        self.max_vote = kwargs.get("rate_lower_bound", "")

        self.url = url_search(self.release_year, self.rate_lower_bound, self.rate_higer_bound, self.max_vote, self.min_vote, self.page_number)
        response = requests.get(self.url)
        raw_page = response.content.decode("utf8")
        self.page = html.fromstring(raw_page)
    
    def get_film_ttids(self):
        urls = self.page.xpath("//div[@class='lister-item mode-advanced']/div[@class='lister-item-content']/h3[@class='lister-item-header']/a/@href")
        ttid = list()
        for url in urls:
            ttid.append(url.split("/")[2]) 
        return ttid

    def get_actors_ttids(self):
        urls = self.page.xpath("//div[@class='lister-item mode-advanced']/div[@class='lister-item-content']/p/a/@href")
        nmid = list()
        for url in urls:
            url_splited = url.split("/")
            if url_splited[1] == "name":
                nmid.append(url.split("/")[2])
        return nmid

    def number_of_films(self):
        number = self.page.xpath("//div[@class='nav'][1]/div[@class='desc']/text()")
        try:
            found = re.search(r"of (.+) titles", number[2]).group(1)
        except AttributeError:
            return 0
        return int(found.replace(',',''))

    