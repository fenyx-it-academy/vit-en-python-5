# This is a Python program
"""  <<<PHONE BOOK>>>   """

phonebook = list([])

def exist_item(fname, lname):
    fitem = False
    for x in phonebook:
        if (x["fname"] == fname) and (x["lname"] == lname):
            return True

    return False
# End of the exist_item

def add_new_contact():
    fname = input("Please enter contact First Name: ")
    lname = input("Please enter contact Last Name: ")
    phone = input("Please enter contact Phone Number: ")

    if exist_item(fname, lname) == True:
        msg = "{0} {1} exist! so you can not add this contact. just you can update!"
        print(msg.format(fname, lname))
    else:
        dict_add = {"fname" : fname,
        "lname" : lname,
        "phone" : phone}

        phonebook.append(dict_add)
# End of the add_new_contact

def edit_contact():
    fname = input("Please enter contact First Name: ")
    lname = input("Please enter contact Last Name: ")
    #phone = input("Please enter contact Phone Number: ")

    num_item = 0
    for x in phonebook:
        if (x["fname"] == fname) and (x["lname"] == lname):
            cmd_text = """
             If you want delete data enter D:
             If you want update data enter U: """
            print(cmd_text)
            cmd = input()
            if cmd.lower() == 'd':
                phonebook.remove(x)
            elif cmd.lower() == 'u':
                fname00 = input("Please enter new FIRST NAME: ")
                lname00 = input("Please enter new LASTNAME: ")
                phone00 = input("Please enter new PHONE:")

                phonebook[num_item]['fname'] = fname00
                phonebook[num_item]['lname'] = lname00
                phonebook[num_item]['phone'] = phone00
            else:
                print("You entered wrong command!")
        num_item += 1

 # End of edit_contact

def delete_contact():
    fname = input("Please enter contact First Name: ")
    lname = input("Please enter contact Last Name: ")

    for x in phonebook:
        if (x["fname"] == fname) and (x["lname"] == lname):
                phonebook.remove(x)

# End of the delete_contact

def search_contact():
    fname = input("Please enter contact First Name: ")
    lname = input("Please enter contact Last Name: ")

    fitem = False
    for x in phonebook:
        if (x["fname"] == fname) and (x["lname"] == lname):
            print("The phone number of ",x['fname'], x['lname'], ' is:', x['phone'])
            fitem = True
            break

    if fitem == False:
        print("There is no contact that you entered!!!")

# End of search_contact


command = ''
while not(command.lower() == 'exit'):

    msgcommand = """
    If you want to add a new contact, please enter A: 
    If you want to update a existing contact, please enter U:
    If you want to find a existing contact, please enter S:
    If you want to delete a existing contact, please enter D:
     For ending of program, Please enter the word <<<EXIT>>>."""
    print(msgcommand)

    command = input()

    if command.lower() == 'a':
        add_new_contact()
    elif command.lower() == 'u':
        edit_contact()
    elif command.lower() == 'd':
        delete_contact()
    elif command.lower() == 's':
        search_contact()
    else:
        print("YOU ENTERED WRONG DATA!")

    print(phonebook)

#End of the program