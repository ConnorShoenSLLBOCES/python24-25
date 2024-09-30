prompt = "Tell me something, and I'll repeat it back to you: "
prompt += "\n Enter 'quit' to end the program. "

message = ""
while message != "quit":
    message = input(prompt)
    print(message)