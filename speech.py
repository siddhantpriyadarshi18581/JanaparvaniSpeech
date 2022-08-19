import speech_recognition as sr
import os
from googletrans import Translator
from gtts import gTTS

translator = Translator()
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
mic = sr.Microphone()

to_lang = input("Enter the destination language")
choice = input("Input Format (Voice = v, Text = t, Image= i): ")


def voice_():
    with mic as source:
        print('Say something')
        recognizer.adjust_for_ambient_noise(source)
        print('Ready to record\n')
        audio = recognizer.listen(source)
        print('Audio captured\n')
        try:
            text = recognizer.recognize_google(audio, language='en')
            return text

        except sr.UnknownValueError:
            print('Please say it again\n')
        except sr.RequestError:
            print('Speech service down\n')

def text_():
    text = input("Enter the text you want to translate")
    return text


def output_type(x):
    ch = input("Output : (Press 'vo' for voice and 'tx' for text) : ")
    if (ch == 'vo'):
        myobj = gTTS(text=x, lang=to_lang, slow=False)
        myobj.save("output.mp3")
        os.system("start output.mp3")
    else:
        print(x)


def translation_lang(text):
    translation = translator.translate(text, dest=to_lang)

    x = translation.text
    output_type(x)


if (choice == 'v'):
    # voice_()
    translation_lang(voice_())


elif (choice == 't'):


    translation_lang(text_())


else:
    print("hi")
