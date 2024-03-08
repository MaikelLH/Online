#Let's start a coffee shop together!! We're going to built a coffee shop using some new python programming concepts!!

#Let's built robot Barista!!

print("Hello, welcome to NetworkChuck Coffee!!!!!!!")

#print("What's your name?") "no se va a usar porque se va a solicitar desde el input"

name = input("What's your name?\n")

if name == "Ben":
    print("You´re not welcome here Evil Ben!! Get Out!!")
    exit()
else: 
    print("Hello " + name + ", thank you so much for coming in today.\n")

# con el + contatenamos y tenemos control de los espacios entre oraciones

menu = "Black Coffee, Espreso, Latte, Cappucino"

print(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu)

order = input()

price = 8

quantity = (input("How many " + order + " do you want?\n"))

total = price * int(quantity)

print("Sounds good " + name + ", we'll have your " + quantity + " " + order + " ready for you in a moment.\n")

print("Thank you. Your total is: $" + str(total) + "\n")



print(type(menu))
print(type(quantity))
print(type(quantity))
print(type(total))

