import kivy
import kivy.app
import smtplib
import kivy.uix.textinput,kivy.uix.boxlayout,kivy.uix.label,kivy.uix.button

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
class  smtp_app(kivy.app.App):
    def build(self):
        self.label = kivy.uix.label.Label(text="Simple smtp messenger (works only when less secure apps turned on!)")
        self.textInput1=kivy.uix.textinput.TextInput(text="enter the username")
        self.textInput2 = kivy.uix.textinput.TextInput(text="enter the password")
        self.textInput3 = kivy.uix.textinput.TextInput(text="enter the message")
        self.textInput4 = kivy.uix.textinput.TextInput(text="enter the target mail-id")
        self.button=kivy.uix.button.Button(text="send message")
        self.button.bind(on_press=self.send_mail)
        self.boxlayout=kivy.uix.boxlayout.BoxLayout(orientation="vertical")
        self.boxlayout.add_widget(self.label)
        self.boxlayout.add_widget(self.textInput1)
        self.boxlayout.add_widget(self.textInput2)
        self.boxlayout.add_widget(self.textInput3)
        self.boxlayout.add_widget(self.textInput4)
        self.boxlayout.add_widget(self.button)
        return self.boxlayout
    def send_mail(self,btn):
        username = self.textInput1.text
        password = self.textInput2.text
        server.login(username, password)
        msg=self.textInput3.text
        target=self.textInput4.text
        server.sendmail(username,target,msg)
if __name__=="__main__":

    S=smtp_app()
    S.run()


