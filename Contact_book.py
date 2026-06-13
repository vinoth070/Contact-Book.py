
def add_Contact(fileName):

    name = input("Enter Contact Name : ")
    phone = input("Enter Contact Number :")

    with open(fileName,'a') as file:

        file.write(f"{name} - {phone}\n")

    print("Contact Added.!")



def view_Contact(fileName):

    with open(fileName,'r') as file:

        contacts = file.readlines()

        for contact in contacts:

            print(contact.strip())




fileName = "Contacts.txt"

while True:
    
    choice = input("1. Add Contact\n2. View Contact\n3. Exit\n Enter Option : ")


    if choice == "1":
        add_Contact(fileName)
    
    elif choice == "2":

        view_Contact(fileName)

    elif choice == "3":
        break

    else:
        print("Invalid Choice. Please Try Again.")