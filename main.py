import csv
import json
import requests

INFILE  = "all-songs"
OUTFILE = "written"

api_keys = ["AIzaSyBQnISjzNNGwITiZ9IGa8h-ACv-zFcQnZw",
            "AIzaSyD708scD_-j8jkICMSLnhWl9wTDMEN9w3c",
            "AIzaSyD6aJcm4_kvngKdzyh59yOZ_5dM_2NwSvc",
            "AIzaSyBXIjogxwr82ek2VYgEg9RHt3sRP4Ekf58",
            "AIzaSyDHzbRIM7RxxEwTd0lJBeQuaNvp3udKBRo",
            "AIzaSyDEfuQXfKR2yYPTMEgMSelgq7G0wnuttxw",
            "AIzaSyB9fqAJboeWVkw16vbTS6CDT5eQ3NOrDK8",
            "AIzaSyC7jeqYlI0of9ytBWsFCMil_1BHLECaSXw",
            "AIzaSyAX5l_PLHVgw1OC-hepf2SHgSIDC-2uUlE",
            "AIzaSyBUY4lBhusyDjODp0o6dfJNAg3gxmpDIe4",
            "AIzaSyAES65sOUOS22G4XD5ink6EBEoIAN-WUmo"]

def get_response(payload):
    return json.loads(requests.get("https://www.googleapis.com/youtube/v3/search", payload).text)

def get_youtube_id(search_string):
    payload = {"part": "snippet", "key": api_keys[-1], "q": search_string, "maxResults": 1, "type": "video", "regionCode": "US", "videoEmbeddable": "true"}
    response = get_response(payload)
    while "error" in response:
        print(response["error"]["errors"][0]["message"][0:80])
        api_keys.pop()
        payload["key"] = api_keys[-1]
        response = get_response(payload)
    print(response["items"][0]["snippet"]["title"])
    return response["items"][0]["id"]["videoId"]

def num_songs_processed():
    with open(OUTFILE) as f:
        return sum(1 for line in f)

def write_to_output(row):
    with open(OUTFILE, "a") as csvfile:
        csv.writer(csvfile, delimiter="|", lineterminator="\n").writerow(row)

if __name__ == "__main__":
    num_songs_written = num_songs_processed()
    with open(INFILE) as csvfile:
        for idx, row in enumerate(csv.reader(csvfile, delimiter="|")):
            if (idx >= num_songs_written):
                search_string = str.join(" ", row[0:2])
                row.append(get_youtube_id(search_string))
                write_to_output(row)