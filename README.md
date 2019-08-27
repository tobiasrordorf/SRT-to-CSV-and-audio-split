# SRT-to-CSV-and-audio-split

To be able to train DeepSpeech, audio-files should not be longer than 10s.
Therefore, this repo offers the possibility to easily splice audio files and prepare corresponding transcript files.
Split long audio files based on subtitle-info in SRT File (Transcript saved in CSV)

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

<b>First:</b> Create a folder called "srt_files" where you store your srt_files and a folder "audio" where you store your audio-files (wmv or mp4).
