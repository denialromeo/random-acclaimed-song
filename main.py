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

def poll_api(url, payload):
    return json.loads(requests.get(url, payload).text)

def get_response(url, payload):
    payload["key"] = api_keys[-1]
    response = poll_api(url, payload)
    while "error" in response:
        print(response["error"]["errors"][0]["message"][0:76])
        api_keys.pop()
        payload["key"] = api_keys[-1]
        response = poll_api(url, payload)
    return response

def get_youtube_id(search_string):
    url = "https://www.googleapis.com/youtube/v3/search"
    payload = {"part": "snippet", "q": search_string, "maxResults": 1, "type": "video", "regionCode": "US", "videoEmbeddable": "true"}
    response = get_response(url, payload)
    print(response["items"][0]["snippet"]["title"])
    return response["items"][0]["id"]["videoId"]

def video_exists(id):
    url = "https://www.googleapis.com/youtube/v3/videos"
    payload = {"part": "contentDetails", "id": id}
    response = get_response(url, payload)
    return (len(response["items"]) > 0)

def video_is_playable_in_US(id):
    url = "https://www.googleapis.com/youtube/v3/videos"
    payload = {"part": "contentDetails", "id": id}
    response = get_response(url, payload)
    contentDetails = response["items"][0]["contentDetails"]
    if "regionRestriction" in contentDetails:
        if "blocked" in contentDetails["regionRestriction"]:
            if "US" in contentDetails["regionRestriction"]["blocked"]:
                return False
        elif "allowed" in contentDetails["regionRestriction"]:
            if "US" in contentDetails["regionRestriction"]["allowed"]:
                return True
    return True

def video_is_embeddable(id):
    url = "https://www.googleapis.com/youtube/v3/videos"
    payload = {"part": "status", "id": id}
    response = get_response(url, payload)
    return response["items"][0]["status"]["embeddable"]

def num_lines_in_file(file):
    with open(file) as f:
        return sum(1 for line in f)

def append_to_file(file, row):
    with open(file, "a") as csvfile:
        csv.writer(csvfile, delimiter="|", lineterminator="\n", quotechar="~").writerow(row)

if __name__ == "__main__":
    num_songs_written = num_lines_in_file(OUTFILE)
    with open(INFILE) as csvfile:
        for idx, row in enumerate(csv.reader(csvfile, delimiter="|")):
            if (idx >= num_songs_written):
                search_string = row[0] + " " + row[1]
                row.append(get_youtube_id(search_string))
                append_to_file(OUTFILE, row)