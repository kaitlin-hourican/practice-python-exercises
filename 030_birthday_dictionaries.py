birthdays = {
    "Jeff": "01/12/2005",
    "Kathy": "27/02/1980",
    "Emma": "13/07/1876",
    "Rob": "30/10/2025"
}

def birthday_lookup(name):
    formatted_name = name.title()
    
    if formatted_name in birthdays:
        return birthdays[formatted_name]
    return False 

def main():
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for name in birthdays:
        print(name)
    
    person = input("\nWho's birthday do you want to look up? ")
    birthday = birthday_lookup(person)

    if birthday:
        print(f"{person.title()}'s birthday is {birthday}.")
    else:
        print("Person not found.")
          
if __name__ == "__main__":
    main()