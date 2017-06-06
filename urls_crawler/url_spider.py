import sys
import time
import threading

from utils import person_page, search_page




###############################
def get_top_rate_film_of_years(start, end, thread_number):
    thread_pool = list()
    films = dict()
    related_people = dict()
    errors = dict()

    interval = int((end-start)/thread_number)

    for year in range(start, end, interval):
        if year > end-interval:
            t = threading.Thread(target=crawl_years, args=(films, related_people, errors, year, end))
        else:
            t = threading.Thread(target=crawl_years, args=(films, related_people, errors, year, year+interval))
        thread_pool.append(t)

    for thread_item in thread_pool:
        thread_item.start()
    for thread_item in thread_pool:
        thread_item.join()
    
    films_list = list()
    for f_item in films.keys():
        films_list += films[f_item]
    # remove duplicated films
    films_list = list(set(films_list))

    people_list = list()
    for p_item in related_people.keys():
        people_list += related_people[f_item]
    people_list = list(set(people_list))

    return films_list, people_list, errors

def crawl_years(films, people, error, start, end):
    for i in range(start, end):
        print ("searching for films of the year %d" % i)
        films[i], people[i], error[i] = crawl_certain_year(i)
        print ("new films %d of year %d" % len(films[i]), i)
        # simple crawling rate control 
        time.sleep(5)

# max_page = 11 if get top 500 films for each year
def crawl_certain_year(year, max_page=11):
    film_list = list()
    people_list = list()       
    error_list = list()
    
    for page in range(1,max_page):
        try:
            year_html = search_page(release_year=year, page=page)
            film_list += year_html.get_film_ttids()
            people_list += year_html.get_actors_ttids()
        except:
            time.sleep(5)
            print ("the page number ", page, " of the year ", year, " encounter a error, skipping this page")
            error_list.append(page)

    return film_list, people_list, error_list

######################################

def get_films_related_to_people():
    return 