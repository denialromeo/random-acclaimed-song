import csv
import json
import re
import requests

DIR      = "C:\\Users\\hi\\Desktop\\code\\random-acclaimed-song\\"
INFILE   = DIR + "all-songs"
OUTFILE  = DIR + "written"
TEMPFILE = DIR + "new-written"

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

def wikipedia_title(artist):
    url = "https://en.wikipedia.org/w/api.php"
    search_string = re.compile("( [fF]eat\.?)|( with )").split(artist)[0]
    payload = {"action": "query", "list": "search", "format": "json", "srsearch": search_string}
    response = poll_api(url, payload)
    poss_title = response["query"]["search"][0]["title"]
    if ((poss_title.lower() == search_string.lower()) and ("may refer to" not in response["query"]["search"][0]["snippet"])):
        return poss_title
    else:
        payload["srsearch"] = search_string + " band"
        response = poll_api(url, payload)
        poss_title = response["query"]["search"][0]["title"]
        return poss_title

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
    print(response["items"][0]["snippet"]["title"], response["items"][0]["id"]["videoId"])
    return response["items"][0]["id"]["videoId"]

def video_title(video_id):
    url = "https://www.googleapis.com/youtube/v3/videos"
    payload = {"part": "snippet", "id": video_id}
    response = get_response(url, payload)
    title = response["items"][0]["snippet"]["title"]
    if ("lyric" in title) or ("Lyric" in title):
        print(title.encode('utf-8'))

def video_is_playable_in_US(video_id):
    video_id = video_id[0:11]
    url = "https://www.googleapis.com/youtube/v3/videos"
    payload = {"part": "contentDetails", "id": video_id}
    response = get_response(url, payload)
    if not (len(response["items"]) > 0): # Does the video exist?
        return False
    if "contentDetails" not in response["items"][0]:
        return False
    contentDetails = response["items"][0]["contentDetails"]
    if "regionRestriction" in contentDetails:
        if "blocked" in contentDetails["regionRestriction"]:
            return (not ("US" in contentDetails["regionRestriction"]["blocked"]))
        elif "allowed" in contentDetails["regionRestriction"]:
            return ("US" in contentDetails["regionRestriction"]["allowed"])
    return True

def video_is_embeddable(video_id):
    url = "https://www.googleapis.com/youtube/v3/videos"
    payload = {"part": "status", "id": video_id}
    response = get_response(url, payload)
    return response["items"][0]["status"]["embeddable"]

def num_lines_in_file(file):
    with open(file) as f:
        return sum(1 for line in f)

def append_to_file(file, row):
    with open(file, "a") as csvfile:
        csv.writer(csvfile, delimiter="|", lineterminator="\n", quotechar="~").writerow(row)

def initial():
    num_songs_written = num_lines_in_file(OUTFILE)
    with open(INFILE) as csvfile:
        for idx, row in enumerate(csv.reader(csvfile, delimiter="|")):
            if (idx >= num_songs_written):
                search_string = row[0] + " " + row[1]
                row.append(get_youtube_id(search_string))
                append_to_file(OUTFILE, row)

def wikipedia_titles():
    num_songs_written = num_lines_in_file(TEMPFILE)
    with open(OUTFILE) as csvfile:
        for idx, row in enumerate(csv.reader(csvfile, delimiter="|")):
            if (idx >= num_songs_written):
                row.append(wikipedia_title(row[0]))
                append_to_file(TEMPFILE, row)

def maintenance():
    num_songs_written = num_lines_in_file(TEMPFILE)
    with open(OUTFILE) as csvfile:
        for idx, row in enumerate(csv.reader(csvfile, delimiter="|")):
            if (idx >= num_songs_written):
                video_id = row[3]
                if video_id.startswith("http"):
                    pass
                elif (video_is_playable_in_US(video_id)):
                    pass
                else:
                    search_string = row[0] + " " + row[1]
                    row[3] = get_youtube_id(search_string)
                append_to_file(TEMPFILE, row)

def print_titles(s=0):
    with open(OUTFILE) as csvfile:
        for idx, row in enumerate(csv.reader(csvfile, delimiter="|")):
            if (idx >= s):
                video_id = row[3]
                if video_id.startswith("http"):
                    continue
                video_title(video_id)

if __name__ == "__main__":
    maintenance()
    # print_titles()