from googleapiclient.discovery import build
import requests
import os

# Your YouTube Data API Key
API_KEY = "YOUR_API_KEY"

# Initialize YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

def fetch_videos(channel_id, max_results=10):
    # Fetch videos from a specific channel
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=max_results,
        type="video",
        order="date"  # Fetch the latest videos
    )
    response = request.execute()

    video_data = []
    for item in response['items']:
        video_id = item['id']['videoId']
        title = item['snippet']['title']
        thumbnail_url = item['snippet']['thumbnails']['high']['url']

        # Fetch video statistics
        stats = youtube.videos().list(part="statistics", id=video_id).execute()
        view_count = stats['items'][0]['statistics'].get('viewCount', 0)
        like_count = stats['items'][0]['statistics'].get('likeCount', 0)

        video_data.append({
            "title": title,
            "video_id": video_id,
            "thumbnail_url": thumbnail_url,
            "views": int(view_count),
            "likes": int(like_count)
        })

    return video_data

def save_thumbnails(video_data, output_folder="thumbnails"):
    # Save thumbnails to a local folder
    os.makedirs(output_folder, exist_ok=True)
    for video in video_data:
        thumbnail_url = video['thumbnail_url']
        thumbnail_path = os.path.join(output_folder, f"{video['video_id']}.jpg")
        with open(thumbnail_path, "wb") as f:
            f.write(requests.get(thumbnail_url).content)
        print(f"Saved thumbnail: {thumbnail_path}")

# Example usage
channel_id = "UCXXhZ89ffJvNg7XuDmS_Zlw"  # Replace with a real channel ID
video_data = fetch_videos(channel_id, max_results=5)
print(video_data)

# Save thumbnails locally
save_thumbnails(video_data)
