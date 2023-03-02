import requests
import json 

x = input("Enter any word: ")
response = requests.get("https://api.giphy.com/v1/gifs/search?api_key=NAk2UDQKmSuGCDhNnnDsB1jgJVo5f2Ts&q={x}&limit=1&offset=0&rating=g&lang=en")
links_to_gifs = []
for obj in response.json():
    if obj == 'url':
        links_to_gifs.append(obj)
print(links_to_gifs)
