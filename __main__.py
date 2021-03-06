
import default_alphabets as da
import kivy
import math
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
kivy.require('1.11.1')

Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '400')

file_path = "alphabet.txt"
limit = 256

alphabet = {}


class InfoWidget(Widget):
    def read_file_button(self):
        try:
            out = read_file(file_path)
            global alphabet
            alphabet = {}
            for item in out:
                alphabet[item] = 1 / len(out)
            self.display_alphabet_info("Custom")
        except FileNotFoundError:
            self.ids.out1.text = "File {} not found\r\n".format(file_path)
        return

    def russian_button(self):
        global alphabet
        alphabet = da.get_alphabet_russian()
        self.display_alphabet_info("Russian")
        return

    def english_button(self):
        global alphabet
        alphabet = da.get_alphabet_english()
        self.display_alphabet_info("English")
        return

    def english_weighted_button(self):
        global alphabet
        alphabet = da.get_alphabet_english_weighted()
        self.display_alphabet_info("English\r\n(weighted)")
        return

    def russian_weighted_button(self):
        global alphabet
        alphabet = da.get_alphabet_russian_weighted()
        self.display_alphabet_info("Russian\r\n(weighted)")
        return

    def display_alphabet_info(self, name):
        out = self.ids.out1
        if alphabet is None:
            out.text = "No alphabet \r\nloaded"
        else:
            out.text = "Alphabet: \r\n{}\r\nSymbols: {}".format(name, len(alphabet))
        return

    def analyze_button(self):
        global alphabet
        if alphabet is None:
            return
        message = self.ids.text_input.text
        info = 0
        for char in message:
            if char in alphabet:
                freq = alphabet[char]
                info += -math.log2(freq)
        self.display_message_info(len(message), info)
        return

    def display_message_info(self, msg_len, value):
        out = self.ids.out2
        out.text = "Message length: {} \r\nInformation: {} bits".format(msg_len, value)
        return


class InfoApp(App):
    def build(self):
        return InfoWidget()


def read_file(uri):
    out = []
    file = open(uri, "r")
    for line in file:
        line = line.strip('\n')
        if len(line) == 0:
            out.append(" ")
        else:
            out.append(line)
    file.close()
    return out


if __name__ == "__main__":
    InfoApp().run()
