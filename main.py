# QDB
# Bishneet Singh

# ------------------ Importing Libraries ------------------ #
import imp
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


# ------------------ Importing Functions ------------------ #
from database import create_table, insert_data, retrieve_data


# ------------------ Main Functions ------------------ #

class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


class MainWidget(Widget):
    pass


class mainApp(App):
    def build(self):
        kv = Builder.load_file('main.kv')
        return kv

if __name__ == '__main__':
    mainApp().run()