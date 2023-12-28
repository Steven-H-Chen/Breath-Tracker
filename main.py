#from typing import Self
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.clock import Clock
import time
import Countdown

class BreathTrackerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)

        self.breath_label = Label(text='Breathe in and out...', font_size=20)
        layout.add_widget(self.breath_label)

        self.slider = Slider(min=0, max=10, value=5)
        layout.add_widget(self.slider)

        start_button = Button(text='Start Breathing', on_press=self.start_breathing)
        layout.add_widget(start_button)

        #stop_button = Button(text='Stop Breathing', on_press=self.stop_breathing)
        #layout.add_widget(stop_button)

        return layout

    def start_breathing(self, instance):
        breath_duration = self.slider.value
        self.breath_label.text = f'Breathe in and hold for {breath_duration} seconds...'
# here i am trying to make a function that would pass the timer command from the slider into the countdown file so that the command 
# so that the coundown file makes the countdown occur and displays it back out here each time a count down has been made until its 
# finished, you can try to see what you can do here to adjust it just make sure to comment what changes you made 
        #if 0.0 <= self.slider.value <1.0 :
            #try:
                #seconds = self.slider.value
                #self.count_seconds(seconds)
            #except ValueError:
                #print("Please reselect slider seconds")

            
        # Add logic for tracking breath duration or any other functionality

    #def stop_breathing(self, instance):
        #breath_duration = self.slider.value
        #self.breath_label.text = f'Breathe out and hold for {breath_duration} seconds...'


    #class MyWidget(Widget):
        #def __init__(self, **kwargs):
            #super(MyWidget, self).__init__(**kwargs)
            #self.draw_my_stuff()

            #self.bind(pos=self.draw_my_stuff)
            #self.bind(size=self.draw_my_stuff)

        #def draw_my_stuff(self, *args):
            #self.canvas.clear()

            #with self.canvas:
                #self.rect = Rectangle(pos=self.pos, size=self.size)

        #return Self
if __name__ == '__main__':
    BreathTrackerApp().run()
