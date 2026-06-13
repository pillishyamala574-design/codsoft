from datetime import datetime
import random

print("=" * 40)
print("      RULE-BASED CHATBOT")
print("=" * 40)

name = input("Enter your name: ")
print(f"Hello, {name}! ")
print("Type 'help' to see available commands.\n")

jokes = [
    "Why did the computer go to the doctor? It had a virus!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the computer cold? It left its Windows open!"
]

while True:
    user = input(f"{name}: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif "how are you" in user:
        print("Bot: I'm doing great! Thanks for asking.")

    elif "your name" in user:
        print("Bot: I am a Rule-Based Chatbot.")

    elif "time" in user:
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    elif "date" in user:
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    elif "joke" in user:
        print("Bot:", random.choice(jokes))

    elif user == "calculator":
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+,-,*,/): ")
            num2 = float(input("Enter second number: "))

            if op == "+":
                print("Result =", num1 + num2)
            elif op == "-":
                print("Result =", num1 - num2)
            elif op == "*":
                print("Result =", num1 * num2)
            elif op == "/":
                print("Result =", num1 / num2)
            else:
                print("Invalid operator!")
        except:
            print("Invalid input!")

    elif user == "help":
        print("\nAvailable Commands:")
        print("hello, hi, hey")
        print("how are you")
        print("your name")
        print("date")
        print("time")
        print("joke")
        print("calculator")
        print("help")
        print("exit\n")

    elif user == "exit":
        print(f"Bot: Goodbye, {name}! Have a nice day. ")
        break

    else:
        print("Bot: Sorry, I don't understand that. Type 'help' for options.")
