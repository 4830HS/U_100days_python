#Positional Argument
def greet_with(name,location) :
	print(f"Hello, my name is {name}.")
	print(f"I live in {location}.")
	
greet_with("Alex","nowhere")

#Keyword Argument
def greet_with(name,location) :
	print(f"Hello, my name is {name}.")
	print(f"I live in {location}.")
	
greet_with(name = "Alex",location = "nowhere")
#or
greet_with(location = "nowhere", name = "Alex")