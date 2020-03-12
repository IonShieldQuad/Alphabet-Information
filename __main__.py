
import default_alphabets as da
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
kivy.require('1.11.1')

Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '400')

file_path = "alphabet.txt"
limit = 256

alphabet = None


class InfoWidget(Widget):
    def read_file_button(self):
        try:
            out = read_file(file_path)
            print("File:\r\n")
            print(out)
            self.ids.out1.text = "{}".format(len(out))
        except FileNotFoundError:
            print("File {} not found\r\n".format(file_path))
        return

    def display_alphabet_info(self, name):
        out = self.ids.out1
        if alphabet is None:
            out.text = "No alphabet \r\nloaded"
        else:
            out.text = "Alphabet: \r\n {} \r\nCount: {}".format(name, len(alphabet))


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
    try:
        print("File:\r\n")
        print(read_file(file_path))
    except FileNotFoundError:
        print("File {} not found\r\n".format(file_path))

    InfoApp().run()
