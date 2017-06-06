# IMDB crawler

IMDB crawler are constituent of two parts: urls crawler and films crawler

The data crawled from IMDB is available in folder ./results

------
## urls crawler (python 3.5)
scripts:


url_generation.py - generate urls of IMDB for a list of ttid in json


result: 

top 500 popular film of each years from 1930 - 2016, related important persons listed in query pages
films rated from 6 to 10 and at least 1000 voted, related important person listed in query pages: 56385(film) 56670(people) 

All related films of people who involved in 9-10 rated, at least 1000 vote film(1606 films):  13368(film) 2391(people)

All related films of people who involved in 8-9 rated, at least 1000 vote film(7820 films):  207533(film) 11206(people)

All related films of people who involved in 7-8 rated, at least 1000 vote film(12383 films):  147301(film) 19850(people)

Summary: 424587 ttid, 57021 nmid in total
This dataset could cover most of important films and important person in film industry
------
## films crawler (python 2.7 + Scrapy) 

Requirement: Python 2.7 + Scrapy

