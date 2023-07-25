
#10-1 to 10-5
class Guest:
    def __init__(self):
        pass

    def get_name(self):
        print("Hello plese enter your name:")
        self.name = input()
        return self.name

    def save_name(self):
        try:
            self.file = open("guest.txt", 'x')
        except:
            self.file = open("guest.txt", 'a')
        self.file.write(f'{self.name}\n')
        

guest = Guest()


while True:
    print("enter 'q' to quit")
    user_input = guest.get_name()
    if user_input == "q":
        break
    guest.save_name()
