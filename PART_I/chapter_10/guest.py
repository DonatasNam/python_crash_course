class Guest:
    def __init__(self):
        pass

    def get_name(self):
        print("Hello plese enter your name:")
        self.name = input()

    def save_name(self):
        try:
            self.file = open("guest.txt", 'x')
        except:
            self.file = open("guest.txt", 'a')
        self.file.write(f'{self.name}\n')
        

guest = Guest()

guest.get_name()
guest.save_name()