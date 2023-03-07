import requests
import re
import pandas as pd
import json
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
api_host = config.get('api', 'host')
api_key = config.get('api', 'key')

def get_webtoon_genre_list():
    url = "https://webtoon.p.rapidapi.com/originals/genres/list"
    querystring = {
        "language": "en"
    }
    headers = {
        'x-rapidapi-host': api_host,
        'x-rapidapi-key': api_key
    }

    response_gen = requests.request("GET", url, headers=headers, params=querystring)
    webtoon_gen_json = response_gen.json()
    webtoon_json_gen_df = pd.DataFrame(webtoon_gen_json['message']['result']['genreList']['genres'])
    print(webtoon_json_gen_df['name'].tolist())


def get_webtoon_title(num):
    url_title = "https://webtoon.p.rapidapi.com/originals/titles/get-info"
    headers_title = {
        'x-rapidapi-host': api_host,
        'x-rapidapi-key': api_key
    }
    querystring_title = {
        "titleNo": num,
        "language": "en"
    }
    # for titles
    response_titles = requests.request("GET", url_title, headers=headers_title, params=querystring_title)
    response_titles_json = response_titles.json()
    title_json = response_titles_json['message']['result']['titleInfo']['title']
    return title_json


def get_webtoon_list_ranking(genre, count):
    url = "https://webtoon.p.rapidapi.com/originals/titles/list-by-rank"
    headers = {
        'x-rapidapi-host': api_host,
        'x-rapidapi-key': api_key
    }
    querystring = {
        "count": count,
        "language": "en"
    }
    # for rankings
    response_rank = requests.request("GET", url, headers=headers, params=querystring)
    webtoon_rank_json = response_rank.json()
    webtoon_json_rank_df = pd.DataFrame(webtoon_rank_json['message']['result']['titleNoListByTabCode'])
    # print(webtoon_json_rank_df.head())
    # print(webtoon_json_rank_df['tabCode'])
    ranked_list = webtoon_json_rank_df.loc[webtoon_json_rank_df['tabCode'] == genre]['titleNoList'].tolist()
    rank_list = ranked_list[0]
    print(rank_list)

    ranked_title_list = []
    for rank in rank_list:
        ranked_title_list.append(get_webtoon_title(rank))
    return print(ranked_title_list)


def get_recommendations(title_number):
    url_rec = "https://webtoon.p.rapidapi.com/originals/titles/get-recommend"
    querystring_rec = {
        "titleNo": title_number,
        "language": "en"
    }
    headers_rec = {
        'x-rapidapi-host': api_host,
        'x-rapidapi-key': api_key
    }
    response_rec = requests.request("GET", url_rec, headers=headers_rec, params=querystring_rec)
    print(response_rec.text)

