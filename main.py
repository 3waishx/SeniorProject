import speech_recognition as sr

red = ['unresponsive', 'dead', 'death']
yellow = ['fever', 'child']
green = ['broken', 'broke']


## Improve mapping so
def mapping(sentence):
    category = ''

    words = sentence.split()
    categories = []
    for word in words:
        if word in red:
            category = 'red'
            categories.append(category)
        
            # add text for red what next when amb is coming
        elif word in yellow:
            category = 'yellow'
            categories.append(category)

            # same comment as above
        elif word in green:
            category = 'green'
            categories.append(category)


    if 'red' in categories:
        category = 'red'
        return category
    
    if 'yellow' in categories and 'red' not in categories:
        category = 'yellow'
        return category

    if 'green' in categories and 'red' not in categories:
             if 'green' in categories and 'yellow' not in categories: 
                category = 'green'
                return category
        



def recognize_speech():
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    print("911 what is your emergency")

    while True:
        # Use the default microphone as the audio source
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        
        # analyzes 
        try:
            # Use Google Web Speech API to recognize the speech
            text = recognizer.recognize_google(audio, language="en-US")
            print("You said:", text)
            # mapping keyword in text
            category = mapping(text)
            print(category)

        except sr.UnknownValueError:
            print("Could you please repeat that")
        except sr.RequestError as e:
            print(f"Error connecting to Google API: {e}")

        

if __name__ == "__main__":
    recognize_speech()

