sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

# for word in sentence.split() :
#     print(word)

result = {
    letters : len(letters) for letters in sentence.split()
}

print(result)