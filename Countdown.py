from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import main

class CountdownApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Countdown will be displayed here")
        self.layout.add_widget(self.label)

        # Start countdown when the app is built
        self.countdown(10)

        return self.layout

    def countdown(self, seconds):
        # Schedule the update_countdown method every second
        Clock.schedule_interval(self.update_countdown, 1)
        self.seconds_left = seconds

    def update_countdown(self, dt):
        if self.seconds_left > 0:
            self.label.text = f"Time remaining: {self.seconds_left} seconds"
            self.seconds_left -= 1
        else:
            self.label.text = "Countdown complete!"
            # Stop the scheduled updates when countdown is complete
            Clock.unschedule(self.update_countdown)

# Currently this file is meant to be the file that contains the countdown functions for the main page 
# you can try to adjust the variables here to see what you can do sofie just make sure you document your changes  with a comment 
