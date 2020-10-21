# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  

pets = {}

while True:
    key = input("Enter the name of a pet. ")
    key = key.strip()
    value = input(f"What kind of pet is/was {key}?")
    value = value.strip()
    pets[key] = value
    again = input("Enter another? Press any key to keep continue adding pets. Type 'q' to quit. ")
    if again == 'q':
        break

print(pets)

