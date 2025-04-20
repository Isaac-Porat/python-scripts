import scrapetube

channel_id = 'UCuzbImxdBNTUeolGXpLVL0A'

videos = scrapetube.get_channel(channel_id=channel_id)

with open('name.txt', 'w', encoding='utf-8') as f:
    for video in videos:
        title = video['title']['runs'][0]['text']
        video_id = video['videoId']
        f.write(f"{title} - https://www.youtube.com/watch?v={video_id}\n")
