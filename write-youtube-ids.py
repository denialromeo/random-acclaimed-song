import csv
import json
import requests

INFILE  = "all-songs"
OUTFILE = "written"

api_keys = ["AIzaSyBQnISjzNNGwITiZ9IGa8h-ACv-zFcQnZw",
            "AIzaSyD708scD_-j8jkICMSLnhWl9wTDMEN9w3c",
            "AIzaSyD6aJcm4_kvngKdzyh59yOZ_5dM_2NwSvc",
            "AIzaSyBXIjogxwr82ek2VYgEg9RHt3sRP4Ekf58",
            "AIzaSyAX5l_PLHVgw1OC-hepf2SHgSIDC-2uUlE",
            "AIzaSyBUY4lBhusyDjODp0o6dfJNAg3gxmpDIe4",
            "AIzaSyAES65sOUOS22G4XD5ink6EBEoIAN-WUmo"]

def get_youtube_id(search_string):
    payload = {"part": "snippet", "key": api_keys[-1], "q": search_string, "maxResults": 1, "type": "video"}
    try:
        response = requests.get("https://www.googleapis.com/youtube/v3/search", payload).text
    except KeyError: # When we hit the YouTube API daily usage limit.
        api_keys.pop()
        payload["key"] = api_keys[-1]
        response = requests.get("https://www.googleapis.com/youtube/v3/search", payload).text
    return json.loads(response)["items"][0]["id"]["videoId"]

def num_songs_processed():
    with open(OUTFILE) as f:
        return sum(1 for line in f)

def write_to_output(row):
    with open(OUTFILE, "a") as csvfile:
        output_writer = csv.writer(csvfile, delimiter="|", lineterminator="\n")
        output_writer.writerow(row)

if __name__ == "__main__":
    num_songs_written = num_songs_processed()
    with open(INFILE) as csvfile:
        input_reader = csv.reader(csvfile, delimiter="|")
        for idx, row in enumerate(input_reader):
            if (idx >= num_songs_written):
                search_string = str.join(" ", row[0:2])
                row.append(search_string)
                write_to_output(row)