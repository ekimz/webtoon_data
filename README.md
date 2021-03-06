# webtoon_data

A preliminary attempt at a Python API wrapper for Webtoon data. For obtaining lists of Webtoon titles and rankings.

## Installation

```bash
$ pip install webtoon_data
```

## Usage

Provide genre list available in WEBTOON.

```
>>> get_webtoon_genre_list
>>> ['Drama', 'Fantasy', 'Comedy', 'Action', 'Slice of life', 'Romance', 'Superhero', 'Sci-fi', 'Thriller', 'Supernatural', 'Mystery', 'Sports', 'Historical', 'Heart-warming', 'Horror', 'Informative']
```

What are the top ranking WEBTOON in specified genre?

```
>>> get_webtoon_list_ranking('ROMANCE')
>>> [1320, 1218, 1798, 1436, 1468, 2606, 2832, 218...
```

## License

`webtoon_data` was created by Kim Eunji. It is licensed under the terms of the MIT license.

## Credits

`webtoon_data` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
