### Random Acclaimed Song

This builds the file used in random-acclaimed-song.

#### How often will I need to run this?

YouTube is more ban-happy than I'd like, so I assume I'll have to run this script at least annually.

YouTube's Search API has a daily usage limit of 100 requests per day per API key (in practice, I seem to get 97). Since there's ~10,000 songs I'd like to process with 11 API keys, it will always take me at least 10 days to write Youtube ID's to an output file.

I can set up `schtasks` to do this for me, so it isn't that much of a hassle, but still, two weeks is two weeks.

There's probably an easier way to do this. Maybe use a less costly API to check if videos exist, then only download when needed?

### To-Do

* Write maintenance script that checks if each video is playable in US. If is, write to output file. If isn't, search for video that is and write to output file.

* https://www.googleapis.com/youtube/v3/videos?part=contentDetails&key=AIzaSyBQnISjzNNGwITiZ9IGa8h-ACv-zFcQnZw&id=02D2T3wGCYg
    ```
    {
     "kind": "youtube#videoListResponse",
     "etag": "\"XpPGQXPnxQJhLgs6enD_n8JR4Qk/XMSAhkcZGO5aLs8WMTgnzNLM1LY\"",
     "pageInfo": {
      "totalResults": 1,
      "resultsPerPage": 1
     },
     "items": [
      {
       "kind": "youtube#video",
       "etag": "\"XpPGQXPnxQJhLgs6enD_n8JR4Qk/XPGRBEtY5AWUaDyKVLvdNfGYDMs\"",
       "id": "02D2T3wGCYg",
       "contentDetails": {
        "duration": "PT3M19S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "false",
        "licensedContent": false,
        "projection": "rectangular"
       }
      }
     ]
    }
    ```

* https://www.googleapis.com/youtube/v3/videos?part=contentDetails&key=AIzaSyBQnISjzNNGwITiZ9IGa8h-ACv-zFcQnZw&id=CKgj1FNToWY
    ```
    {
     "kind": "youtube#videoListResponse",
     "etag": "\"XpPGQXPnxQJhLgs6enD_n8JR4Qk/Rk41fm-2TD0VG1yv0-bkUvcBi9s\"",
     "pageInfo": {
      "totalResults": 0,
      "resultsPerPage": 0
     },
     "items": []
    }
    ```

* https://www.googleapis.com/youtube/v3/videos?part=contentDetails&key=AIzaSyBQnISjzNNGwITiZ9IGa8h-ACv-zFcQnZw&id=NpQ88a6zy8E
    ```
    {
     "kind": "youtube#videoListResponse",
     "etag": "\"XpPGQXPnxQJhLgs6enD_n8JR4Qk/cUl56bOUdFswjXCguH8hOoBS7PE\"",
     "pageInfo": {
      "totalResults": 1,
      "resultsPerPage": 1
     },
     "items": [
      {
       "kind": "youtube#video",
       "etag": "\"XpPGQXPnxQJhLgs6enD_n8JR4Qk/NDTIxFetwZFUHKdyiAqOzFv3Xwg\"",
       "id": "NpQ88a6zy8E",
       "contentDetails": {
        "duration": "PT5M28S",
        "dimension": "2d",
        "definition": "sd",
        "caption": "false",
        "licensedContent": false,
        "regionRestriction": {
         "blocked": [
          "CZ","CY","CX","CW","CV","CU","CR","CO","CN","CM","CL","CK","CI","CH","CG","CF","ML","CD","CC","CA","SO","SN","SM","SL","SK","SJ","SI","SH","HR","SE","SD","SC","SB","HT","HU","HK","NO","HN","SZ","SY","HM","SV","ST","SS","SR","BY","BZ","BQ","BR","BS","BT","GA","BV","BW","BH","BI","BJ","GH","BL","BM","BN","BO","BA","BB","BD","BE","BF","BG","KG","KE","RO","KN","KM","ZW","RE","KI","KH","KW","ZA","KR","KP","RS","KZ","KY","RW","IM","GF","GD","UY","JE","UZ","IL","JM","US","JO","JP","UG","UA","IO","DM","DJ","DK","MU","MT","MW","MV","TZ","EH","MS","MR","EE","TW","TT","MY","MX","EC","RU","ME","MD","MG","TM","MA","TK","MC","PM","MM","TG","MO","MN","MH","MK","ER","IS","SA","LV","DO","LT","LU","LR","LS","WS","DE","LY","DZ","LC","LA","LB","LK","LI","FR","SX","AX","MQ","FO","FI","FJ","MP","VE","GI","VG","VA","GM","VC","GU","GB","VN","GG","VI","GE","WF","TV","GY","GS","GR","GQ","GP","GW","EG","OM","GT","AQ","AS","AR","AU","AT","AW","TR","AZ","YE","AE","AD","AG","AF","AI","MZ","AM","AL","FM","QA","TN","FK","NZ","TO","NU","NP","TL","NR","YT","NL","ES","MF","NI","GN","NE","NF","NG","NA","NC","TH","AO","SG","VU","TF","ET","TD","UM","PA","PF","PG","PE","IQ","PK","PH","IR","PN","IT","PL","TC","PR","PS","ZM","GL","TJ","PW","PT","IN","PY","IE","ID"
         ]
        },
        "projection": "rectangular"
           }
          }
         ]
        }
    ```

* https://www.googleapis.com/youtube/v3/videos?part=contentDetails&key=AIzaSyBQnISjzNNGwITiZ9IGa8h-ACv-zFcQnZw&id=TJgiTCkoJFM

    ```
     "kind": "youtube#videoListResponse",
     "etag": "\"XpPGQXPnxQJhLgs6enD_n8JR4Qk/0fVCc9Wk0yVnqmlVCu5lk1DwlLQ\"",
     "pageInfo": {
      "totalResults": 1,
      "resultsPerPage": 1
     },
     "items": [
      {
       "kind": "youtube#video",
       "etag": "\"XpPGQXPnxQJhLgs6enD_n8JR4Qk/bVWHoWh2_KMqm37PCq9GzPfGsjI\"",
       "id": "TJgiTCkoJFM",
       "contentDetails": {
        "duration": "PT4M26S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "false",
        "licensedContent": true,
        "regionRestriction": {
         "allowed": [
          "PY","LI","PT","PR","PL","LV","LU","LT","PE","PA","KR","CH","GB","CO","CL","MX","CA","CZ","GT","GU","GR","CR","TR","IN","ID","IE","MK","MT","IS","IT","HU","HR","UA","DK","DO","UY","HN","DE","US","NL","NO","NI","BE","RS","RU","VE","RO","NZ","VI","ZA","ES","AR","AS","AT","AU","EE","EC","SV","SK","SI","SE","JP","BO","BA","FI","BG","BY","FR","CY","BR"
         ]
        },
        "projection": "rectangular"
       }
      }
     ]
    }
    ```

* https://www.googleapis.com/youtube/v3/videos?part=status&key=AIzaSyBQnISjzNNGwITiZ9IGa8h-ACv-zFcQnZw&id=Ldyx3KHOFXw

    ```
    {
     "kind": "youtube#videoListResponse",
     "etag": "\"XpPGQXPnxQJhLgs6enD_n8JR4Qk/Js7-vyqzYRehGGaYnSPHo6Ouh6U\"",
     "pageInfo": {
      "totalResults": 1,
      "resultsPerPage": 1
     },
     "items": [
      {
       "kind": "youtube#video",
       "etag": "\"XpPGQXPnxQJhLgs6enD_n8JR4Qk/9mlWHJaDwMHlQYzknvLuUtgQ5VY\"",
       "id": "Ldyx3KHOFXw",
       "status": {
        "uploadStatus": "processed",
        "privacyStatus": "public",
        "license": "youtube",
        "embeddable": false,
        "publicStatsViewable": true
       }
      }
     ]
    }
    ```