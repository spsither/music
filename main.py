import os
import yt_dlp

# === CONFIGURATION ===
playlist_url = 'https://www.youtube.com/playlist?list=PLPPFi2KpH0UTY1cCZAeMrBwNAa68Oeeii'
output_folder = 'downloads'
archive_file = 'downloaded.txt'

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# yt-dlp options
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(output_folder, '%(playlist_index)s - %(title)s.%(ext)s'),
    'download_archive': archive_file,  # <-- Prevent re-downloading
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'ignoreerrors': True,
    'noplaylist': False,
    'quiet': False,
    'no_warnings': True,
}

# Run yt-dlp
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])
