# from __future__ import unicode_literals               c)
# import youtube_dl

# ydl_opts = {}
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://www.youtube.com/watch?v=n6BwAWiHcSg&t=182s'])

# from __future__ import unicode_literals               # d)
# import youtube_dl
# ydl_opts = {}
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     URL = ['https://www.youtube.com/watch?v=GIDoQsQyS0s', 'https://www.youtube.com/watch?v=Wv2rLZmbPMA']
#     ydl.download(URL)

# from __future__ import unicode_literals               # e)
# import youtube_dl
# ydl_opts = {}
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     r = ydl.extract_info('https://www.youtube.com/watch?v=Wv2rLZmbPMA', download=False)
#     print(r)

from __future__ import unicode_literals               # f)
import youtube_dl
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    URL = ['https://www.youtube.com/watch?v=Wv2rLZmbPMA', 'https://www.youtube.com/watch?v=n6BwAWiHcSg&t=182s', 'https://www.youtube.com/watch?v=GIDoQsQyS0s']
    for i in URL:
        ext = ydl.extract_info(i, download = False)
    exted = [ext]
    print(exted)

import json
var = exted
with open('data1.json', 'w') as outfile:
    json.dump(var, outfile)


# var = 'I love manga and anime'                        # g)
# with open('LOL.txt', 'a') as out:
#     out.write(var + '\n')