from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
import speech_recognition as sr
from kivy.core.window import Window
from googletrans import Translator
import languages
import kivy.resources
import datetime
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

date = datetime.datetime.now()
dtime = date.strftime("%d-%B-%Y:%X")
ofile = open('speechtotextdatas.txt', 'a')

kivy.resources.resource_add_path('C:\Windows\Fonts')

translator = Translator()
translator = Translator(service_urls=['translate.googleapis.com'])
Window.size = (400, 650)
class ScreenOne(Screen):
    pass
class ScreenTwo(Screen):
    pass
class ToolScreen(Screen):


    def Btnmic(self):
        self.ids.lblMessage.text = "Say something!"
        Clock.schedule_once(lambda d: self.GetAudio(), 0)

    def callspeak(self):
        name = self.ids.enter_speech.text
        engine.say(name)
        engine.runAndWait()
        pass

    def tobestop(self):
        ofile.close()

    def GetAudio(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        self.audio = audio
        try:
            self.ids.lblMessage.text = r.recognize_google(audio, language='en_in')
            a = r.recognize_google(audio, language='en_in')
            print(type(a))
            print("{} \t {} \n".format(a, dtime))
            ofile.write("{} \t {} \n".format(a, dtime))

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    def spinner_clicked(self,value):
        a = value
        print(a)
        name = self.ids.input_enter.text
        dictvalue = list(languages.alllang.values())
        dictkey = list(languages.alllang.keys())
        position = dictvalue.index(a)
        print(dictkey[position])
        translation = translator.translate(name, dest=dictkey[position])
        self.ids.output_enter.text = '{}'.format(translation.text)
        print(translation.text)

class SpeakWell(MDApp):

    def build(self):
        return Builder.load_file('kgkv.kv')


main = SpeakWell()
main.run()