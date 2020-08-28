import sys
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
r = sr.Recognizer()

def printvoices():
    voices = engine.getProperty('voices')
    print(len(voices))
    for voice in voices:
        print("Voice:")
        print(" - ID: %s" % voice.id)
        print(" - Name: %s" % voice.name)
        print(" - Languages: %s" % voice.languages)
        print(" - Gender: %s" % voice.gender)
        print(" - Age: %s" % voice.age)
def TextToSpeech(text):
    engine.say(text)
    engine.runAndWait()
def SpeechToText():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio1 = r.listen(source)
            MyText = r.recognize_google(audio1)
            print(MyText)
    except:
        print("Someexception occurred")
        pass
def main(argv):
    #printvoices()
    for arg in argv:
        TextToSpeech(arg)
    SpeechToText()

if __name__=='__main__':
    main(sys.argv[1:])
