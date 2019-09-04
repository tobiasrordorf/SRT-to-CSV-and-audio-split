#This script will change the encoding of the srt file, and then extract the information as well
#as store it in a csv file. According to the info in this csv file, the audio is splitted
#the splitted audio and transcripts are then merged, cleaned and splitted into three subsets

import pandas as pd
import os, io, re, sys, time, datetime
from glob import glob
import numpy as np

from util.creating_directories import create_directories
from util.convert_srt_to_csv import change_encoding
from util.convert_srt_to_csv import convert_srt_to_csv
from util.change_sample_rate import pre_process_audio
from util.extract_audio import wmv_to_wav
from util.extract_audio import mp4_to_wav
from util.slice_audio import split_files
from util.create_DS_csv import create_DS_csv
from util.merge_csv import merge_csv
from util.merge_transcripts_and_files import merge_transcripts_and_wav_files
from util.clean import clean_unwanted_characters
from util.split import split_dataset
from util.audio_metrics import audio_metrics

start_time = time.time()

#Check if srt_files directory exists and contains srt files

srt_path = './srt_files'
'''
if os.path.exists(srt_path):
    print('Folder %s exists.. continuing processing..' %srt_path)
else:
    print('Folder "srt_files" is missing')
    try:
        os.mkdir(srt_path)
    except OSError:
        print('Creation of directory %s failed' %srt_path)
    else:
        print('Successfully created the directory %s' %srt_path)
    print('--> Please add srt files to folder %s' %srt_path)
    sys.exit()

#Check if audio directory exists and contains wmv or wav files

audio_path = './audio/'

if os.path.exists(audio_path):
    print('Folder %s exists.. continuing processing..' %audio_path)
else:
    print('Folder "audio" is missing')
    try:
        os.mkdir(audio_path)
    except OSError:
        print('Creation of directory %s failed' %audio_path)
    else:
        print('Successfully created the directory %s' %audio_path)
    print('--> Please add wav or wmv files to folder %s' %audio_path)
    sys.exit()

srt_counter = len(glob('./srt_files/' + '*.srt'))

if srt_counter == 0:
    print('!!! Please add srt_file(s) to %s-folder' %srt_path)
    sys.exit()
'''
################################################################################
#############################CALL THE FUNCTIONS#################################

#Create directories
create_directories()
'''
#Changing encoding from "cp1252" (a.k.a Windows 1252)to "utf-8-sig"
print('Encoding srt_file(s) to utf8...')
for srt in glob('./srt_files/*.srt'):
    change_encoding(srt)
print('Encoding of %s-files changed' %srt_counter)
print('---------------------------------------------------------------------')

#Extracting information from srt-files to csv
print('Extracting information from srt_file(s) to csv_files')
for file in glob('./srt_files/*.srt'):
    convert_srt_to_csv(file)
print('%s-file(s) converted and saved as csv-files to ./csv' %srt_counter)
print('---------------------------------------------------------------------')

#extract audio (wav) from wmw
for entry in glob('./audio/*.wmv'):
    wmv_to_wav(entry)
print('WMV to WAV convert complete')
print('---------------------------------------------------------------------')

#extract audio (wav) from mp4
for entry in glob('./audio/*.mp4'):
    mp4_to_wav(entry)
print('MP4 to WAV convert complete')
print('---------------------------------------------------------------------')

#Pre-process audio for folder in which wav files are stored
pre_process_audio('./ready_for_slice/')
print('Pre-processing of audio files is complete.')
print('---------------------------------------------------------------------')
'''
#now slice audio according to start- and end-times in csv
print('Slicing audio according to start- and end_times of transcript_csvs...')
for item in glob('./ready_for_slice/*.csv'):
    wav_item = item.replace('.csv','.wav')
    if os.path.exists(wav_item):
        split_files(item, wav_item)
    else:
        next
wav_counter = len(glob('./sliced_audio/' + '*.wav'))
print('Slicing complete. {} files in dir "sliced_audio"'.format(wav_counter))
print('---------------------------------------------------------------------')

#Now create list of filepaths and -size of dir ./sliced_audio
create_DS_csv('./sliced_audio/')
print('DS_csv with Filepaths - and sizes created.')
print('---------------------------------------------------------------------')

#now join all seperate csv files
merge_csv('./ready_for_slice/')
print('Merged csv with all transcriptions created.')
print('---------------------------------------------------------------------')

#merge the csv with transcriptions and the file-csv with paths and sizes
transcript_path = './merged_csv/Full_Transcript.csv'
DS_path = './merged_csv/Filepath_Filesize.csv'
merge_transcripts_and_wav_files(transcript_path, DS_path)
print('Final DS csv generated.')
print('---------------------------------------------------------------------')

#clean the data of unwanted characters
final_csv_path = 'DS_training_final.csv'
clean_unwanted_characters(final_csv_path)
print('Unwanted characters cleaned.')
print('---------------------------------------------------------------------')

#write transcript to text-file for language model
df_text = pd.read_csv('./merged_csv/DS_training_final_cleaned.csv')
df_text['transcript'].to_csv('./final_csv/txt_for_lm.txt', header=None, index=None, mode='a')

#Now split the data into three subsets
to_split_path = 'DS_training_final_cleaned.csv'
split_dataset(to_split_path)
print('Datasplit completed.')

print('********************************************** FINISHED ************************************************')
print('The preprocessing of wmv or mp4 files and their corresponding srt files is completed')
print('Final processed audio is in ./sliced_audio and final csv-files in ./final_csv')
print('******************************************* AUDIO METRICS **********************************************')
if os.path.isdir('./merged_csv/') is True and os.path.isdir('./final_csv/') is True:
    audio_metrics()
print('******************************************* Execution Time *********************************************')
#evaluate the scripts execution time
end_time = time.time()
exec_time = str(datetime.timedelta(seconds=end_time-start_time))

print('The script took {} to run'.format(exec_time))
print('********************************************************************************************************')


'''
Sources:
 - Downsampling wav-files: https://stackoverflow.com/questions/30619740/python-downsampling-wav-audio-file
 - Converting to 16-bit files: https://stackoverflow.com/questions/44812553/how-to-convert-a-24-bit-wav-file-to-16-or-32-bit-files-in-python3
 - Extract audio (wav) from wmv or mp4: https://zulko.github.io/moviepy/
 - Extract audio (wav) from wmv or mp4: https://medium.com/@steadylearner/how-to-extract-audio-from-the-video-with-python-aea325f434b6
 - Dataset-split: https://stackoverflow.com/questions/38250710/how-to-split-data-into-3-sets-train-validation-and-test

Further information:
 - README.md (https://github.com/tobiasrordorf/SRT-to-CSV-and-audio-split)
'''
