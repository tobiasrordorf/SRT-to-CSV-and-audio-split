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
<p><b>change_encoding</b></p>
<p><b>convert_srt_to_csv</b></p>
<p><b>wmv_to_wav & mp4_to_wav</b></p>
<p><b>pre_process_audio</b></p>
<p><b>split_files</b></p>
<p><b>create_DS_csv</b></p>
<p><b>merge_csv</b></p>
<p><b>merge_transcripts_and_wav_files</b></p>
<p><b>clean_unwanted_characters</b></p>
<p><b>split_dataset</b></p>
