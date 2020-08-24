
lucky_numbers = [4, 8, 15, 17, 23, 42]
players = ["Kevin", "Stacey", "Jim", "Daniel", "Mike"]

is_login_success = False
while True:
    name = input("Please enter your name or enter `Exit` to exit game\n> ").capitalize().strip()

    if name == "Exit":
        is_login_success = False
        print("Bye bye! Hope to see you soon.")
        break

    elif name in players:
        is_login_success = True
        print(f"Ok {name}, move on..")
        break

    else:
        print("Uh oh, you are not on the players list!")


if is_login_success:

    input_numbers = list(map(int, input("Enter 6 lucky numbers: ").split()))
if input_numbers == lucky_numbers:
    print(f"Congratulations {name} YOU WON!")
else:
    print("Sorry. You guessed wrong!")
