# webtoon_data

As an avid WEBTOON reader, I was inspired to create a Python wrapper that would display information regarding the top / hottest / most relevant WEBTOONs available today. There are two sections on the WEBTOON website or app, Canvas and Originals, which refer to content that is published independently and content that is licensed by WEBTOON respectively.

The API I found (on RapidAPI; link below) provides access to all listings available on the WEBTOON platform, in both Canvas and Original. This python wrapper can create ranked lists of any length by genre, provide recommendations with synopses of recommended titles, and get basic information such as names of the author and illustrator and a list of available genres.

API referenced: https://rapidapi.com/apidojo/api/webtoon

## Installation

```bash
$ pip install webtoon_data
```

## Usage

Get the title number of a WEBTOON.

```
>>> get_webtoon_num('True Beauty')
>>> The title number for (that WEBTOON) is 1436, hope that helps! :)
```

Get the title name with the title number of a WEBTOON.

```
>>> get_webtoon_title(3210)
>>> The Spark in Your Eyes
```


Provide a list of genres available on the WEBTOON platform.
```
>>> get_webtoon_genre_list
>>> ['Drama', 'Fantasy', 'Comedy', 'Action', 'Slice of life', 'Romance', 'Superhero', 'Sci-fi', 'Thriller', 'Supernatural', 'Mystery', 'Sports', 'Historical', 'Heart-warming', 'Horror', 'Informative']
```

What are the top ranking WEBTOONs in specified genre of n length?

```
>>> get_webtoon_list_ranking('ROMANCE', 25)
>>> ['Lore Olympus', 'Down To Earth', 'Marry My Husband', 'Operation: True Love', 'Maybe Meant to Be', 
'The Doctors are Out', 'Go Away Romeo', 'True Beauty', 'The Kiss Bet', 'Hello Baby', 'SubZero', 'Villain with a Crush', 
'Night Owls & Summer Skies', 'Act Like You Love Me!', 'The Blind Prince', 'Leveling Up My Husband to the Max', 
'My Gently Raised Beast', 'For My Derelict Favorite', 'Blood Reverie', 'Be My Villain', 'My Reason to Die', 
'The RUNWAY', 'Perfect Marriage Revenge', 'Bitten Contract', 'Sixth Sense Kiss']
```

Can you give me a recommendation of a WEBTOON to read from a title I provide?

```
>>> get_recommendations(1436)
>>> Here are three WEBTOONs that we recommend if you enjoy True Beauty:
     title  ...                                           synopsis
0  SAVE ME  ...  Seven boys. Best friends. Their fates intertwi...
1    Edith  ...  Edith is not your typical heroine. She struggl...
2  KILLMAX  ...  Born into a bloodline of witches, Max is force...
```


## License

`webtoon_data` was created by Kim Eunji. It is licensed under the terms of the MIT license.

## Credits

`webtoon_data` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
