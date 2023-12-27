from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider

class BreathTrackerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)

        self.breath_label = Label(text='Breathe in and out...', font_size=20)
        layout.add_widget(self.breath_label)

        self.slider = Slider(min=0, max=10, value=5)
        layout.add_widget(self.slider)

        start_button = Button(text='Start Breathing', on_press=self.start_breathing)
        layout.add_widget(start_button)

        return layout

    def start_breathing(self, instance):
        breath_duration = self.slider.value
        self.breath_label.text = f'Breathe in for {breath_duration} seconds...'
        # Add logic for tracking breath duration or any other functionality

if __name__ == '__main__':
    BreathTrackerApp().run()
