# import speech_recognition as h
# my_mic = h.Microphone(device_index=1)
# recognizer = h.Recognizer()
# print("say now...")
# with my_mic as new:
#     audio = recognizer.listen(new)
#     print(recognizer.recognize_sphinx(audio))



import speech_recognition as sr
import sphinx
import pocketsphinx

r = sr.Recognizer()
with sr.Microphone() as source:                # use the default microphone as the audio source
    audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

try:
    print("You said " + r.recognize_sphinx(audio))    # recognize speech using Google Speech Recognition
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")