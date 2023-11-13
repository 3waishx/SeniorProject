import speech_recognition as sr

## small library of keywords for each category 
red = ['cardiac Arrest', 'heart failure', 'stroke','seizure','hemorrhaging','head injury','abdominal injury','chest Injury','septic shock','diabetes Ketoacidosis','dka','anaphylaxis','allergic shock','posioning','drug overdose','severe bleeding','choking','child is choking']
yellow = ['abdominal pain', 'Pneumonia','bells plasy','asthma','Fracture','allergic reaction', 'anexity', 'panic attack','upper respiratory infection','open fracture','bone is sticking out']
green = ['Minor abrasion', 'burns', 'minor fractures','insect bite','foreign body in ear','foreign body in nose','nausea','mild asthma','mild back pain']


## Dont touch, we barely made it work (mapping for the categories that barely worked..)
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
        print("This is a RED case, Ambulance ETA 7 to 9 minutes")

    if category == 'yellow':
        print("This is a YELLOW case, Ambulace ETA up to 10 minutes")
    
    if category == 'green' or category == 'None':
        print("This is a GREEN case, Connecting to call center... please wait a minute..")


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

