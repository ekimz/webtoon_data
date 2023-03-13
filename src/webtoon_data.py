from configparser import ConfigParser
import pandas as pd
import requests
import json

# access
config = ConfigParser()
config.read('config.ini')
api_host = config.get('api', 'host')
api_key = config.get('api', 'key')


# Get a list of genres available on WEBTOON
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


# Get string title of WEBTOON from number ID
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


# Get a list of given genre of top ranked WEBTOONS up to placement stated in count
# i.e. get_webtoon_list_ranking('ALL', 23) should result in 23 top WEBTOONs across all genres
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
    # print(ranked_list)
    rank_list = ranked_list[0]
    # print(rank_list)

    ranked_title_list = []  # initiate empty list for ranked list
    for rank in rank_list:
        ranked_title_list.append(get_webtoon_title(rank))  # replace number titles with string titles, readability
    return print(ranked_title_list)


# get_webtoon_list_ranking('ROMANCE', 3)


# Provide 3 WEBTOON recommendations based on title provided
# AND ALSO PROVIDE A SUMMARY OF EACH ONE (DESCRIPTION)
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
    response_rec_json = response_rec.json()  # turn it into json
    response_rec_df = pd.DataFrame(response_rec_json['message']['result']['recommend'])  # [0]['webtoon']

    # print(response_rec_df.head())

    if response_rec_df.empty:
        print('I can\'t find that one, pls check your ID again or add a different WEBTOON - I can take another look :O')
    else:
        rec_df = pd.DataFrame(response_rec_json['message']['result']['recommend'][0]['webtoon'])
        all_recs_df = rec_df[['title', 'titleNo', 'representGenre', 'writingAuthorName', 'pictureAuthorName',
                              'language', 'starScoreAverage', 'readCount', 'favoriteCount', 'synopsis']]
        print('Here are three WEBTOONs that we recommend if you enjoy ' + get_webtoon_title(title_number) + ':')
        print(all_recs_df)

# get_recommendations(1436)
