from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock, mainthread
import speech_recognition as sr
from kivy.core.window import Window

Window.size = (400, 600)
Window.clearcolor = (120/255, 140/255, 250/255, 1)

class Principal(Screen):
    def Btnmic(self):
        self.ids.lblMessage.text = "Say something!"
        Clock.schedule_once(lambda d: self.GetAudio(), 0)

    def GetAudio(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        self.audio = audio
        try:
            self.ids.lblMessage.text = r.recognize_google(audio, language='en_in')
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


class testsapkApp(App):

    def build(self):
        sm = ScreenManager()
        self.sm = sm
        sm.add_widget(Principal(name='Principal'))
        return sm

    def on_pause(self):
        return False


main = testsapkApp()
main.run()
