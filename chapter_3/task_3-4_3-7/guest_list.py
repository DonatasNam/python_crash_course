# task 3-4
invites =["Mathew Mercer","Marisha Ray","Travis Willingham","Laura Bailey"]

invitation_message = "I am inviting you to play DnD and would be gratefull if you would accept"

print(f"\n{invites[0]} {invitation_message}\
    \n{invites[1]} {invitation_message}\
    \n{invites[2]} {invitation_message}\
    \n{invites[3]} {invitation_message}")

#task 3-5
print(f"{invites[2]} cannot make it")

invites.remove(f"{invites[2]}")
invites.append("Sam Reigel")

print(f"\n{invites[0]} {invitation_message}\
    \n{invites[1]} {invitation_message}\
    \n{invites[2]} {invitation_message}\
    \n{invites[3]} {invitation_message}")

#task 3-6

print("I have aquired a bigger table")

invites.insert(0, "Ashley Johnson")
invites.insert(2, "Liam O'Brien")
invites.append("Travis Willingham")

for i in invites:
    print(f"{i} {invitation_message}")