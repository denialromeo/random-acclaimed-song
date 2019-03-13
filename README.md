### Random Acclaimed Song

This builds the file used in random-acclaimed-song.

#### How often will I need to run this?

YouTube is more ban-happy than I'd like, so I assume I'll have to run this script at least annually.

YouTube's Search API has a daily usage limit of 100 requests per day per API key (in practice, I seem to get 97). Since there's ~10,000 songs I'd like to process with 11 API keys, it will always take me at least 10 days to write Youtube ID's to an output file.

I can set up `schtasks` to do this for me, so it isn't that much of a hassle, but still, two weeks is two weeks.