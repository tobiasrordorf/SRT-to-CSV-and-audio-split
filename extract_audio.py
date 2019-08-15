#Source:
# - https://zulko.github.io/moviepy/
# - https://medium.com/@steadylearner/how-to-extract-audio-from-the-video-with-python-aea325f434b6

#19.06.2019

import sys
from moviepy.editor import *
from glob import glob

#Loop through every file in folder audio that ends with .wmv
for entry in glob('./audio/*.wmv'):
    video = VideoFileClip(entry)
    #extract audio from video
    audio = video.audio
    #write audio file with specified ending .wav
    audio.write_audiofile(entry + '.wav')
print('WMV to WAV convert complete')
