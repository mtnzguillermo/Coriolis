
# General imports
import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager

# Internal imports
# It is necessary to import all classes mentioned in "graphics/main.mv"
from graphics.intro_screen import IntroScreen
from graphics.game_screen import GameScreen

# Root class defined in "graphics/main.mv"
class Manager(ScreenManager):
    pass

# Main app class, returning the kv file of the root class Manager
class Coriolis(App):
    def build(self):
        return Builder.load_file("graphics/main.kv")

if __name__ == '__main__':
    Coriolis().run()