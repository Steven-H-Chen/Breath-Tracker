from kivy.app import App
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.uix.bubble import Bubble
from main import BreathTrackerApp

class BreathBubble(Widget):
    def breathe(self, duration, *args):
        # Create an Animation to scale the bubble up and down
        anim = Animation( duration=self.BreathTrackerApp.build.slider.value/1) + Animation( duration=self.BreathTrackerApp.build.slider.value/1, background_color=(0, 0, 1, 0))
        animate += Animation (size_hint = (duration))
        anim.repeat = True
        anim.start(self)

        return anim
