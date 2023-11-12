import speech_recognition as sr

## add more words here 
red = ['unresponsive', 'dead', 'death']
yellow = ['fever', 'child']
green = ['broken', 'broke']


## Dont touch, we barely made it work
def mapping(sentence):
    category = ''

    words = sentence.split()
    categories = []
    for word in words:
        if word in red:
            category = 'red'
            categories.append(category)
        
        elif word in yellow:
            category = 'yellow'
            categories.append(category)

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
        
# displaying information 
def display(category):
    if category == 'red':
        print("AMB ETA 5 MIN")

    if category == 'yellow':
        print("ETA 10 MIN")
    
    if category == 'green' or category == 'None':
        print("Connecting to call center... please wait a minute..")


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
            display(category)

        except sr.UnknownValueError:
            print("Could you please repeat that")
        except sr.RequestError as e:
            print(f"Error connecting to Google API: {e}")

        

if __name__ == "__main__":
    recognize_speech()
