# SRT-to-CSV-and-audio-split
Split long audio files based on subtitle-info in SRT File (Transcript saved in CSV)


FYI: the script "convert_srt_to_csv.py" is meant to be used on srt files with encoding "cp1252" (a.k.a Windows 1252). The reason for this is that in order to keep characters such as "ä", the files have to be encoded to "utf8"

First: create a folder called "srt_files" where you store your srt_files.

