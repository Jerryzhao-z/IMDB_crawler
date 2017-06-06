# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ImdbItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    ttid = Field()
    release_year = Field()
    rating = Field()
    vote = Field()
    primary_language = Field()
    country = Field()
    genre = Field()
    film_format = Field()
    keywords = Field()
    

    writers = Field()
    director = Field()
    actors = Field()
    music = Field()
    cinematography = Field()
    editor = Field()
    producer = Field()
    cast_director = Field()
    costume_design = Field()
    set_design = Field()
    content_rating = Field()
    production_company = Field()
    filming_location = Field()

class peopleItem(Item):
    name = Field()
