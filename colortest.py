import termcolor

t = termcolor.colored("Hello ", "red")
t+= termcolor.colored("World", "green")
print(t)
print (termcolor.COLORS)
print(format(12, "x2",))