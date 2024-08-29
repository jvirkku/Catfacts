import requests


def get_facts():
    factlist = []

    for i in range(1,user_input+1): #for loop to create a list containing 6 facts
        response = requests.get(f'https://meowfacts.herokuapp.com/?count{i}')
        fact = response.json()['data'][0]
        factlist.append(fact)
    return factlist

def cat_facts():
    factlist = get_facts()
    
    for i in range(user_input):
        print(f"Fact no {i+1}: {factlist[i]}")
        print("")
    print("I hope you learned something new today!")
    print("")

print("")
print("Welcome to the cat fact generator.")
while True:
    try:
        user_input = int(input("How many cat facts would you like to know today? "))
        if user_input > 0 and user_input <= 15:
            print("")
            cat_facts()
            break
        elif user_input == 0:
            print("Well okay then...")
            break
        else:
            print("Thats a bit too much...")
    except ValueError:
        print("Please enter a valid number")









