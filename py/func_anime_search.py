import requests as rq
import json

def anime_search():
    searchparams = {'q': input("Search for anime: "), 'limit': 20, 'order_by': 'popularity', 'sort': 'asc'}
    re = rq.get('https://api.jikan.moe/v4/anime', params= searchparams)
    redata = re.json()
    re_len = str(str(redata).count('title_english'))
    if response.status_code >= 400:
        print("No results found.")
    elif redata['data'] == []:
        print("No results found.")
    else:
        print(re_len + " result(s) found:")
        print(print(json.dumps(redata, indent= 4, sort_keys= True)))
        
anime_search()