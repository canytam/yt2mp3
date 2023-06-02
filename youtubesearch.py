from googleapiclient.discovery import build

def search_videos(query):
    request = youtube.search().list(part='id', type='video', q=query, maxResults=50)
    response = request.execute()
    video_ids = [item['id']['videoId'] for item in response['items']]
    video_details = get_video_details(video_ids)
    return video_details

def get_video_details(video_ids):
    request = youtube.videos().list(part='snippet', id=','.join(video_ids))
    response = request.execute()
    return response['items']

youtube = build('youtube', 'v3', developerKey='AIzaSyDnsbCvMA7PVuMiHWAPPkwjDQhm_ANEhM0')
query = '姜濤'
video_details = search_videos(query)
for item in video_details:
    title = item['snippet']['title']
    print(f'Title: {title}')