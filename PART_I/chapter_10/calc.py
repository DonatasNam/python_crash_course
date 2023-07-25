

def get_num():

    while True:
        print("enter a number:")
        num = input()
        if num == "q":
            break
        try:
            num = int(num)
            break
        except:
            print("Please enter a valid integer")
            pass
    return num

def sum_num(num1,num2):
    return num1 + num2

print("press q to quit")
num1 = get_num()
if isinstance(num1, int) != True:
    print("Exiting...")
    exit()

num2 =get_num()
if isinstance(num2, int) != True:
    print("Exiting...")
    exit()

print(sum_num(num1,num2))