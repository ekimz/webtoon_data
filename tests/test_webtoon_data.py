from webtoon_data import webtoon_data
import pytest
import pandas as pd
import requests
import re
import json

def test_get_webtoon_genre_list():
    assert get_webtoon_genre_list() == ['Drama', 'Fantasy', 'Comedy', 'Action', 'Slice of life', 'Romance', 'Superhero', 'Sci-fi', 'Thriller', 'Supernatural', 'Mystery', 'Sports', 'Historical', 'Heart-warming', 'Horror', 'Informative']

