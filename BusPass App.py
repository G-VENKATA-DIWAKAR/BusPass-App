#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install kivy


# In[1]:


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class BusPassApp(App):
    def build(self):
        self.username_input = TextInput(hint_text="Username", multiline=False)
        self.email_input = TextInput(hint_text="Email", multiline=False)
        self.pass_type_input = TextInput(hint_text="Pass Type (e.g., daily, weekly, monthly)", multiline=False)
        self.validity_input = TextInput(hint_text="Validity Duration (e.g., 30 days)", multiline=False)

        self.register_button = Button(text="Register", on_press=self.register)
        self.apply_pass_button = Button(text="Apply for Bus Pass", on_press=self.apply_for_pass)

        self.feedback_label = Label(size_hint_y=None, height=40)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.username_input)
        layout.add_widget(self.email_input)
        layout.add_widget(self.pass_type_input)
        layout.add_widget(self.validity_input)
        layout.add_widget(self.register_button)
        layout.add_widget(self.apply_pass_button)
        layout.add_widget(self.feedback_label)

        return layout

    def register(self, instance):
        username = self.username_input.text.strip()
        email = self.email_input.text.strip()

        if username and email:
            
            print(f"Registered user: {username}, Email: {email}")
            self.feedback_label.text = "Registration successful!"
            self.clear_inputs()
        else:
            self.feedback_label.text = "Please enter both username and email."

    def apply_for_pass(self, instance):
        pass_type = self.pass_type_input.text.strip()
        validity = self.validity_input.text.strip()

        if pass_type and validity:
            
            print(f"Pass Type: {pass_type}, Validity: {validity}")
            self.feedback_label.text = "Bus pass application successful!"
            self.clear_inputs()
        else:
            self.feedback_label.text = "Please enter both pass type and validity duration."

    def clear_inputs(self):
        self.username_input.text = ""
        self.email_input.text = ""
        self.pass_type_input.text = ""
        self.validity_input.text = ""

if __name__ == '__main__':
    BusPassApp().run()

