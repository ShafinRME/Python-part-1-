import turtle
name = turtle.textinput("name", "What is your name?")
if name.startswith("mr") or name.startswith("Mr"):
    print("Hello Sir", name)
elif name.startswith("Ms") or name.startswith("ms") or name.startswith("Miss") or name.startswith("miss"):
    print("Hellow Mam", name)
else:
    name = name.capitalize()
    str = "Hi " + name + "! How are you?"
    print(str)
