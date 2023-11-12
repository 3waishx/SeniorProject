import speech_recognition  as sr


# speech recongnizer 
r = sr.Recognizer()
print("[+] speech recongnizer")

# microphone
mic = sr.Microphone()
print("[+] Microphone")

# capturing microphone input
print("[+] mic as source")
with mic as source:
    print("[+] Listening")
    audio = r.listen(source)

