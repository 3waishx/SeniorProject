import whisper
from whisper_mic.whisper_mic import WhisperMic

mic = WhisperMic()
result = mic.listen()

print(result)

if 'help' in result:
    print("code red")