# Split audio according to information in srt-file.

To be able to train the speech-recognition engine <a href='https://github.com/mozilla/DeepSpeech'> DeepSpeech</a>, audio-files should not be longer than 10s.
Therefore, this repo offers the possibility to easily split audio files based on the subtitle-info in srt-files and prepare corresponding transcript files.


**Table of Contents**

- [Prerequisites](#prerequisites)
- [Walk-through](#walk-through)


## Prerequisites

* [Python 3.6](https://www.python.org/)
* [librosa](https://librosa.github.io/librosa/)
* [SoundFile](https://pypi.org/project/SoundFile/)
* [pydub](https://pypi.org/project/pydub/)
* [moviepy](https://zulko.github.io/moviepy/)

FYI: the script "convert_srt_to_csv.py" is meant to be used on srt files with encoding "cp1252" (a.k.a Windows 1252). The reason for this is that in order to keep characters such as "ä", the files have to be encoded to "utf8"


## Walk-through

<b>This section will explain what the modules and script do in order to provide a deeper understanding of the individual steps and facilitate modification</b>

FYI: the script "convert_srt_to_csv.py" is meant to be used on srt files with encoding "cp1252" (a.k.a Windows 1252). The reason for this is that in order to keep characters such as "ä", the files have to be encoded to "utf8". If your files are alread in "utf8", then deactive the module "change_encoding"

<b>First:</b> Create a folder called "srt_files" where you store your srt_files and a folder "audio" where you store your audio-files (wmv or mp4).

### Modules
<p><b>- change_encoding: </b>The encoding of srt-files is changed from cp1252 to utf-8.</p>
<p><b>- convert_srt_to_csv: </b>Start time, end-time and subtitle are extracted from the srt-files and stored in a csv. In preparation for audio-splitting, a column id is generated from the filename with the addition of a unique number.</p>
<p><b>- wmv_to_wav & mp4_to_wav: </b>Extraction of audio from wmv or mp4 files.</p>
<p><b>- pre_process_audio: </b>Audio is processed to meet DeepSpeechs requirements of sample-rate 16kHz and bit-rate 16.</p>
<p><b>- split_files: </b>The audio files are splitted according to the start- and end-times in the csv files. The splitted audio-files are named after the id given in the transcripts.</p>
<p><b>- create_DS_csv: </b>This module creates a csv with filepaths and filesizes of all processed audio files. </p>
<p><b>- merge_csv: </b>Merge_csv joins all seperate csv-files.</p>
<p><b>- merge_transcripts_and_wav_files: </b>This module matches the transcripts to the available audio files.</p>
<p><b>- clean_unwanted_characters: </b>Unwanted characters are removed.</p>
<p><b>- split_dataset: </b>The final transcripts are splitted into train, test, and dev files and stored in './final_csv'. (train: 75%, test: 15%, dev: 10%)</p>
