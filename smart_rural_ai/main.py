from coordinator import CoordinatorAgent

bot = CoordinatorAgent()

print("Smart Rural AI Started (type exit to stop)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = bot.handle(user_input)
    print("\nAI:", response, "\n")