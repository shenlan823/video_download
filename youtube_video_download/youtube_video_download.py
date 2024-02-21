from yt_dlp import YoutubeDL  
import requests  
import sys  
import sqlite3  
import os  
from prettytable import PrettyTable  
from urllib import request  
from bs4 import BeautifulSoup  
import os  
import ffmpeg
  
# 确保下载目录存在  
if not os.path.exists('Downloads'):  
    os.makedirs('Downloads')
  
def download_video(video_url):  
    ydl_opts = {  
        'format': 'bestvideo+bestaudio/best',  
        'outtmpl': 'Downloads/%(title)s-%(id)s.%(ext)s',  # 使用标题作为文件名，并保留扩展名  
        'restrictfilenames': True,  
        'noplaylist': True,  
        'ignoreerrors': True,  
        # 'verbose': True,  
    }  
  
    with YoutubeDL(ydl_opts) as ydl:  
        try:  
            info_dict = ydl.extract_info(video_url, download=False)  
            print(f"Title: {info_dict['title']}")  
            print(f"ID: {info_dict['id']}")  
              
            # 如果需要，可以在这里对标题进行处理，例如替换非法字符或截断过长的标题             

            # 开始下载视频  
            ydl.download([video_url])  
        except Exception as e:  
            print(f"An error occurred: {e}")  
  
# Define the URL list and the loop here  
# url_list = ['https://www.youtube.com/watch?v=PDiO8cIjlGE']
url_list = []  
  
while True:  
    url = input("Enter a YouTube URL (or 'quit' to finish): ")  
    if url.lower() == 'quit':  
        break  
    url_list.append(url)    
  
for i in url_list:  
    print(i)  
    download_video(i)
    print("下载完成")