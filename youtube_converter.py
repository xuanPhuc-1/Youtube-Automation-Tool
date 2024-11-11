from yt_dlp import YoutubeDL
from moviepy.editor import *
import os
from datetime import datetime

def download_youtube_audio_as_wav(url):
    try:
        # Tạo thư mục "audio" nếu chưa có
        if not os.path.exists("audio"):
            os.makedirs("audio")
        
        # Tạo UUID từ thời gian hiện tại làm tên file
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"audio/{current_time}.wav"
        
        # Sử dụng yt-dlp để tải audio
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'temp.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        # Chuyển đổi sang định dạng .wav
        audio = AudioFileClip("temp.mp3")
        audio.write_audiofile(output_filename)
        
        # Xóa file tạm
        audio.close()
        os.remove("temp.mp3")
        return output_filename
    except Exception as e:
        print("Có lỗi xảy ra:", e)


