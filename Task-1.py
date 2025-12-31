try:
    with open("sample.txt", "r") as file:
       Line1=file.readline()
       print(Line1)
       Line2=file.readline()
       print(Line2)
       Line3=file.readline()
       print(Line3)

except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")

