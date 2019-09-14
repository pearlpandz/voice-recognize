import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print('Speak anything: ')
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        f= open("notes.txt","w+")
        f.write(f"{text} \n")
        f.close() 
        print('you said: {}'.format(text))
    except: 
        print('sorry could not recognize your voice')
