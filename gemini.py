import os
from dotenv import load_dotenv
import google.generativeai as genai

# Tải biến môi trường từ file .env
load_dotenv()

# Lấy khóa API từ biến môi trường
API_KEY = os.getenv("GEMINI_API_KEY")

# Hàm để đọc nội dung từ file SRT
def read_srt_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Cấu hình API Gemini và tạo prompt
def generate_content_from_srt(file_path, num_chapters):
    # Đọc nội dung file SRT
    srt_content = read_srt_file(file_path)

    # Cấu hình khóa API
    genai.configure(api_key=API_KEY)

    # Tạo prompt tùy chỉnh với vai trò và yêu cầu chi tiết
    custom_prompt = (
        "You are a content creator tasked with structuring video content into sections and adding timestamps. "
        f"The video has been transcribed into sentences with their respective timestamps, provided below.\n\n"
        f"Here is the content:\n{srt_content}\n\n"
        f"Please divide the content into {num_chapters} chapters. "
        "For each chapter, provide only the starting timestamp and a single-sentence summary. Format the output as 'MM:SS - Summary'."
    )

    # Khởi tạo mô hình và gửi yêu cầu với prompt
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(custom_prompt)

    # Kiểm tra và in ra kết quả phản hồi theo định dạng mong muốn
    if response and response.text:
        print(response.text.strip())
    else:
        print("No response or content returned from the API.")

