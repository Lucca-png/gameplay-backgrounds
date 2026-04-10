import os, json, urllib.parse

videos_dir = 'videos'
base_url = 'https://raw.githubusercontent.com/Lucca-png/gameplay-backgrounds/main/videos/'

videos = []
if os.path.isdir(videos_dir):
    for f in sorted(os.listdir(videos_dir)):
        if f.endswith('.mp4'):
            url = base_url + urllib.parse.quote(f)
            videos.append({'file': f, 'url': url})

result = {'videos': videos, 'count': len(videos)}

with open('index.json', 'w') as out:
    json.dump(result, out, indent=2)

print(f'Index gerado com {len(videos)} videos')
