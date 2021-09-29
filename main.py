from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

Builder.load_file('main.kv')

Window.size = (500, 700)

class MyLayout(Widget):
    
    def clear(self):
        self.textinput.text = "0"

    def delete(self):
        string = self.textinput.text
        self.textinput.text = string[0:-1]

    def answer(self):
        if ("+" in self.textinput.text and "." in self.textinput.text):
            string = self.textinput.text
            place = string.find("+")
            firststring = string[0:place]
            secondstring = string[place+1:]
            firstnum = float(firststring)
            secondnum = float(secondstring)
            answer = firstnum + secondnum
            self.textinput.text = str(answer)
        elif ("+" in self.textinput.text):
            string = self.textinput.text
            place = string.find("+")
            firststring = string[0:place]
            secondstring = string[place+1:]
            firstnum = int(firststring)
            secondnum = int(secondstring)
            answer = firstnum + secondnum
            self.textinput.text = str(answer)
        elif ("-" in self.textinput.text and "." in self.textinput.text):
            string = self.textinput.text
            place = string.find("-")
            firststring = string[0:place]
            secondstring = string[place+1:]
            firstnum = float(firststring)
            secondnum = float(secondstring)
            answer = firstnum - secondnum
            self.textinput.text = str(answer)
        elif ("-" in self.textinput.text):
            string = self.textinput.text
            place = string.find("-")
            firststring = string[0:place]
            secondstring = string[place+1:]
            firstnum = int(firststring)
            secondnum = int(secondstring)
            answer = firstnum - secondnum
            self.textinput.text = str(answer)
        elif ("x" in self.textinput.text and "." in self.textinput.text):
            string = self.textinput.text
            place = string.find("x")
            firststring = string[0:place]
            secondstring = string[place+1:]
            firstnum = float(firststring)
            secondnum = float(secondstring)
            answer = firstnum * secondnum
            self.textinput.text = str(answer)
        elif ("x" in self.textinput.text):
            string = self.textinput.text
            place = string.find("x")
            firststring = string[0:place]
            secondstring = string[place+1:]
            firstnum = int(firststring)
            secondnum = int(secondstring)
            answer = firstnum * secondnum
            self.textinput.text = str(answer)
        elif ("/" in self.textinput.text and "." in self.textinput.text):
            string = self.textinput.text
            place = string.find("/")
            firststring = string[0:place]
            secondstring = string[place+1:]
            firstnum = float(firststring)
            secondnum = float(secondstring)
            if secondnum == 0 or 0. or 0.0 or 0.00 or 0.000:
                self.textinput.text = "ERROR"
            else:
                answer = firstnum / secondnum
                self.textinput.text = str(answer)
        elif ("/" in self.textinput.text):
            string = self.textinput.text
            place = string.find("/")
            firststring = string[0:place]
            secondstring = string[place+1:]
            firstnum = int(firststring)
            secondnum = int(secondstring)
            if secondnum == 0:
                self.textinput.text = "ERROR"
            else:
                answer = firstnum / secondnum
                self.textinput.text = str(answer)
        else:
            self.textinput.text = "ERROR"


    def adddec(self):
        self.textinput.text = self.textinput.text + "."

    def addnums(self):
        self.textinput.text = self.textinput.text + "+"

    def subnums(self):
        self.textinput.text = self.textinput.text + "-"

    def multiplynums(self):
        self.textinput.text = self.textinput.text +"x"

    def dividenums(self):
        self.textinput.text = self.textinput.text +"/"

    def numzero(self):
            self.textinput.text = self.textinput.text + "0"
    def numone(self):
        if self.textinput.text == "0":
            self.textinput.text = "1"
        else:
            self.textinput.text = self.textinput.text + "1"
    def numtwo(self):
        if self.textinput.text == "0":
            self.textinput.text = "2"
        else:
            self.textinput.text = self.textinput.text + "2"
    def numthree(self):
        if self.textinput.text == "0":
            self.textinput.text = "3"
        else:
            self.textinput.text = self.textinput.text + "3"
    def numfour(self):
        if self.textinput.text == "0":
            self.textinput.text = "4"
        else:
            self.textinput.text = self.textinput.text + "4"
    def numfive(self):
        if self.textinput.text == "0":
            self.textinput.text = "5"
        else:
            self.textinput.text = self.textinput.text + "5"
    def numsix(self):
        if self.textinput.text == "0":
            self.textinput.text = "6"
        else:
            self.textinput.text = self.textinput.text + "6"
    def numseven(self):
        if self.textinput.text == "0":
            self.textinput.text = "7"
        else:
            self.textinput.text = self.textinput.text + "7"
    def numeight(self):
        if self.textinput.text == "0":
            self.textinput.text = "8"
        else:
            self.textinput.text = self.textinput.text + "8"
    def numnine(self):
        if self.textinput.text == "0":
            self.textinput.text = "9"
        else:
            self.textinput.text = self.textinput.text + "9"

class CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    CalculatorApp().run()