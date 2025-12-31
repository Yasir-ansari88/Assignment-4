user_input = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")

additional_input = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(additional_input + "\n")

print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    line = file.read()
    print(line)