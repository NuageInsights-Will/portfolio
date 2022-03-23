import requests as rq
import json


def animesearch(q: str) -> dict:
    searchparams = {
        "q": q,
        "limit": 20,
        "order_by": "popularity",
        "sort": "asc",
    }
    re = rq.get("https://api.jikan.moe/v4/anime", params=searchparams)
    data = re.json()
    results = str(str(data).count("title_english"))
    if re.status_code >= 400:
        print("No results found.")
    elif data["data"] == []:
        print("No results found.")
    else:
        print(results + " result(s) found:")
        return json.dumps(data, indent=4, sort_keys=True)


q = input("Search for anime: ")
animes = animesearch(q)

print(animes)
