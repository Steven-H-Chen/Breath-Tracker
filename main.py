#from typing import Self
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.graphics import Ellipse, Color
import time

class BreathTrackerApp(App):

    def build(self): #self is a reference to the class name in a way its like saying BreathTrackerApp but instead as self
        layout = BoxLayout(orientation='vertical', padding=100, spacing= 100)

        self.breath_label = Label(text='Breathe in and out...', font_size=30)
        layout.add_widget(self.breath_label)

        self.slider = Slider(min=0, max=10, value=5)
        layout.add_widget(self.slider)

        container = Widget()#calling in a container widget
        with container.canvas:
            #self.circle_color = Color(1, 0, 0, 1)  # Initial color (red)
            self.circle = Ellipse(pos=(473, 250), size=(50, 50))
        #container.bind(on_touch_down=self.animate_circle)
        layout.add_widget(container)

        start_button = Button(text='Start Breathing', background_color=(0, 1, 0, 1))
        start_button.bind(on_press=self.start_breathing)
        start_button.bind(on_press=self.animate_circle)
        layout.add_widget(start_button)        

        return layout
    
    def animate_circle(self, instance ):#touch
        # Animate the circle's position, size, and color
        bduration = int (self.slider.value)
        if bduration >0:
            animate = Animation(size=(100, 100),duration=bduration) #+ Animation(background_color=(0, 1, 0, 1))
            animate.start(self.circle)
        elif bduration >0:
            animate = Animation(size=(100, 100),duration=bduration) #+ Animation(background_color=(0, 1, 0, 1))
            animate.start(self.circle)

        #animate.stop(self.Ellipse)


        #pos=(touch.x - 25, touch.y - 25),

    def start_breathing(self, instance): # instance in this situation is reference to the trigger method basically referencing on press from the button 
        breath_duration = int(self.slider.value)
        self.breath_label.text = f'Breathe in  {breath_duration} seconds...'

        # Schedule countdown for breath in phase
        Clock.schedule_interval(self.update_countdown_in, 1)
        self.countdown_in = breath_duration

    def update_countdown_in(self, dt):
        if self.countdown_in > 0:
            self.breath_label.text = f' Breathin: Hold for {self.countdown_in} seconds...'
            self.countdown_in -= 1
            
        else:
            self.breath_label.text = 'Breathe out...'
            Clock.unschedule(self.update_countdown_in)
            
            # Schedule countdown for breath out phase
            breath_duration = int(self.slider.value)
            Clock.schedule_interval(self.update_countdown_out, 1)
            self.countdown_out = breath_duration

    def update_countdown_out(self, dt):
        if self.countdown_out > 0:
            self.breath_label.text = f'Breathe out: Hold for {self.countdown_out} seconds...'
            self.countdown_out -= 1
        else:
            self.breath_label.text = 'Done...'
            Clock.unschedule(self.update_countdown_out)
    

if __name__ == '__main__':
    BreathTrackerApp().run()
