#Audio pre-processing
import os

import shutil

def merge_audiofiles_from_folders ():
    src = r'/Volumes/MA-Tobi/merge'
    dest = r'/Volumes/MA-Tobi/merged'
    print('Merging audio files into one folder...')
    for path, subdirs, files in os.walk(src):
        for name in files:
            filename = os.path.join(path, name)
            shutil.copy2(filename, dest)
    print('Audio-Files-Merge complete, dir "merged" created ')


merge_audiofiles_from_folders()
