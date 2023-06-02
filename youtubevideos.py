from googleapiclient.discovery import build

def get_video_details(video_id):
    youtube = build('youtube', 'v3', developerKey='AIzaSyDnsbCvMA7PVuMiHWAPPkwjDQhm_ANEhM0')
    request = youtube.videos().list(part='snippet,statistics', id=video_id)
    response = request.execute()
    return response

video_id = 'dQw4w9WgXcQ'
details = get_video_details(video_id)
print(details)

def print_video_details(details):
    title = details['items'][0]['snippet']['title']
    view_count = details['items'][0]['statistics']['viewCount']
    print(f'Title: {title}')
    print(f'View count: {view_count}')

print_video_details(details)