#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

# <bitbar.title>HN Front Page</bitbar.title>
# <bitbar.author>AbdulMajedRaja</bitbar.author>
# <bitbar.author.github>amrrs</bitbar.author.github>
# <bitbar.desc>Display Top Hacker News Headlines</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>
# <bitbar.version>1.0</bitbar.version>
#
# 1 second refresh rate may be overkill. Wording & formatting of the time may
# also be easily altered below.

import requests
content = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
ids = content.json()
print("HN")
story_base = "https://hacker-news.firebaseio.com/v0/item/"
hn_link = "https://news.ycombinator.com/item?id="
print('---')
for id in ids[:10]:
    story = requests.get(story_base + str(id) + ".json")
    story_json = story.json()
    print(story_json["title"] + "| href = https://news.ycombinator.com/item?id=" + str(id))
