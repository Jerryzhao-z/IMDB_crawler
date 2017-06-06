import json
import argparse

parser = argparse.ArgumentParser(description='transform list of ttid in json format to list of urls for film crawler')
parser.add_argument("--input_file", metavar="FILE", required=True, dest='f_in', type=str, help="input json which contains list of ttid")
parser.add_argument("--output_file", default="./film_urls.txt", dest='f_out', type=str, help="output text file which contains list of urls of IMDB")
parser.add_argument("--input_encoding", default="utf8", dest='encoding_in', type=str, help="encoder of input file")
parser.add_argument("--output_encoding", default="utf8", dest='encoding_out', type=str, help="encoder of output file")

args = parser.parse_args()

with open(args.f_in, encoding=args.encoding_in) as f_in:
    orignal_films = json.load(f_in)

with open(args.f_out, "w", encoding=args.encoding_out) as f_out:
    for film in orignal_films:
        print ("http://www.imdb.com/title/"+film+"/", file=f_out)
