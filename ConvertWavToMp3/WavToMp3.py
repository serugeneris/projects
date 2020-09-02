from os import path
from pydub import AudioSegment

# files                                                                         
src = r"C:\Users\User\Desktop\file.wav"
dst = r"C:\Users\user\Desktop\file.mp3"

# convert wav to mp3

sound = AudioSegment.from_wav(src)
sound.export(dst, format="mp3")

print("All done!")
