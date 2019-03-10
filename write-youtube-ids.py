import fileinput
import json
import requests

def get_youtube_id(search_string):
    # API_KEY = "AIzaSyBQnISjzNNGwITiZ9IGa8h-ACv-zFcQnZw"
    # API_KEY = "AIzaSyD708scD_-j8jkICMSLnhWl9wTDMEN9w3c"
    # API_KEY = "AIzaSyD6aJcm4_kvngKdzyh59yOZ_5dM_2NwSvc"
    # API_KEY = "AIzaSyBXIjogxwr82ek2VYgEg9RHt3sRP4Ekf58"
    API_KEY = "AIzaSyAX5l_PLHVgw1OC-hepf2SHgSIDC-2uUlE"
    # API_KEY = "AIzaSyBUY4lBhusyDjODp0o6dfJNAg3gxmpDIe4"
    # API_KEY = "AIzaSyAES65sOUOS22G4XD5ink6EBEoIAN-WUmo"
    payload = {"part": "snippet", "key": API_KEY, "q": search_string, "maxResults": 1, "type": "video"}
    response = requests.get("https://www.googleapis.com/youtube/v3/search", payload).text
    return json.loads(response)["items"][0]["id"]["videoId"]

def write_youtube_ids():
    for line in fileinput.input("to-write", inplace=True):
        line = line.rstrip('\n')
        values = line.split("|")
        search_string = str.join(" ", values[0:2])
        youtube_id = get_youtube_id(search_string)
        print(line + "|" + youtube_id)

if __name__ == "__main__":
    write_youtube_ids()