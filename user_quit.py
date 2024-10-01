prompt = "Tell me something, and I'll repeat it back to you: "
prompt += "\n Enter 'quit' to end the program. "

# message = ""
# while message != "quit":
#     message = input (prompt)
#     print (message)

print("\n\n\nWhile loop using a flag")
print("-----------------------------")

active = True #programming flag

while active:
    message = input (prompt)
    if message == "quit":
        active = False
    else:
        print (message)