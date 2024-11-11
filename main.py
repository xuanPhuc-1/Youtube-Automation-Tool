import tkinter as tk
from tkinter import filedialog
import subprocess
import os
from youtube_converter import download_youtube_audio_as_wav
from gemini import generate_content_from_srt
def run_whisper(file_path):
    # Xác định đường dẫn tới whisper-faster.exe và output folder
    whisper_path = "./Faster-Whisper-XXL/faster-whisper-xxl.exe"
    output_dir = "timestamps-ouput"
    
    # Tạo lệnh tương tự command bạn đã đưa ra
    command = [whisper_path, file_path, "--language", "English", "--model", "medium", "--output_dir", output_dir]
    
    print(f"Running command: {' '.join(command)}")
    # Chạy lệnh bằng subprocess
    try:
        subprocess.run(command, check=True)
        return os.path.join(output_dir, file_path.split('/')[-1].replace('.wav', '.srt'))
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Chọn file và chạy lệnh whisper
    youtube_url = input("Nhập link YouTube: ")
    audio_file = download_youtube_audio_as_wav(youtube_url)
    
    if audio_file:
        output = run_whisper(audio_file)
        
        # Nhập số chương từ người dùng
        num_chapters = int(input("Nhập số chương bạn muốn tạo: "))
        
        # Biến để kiểm tra nếu người dùng muốn thử lại
        retry = True
        while retry:
            # Gọi hàm tạo nội dung
            generate_content_from_srt(output, num_chapters)
            
            # Hỏi người dùng xem có muốn thử lại không
            user_input = input("Bạn có hài lòng với kết quả không? (Y/N): ").strip().lower()
            if user_input == "y":
                retry = False
            else:
                print("Chạy lại với nội dung và số chương cũ.")
    else:
        print("No file selected.")

