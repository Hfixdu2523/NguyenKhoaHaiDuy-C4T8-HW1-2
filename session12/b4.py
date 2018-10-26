from youtube_dl import YoutubeDL

options = {
    'default_search': 'ytsearch5'
}

ydl = YoutubeDL(options)
search_result = ydl.extract_info('that girl', False)
print(search_result)

import json
var = search_result
with open('data2.json', 'w') as outfile:
    json.dump(var, outfile)