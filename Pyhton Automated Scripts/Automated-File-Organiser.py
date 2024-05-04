import os
from pathlib import Path
import shutil

# Point the code to the correct directory
os.chdir('/Users/R2/Downloads')

# First get all different file types example
music_file = {'mp3','mp4', 'WAV','FLAC'}

video_files=['mkv','avi', 'mov']

image_files = ['JPEG','GIF','PNG','PSD']

def is_audio(file):
    return os.path.splitext(file)[1] in music_file
def is_video(file):
    return os.path.splitext(file)[1] in video_files
