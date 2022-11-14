from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from main import PongApp


# /////////////////////starting window//////////////////////


# view of the window when popup in the beginning
Builder.load_string('''
<ConfirmPopup>:
    cols:1
	Label:
		text: root.text
	GridLayout:
		cols: 2
		size_hint_y: None
		height: '44sp'
		Button:
			text: 'Yes'
			on_release: root.dispatch('on_answer','yes')
		Button:
			text: 'No'
			on_release: root.dispatch('on_answer', 'no')
''')




# using this class building popup window
# and check the user answers
class PopupWindow(App):


    # using this build method we build the window and
    # return the content of the window
    def build(self):
        content = ConfirmPopup(text='Do you want to play this PONG game ?')
        content.bind(on_answer=self._on_answer)
        self.popup = Popup(title="PONG GAME",
                           content=content,
                           size_hint=(None, None),
                           size=(300, 300),
                           auto_dismiss=False)
        self.popup.open()


    # using this _on_answer method get the action according
    # to the user input(if a user says "yes" then start the game and
    # if user says "no" then not start game and show a blank window)
    def _on_answer(self, instance, answer):
        print("USER ANSWER: ", repr(answer))
        if answer == "yes":
            PopupWindow().stop()
            self.popup.dismiss()
            PongApp().run()
        elif answer == "no":
            self.popup.dismiss()

        self.popup.dismiss()
        

class ConfirmPopup(GridLayout):
    text = StringProperty()

    def __init__(self, **kwargs):
        self.register_event_type('on_answer')
        super(ConfirmPopup, self).__init__(**kwargs)

    def on_answer(self, *args):
        pass

 # this method is used to execute programme code only
 # if the file was run directly, and not imported.
if __name__ == '__main__':
    PopupWindow().run()

