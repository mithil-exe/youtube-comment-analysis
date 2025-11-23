from googleapiclient.discovery import build
import pandas as pd

api_key = "AIzaSyAQOvx9PqVJkzMkTVeRYrG6XPH2KT28CWQ"   # paste your API key
video_id = "YG1sW00jwLY"      # e.g. dQw4w9WgXcQ

youtube = build('youtube', 'v3', developerKey=api_key)

comments = []
next_page_token = None

while True:
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,
        pageToken=next_page_token,
        textFormat="plainText"
    )
    response = request.execute()

    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    next_page_token = response.get('nextPageToken')

    if next_page_token is None:
        break

df = pd.DataFrame({"Comment": comments})
df.to_csv("youtube_comments.csv", index=False)

print("Comments downloaded:", len(comments))
