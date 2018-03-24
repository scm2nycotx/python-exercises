#main program
import pickle
def print_menu():
    print(" ")
    print("=" * 40)
    print("Electronic Phone Book for Houston Astros")
    print("=" * 40)
    print("1. List all entries")
    print("2. Add an entry")
    print("3. Remove an entry")
    print("4. Lookup an entry")
    print("5. Save entries")
    print("6. Load saved entries")
    print("7. Quit")
entries = {"Justin" : {"Number" : "713-123-4567", "e-mail" : "justinv@houstonastros.com", "url" : "http://m.astros.mlb.com/roster/35"},
           "Jose" : {"Number" : "713-123-7890", "e-mail" : "Josea@houstonastros.com", "url" : "http://m.astros.mlb.com/roster/27"},
           "George" : {"Number" : "713-123-0123", "e-mail" : "georges@houstonastros.com", "url" : "http://m.astros.mlb.com/roster/4"},
           "Carlos" : {"Number" : "713-123-1234", "e-mail" : "carlosc@houstonastros.com", "url" : "http://m.astros.mlb.com/roster/1"}
}
menu_choice = 0
print_menu()

#individual choices
def print_nested(entries, nesting = -2):
	if type(entries) == dict:
		print('')
		nesting += 4
		for k in entries:
			print(nesting * ' ', end='')
			print(k, end=':')
			print_nested(entries[k],nesting)
	else:
		print(entries)
		
def add_contact():
    k0 = input("Name: ")
    v1 = input("Number: ")
    v2 = input("e-mail: ")
    v3 = input("url: ")
    new_contact = {"Number" : v1, "e-mail" : v2, "url" : v3}
    entries[k0] = new_contact
    print("{} has been added to phonebook".format(k0))
    
def remove_contact():
    name = input("Name: ")
    if name in entries:
        del entries[name]
        print("{} has been deleted from phonebook".format(name))
    else:
        print("{} was not found".format(name))
        
def lookup_contact():
    name = input("Name: ")
    if name in entries:
        print("The entry for {} is: ".format(name), entries[name])
    else:
        print("{} was not found".format(name))
        
def save_contact():
    myfile = open('phonebook.pickle', 'wb')
    pickle.dump(entries, myfile)
    myfile.close()
    
def load_saved_contact():
    myfile = open('phonebook.pickle', 'rb')
    global entries
    entries = pickle.load(myfile)
    myfile.close()
    print("Loaded saved entries!")
    
while True:
    menu_choice = int(input("Type in a number (1-7): "))
    if menu_choice == 1:
        print("Print all contacts' information: ")
        print_nested(entries)
    elif menu_choice == 2:
        print("Add a contact: ")
        add_contact()
    elif menu_choice == 3:
        print("Remove a contact: ")
        remove_contact()
    elif menu_choice == 4:
        print("Lookup a contact: ")
        lookup_contact()
    elif menu_choice == 5:
        print("Save the entries: ")
        save_contact()
    elif menu_choice == 6:
        print("Load saved entries: ")
        load_saved_contact()
    elif menu_choice == 7:
        print("Quit!")
        break
    else:
        print("Number is invalid!")
        