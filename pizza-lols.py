#copyright Alan Thomson asmt3

person = input('Enter your name: ')
print('Hello', person)

while True:
  response = input("I'm meeting Dave and Emma for pizza on Friday. Would you like to come, " + person + "?\n")
  if response == "yes":
    print("great! See you there")
    break
