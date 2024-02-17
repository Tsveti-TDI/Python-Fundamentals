message_number = int(input())

for i in range(message_number):
    message = int(input())
    if message == 88:
        print("Hello")
    elif message == 86:
        print("How are you?")
    elif message > 88:
        print("Bye.")
    else:
        print("GREAT!")