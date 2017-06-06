import json
import argparse

from url_spider import get_top_rate_film_of_years
## top 500 popular films from 1930 to 2017

parser = argparse.ArgumentParser(description='get top 500 films of years')
parser.add_argument("--thread", default=5, dest='thread', type=int, help="number of threads")
parser.add_argument("--start", default=1930, dest='start', type=int, help="start year of crawler")
parser.add_argument("--end", default=2017, dest='end', type=int, help="end year of crawler")
parser.add_argument("--output_films_file", default="", dest="film_loc", type=str, help="location of output ttid json film")
parser.add_argument("--output_people_file", default="", dest="people_loc", type=str, help="location of output nmid json film")
parser.add_argument("--output_error_file", default="", dest="error_loc", type=str, help="location of output errors json film")
parser.add_argument("--output_encoding", default="utf8", dest='encoding_out', type=str, help="encoder of output file")

args = parser.parse_args()
start = args.start
end = args.end
thread_num = args.thread


output_film = args.film_loc if len(args.film_loc)>0 else './data/films_'+str(start)+'_to_'+str(end)+'.json'
output_people = args.people_loc if len(args.people_loc)>0 else './data/people_'+str(start)+'_to_'+str(end)+'.json'
output_error = args.error_loc if len(args.error_loc)>0 else './data/error_'+str(start)+'_to_'+str(end)+'.json'



films_list, people_list, errors = get_top_rate_film_of_years(start, end, thread_num)

json.dump(films_list, open(output_film, 'w', encoding="utf8"))
json.dump(people_list, open(output_people, 'w', encoding="utf8"))
json.dump(errors, open(output_error, 'w', encoding="utf8"))

# important people of 9-10 rate, at least 1000 vote films 

#get_films_related_to_people()