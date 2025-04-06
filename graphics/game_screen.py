
# General imports
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen

# Load the kivy file describing the screen
Builder.load_file("graphics/game_screen.kv")

# Screen class (details in the kivy file)
class GameScreen(Screen):
    pass