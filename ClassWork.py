countries = {'France': 'Paris', 'Japan': 'Tokyo', 'Chile': 'Santiago'}
command_list = {'add', 'search', 'delete', 'replace'}

while True:
    user_input = input("Wold you like to add, search, delete, replace or quit?\t")
    if user_input.lower() == 'quit':
        print('Thanks for using.')
        break
    if user_input not in command_list:
        print("Provide valid command")
        continue
    if user_input == 'add':
        country = input("Enter country add:\t")
        if country not in countries.keys():
            capital = input("Enter capital\t")
            countries[country] = capital

    elif user_input == 'search':
        country = input("Enter country search: \t")
        print(countries.get(country, "No such country\t"))

    elif user_input == 'delete':
        country = input("Enter country to delete: \t")
        countries.pop(country, "No such country")

    else:
        country = input("Enter country to replace")
        if country in countries.keys():
            del countries[country]
            new_country = input("Enter new country: \t")
            countries[new_country] = input("Enter capital: \t")


print("\r\n")

for key in countries:
    print(f"{key}:{countries[key]}")

key_list = list(sorted(countries.keys()))

