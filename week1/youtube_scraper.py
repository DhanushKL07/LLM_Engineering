import sys
from yt_dlp import YoutubeDL  # pyright: ignore[reportMissingImports]


def get_youtube_video_info(video_url: str) -> dict:
    """Extracts metadata from a given YouTube video URL."""
    ydl_opts = {
        'quiet': True,
        'skip_download': True,  # Only fetch metadata, do not download the video
        'extract_flat': False,
        'no_warnings': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(video_url, download=False)
            return {
                "title": info.get("title"),
                "uploader": info.get("uploader"),
                "view_count": info.get("view_count"),
                "like_count": info.get("like_count"),
                "duration_seconds": info.get("duration"),
                "upload_date": info.get("upload_date"),
                "description": info.get("description"),
                "thumbnail_url": info.get("thumbnail"),
            }
        except Exception as e:
            return {"error": str(e)}
