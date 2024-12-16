#Ryan Haddadi
#October 21 2021

from contacts import *

pick = Contacts("txt.dat")

choice = 0
while(True):
	print ("      Tuffy Titan Contact Main Menu   ")
	print ("1.) Add contact")
	print ("2,) Modify contact")
	print ("3.) Delete contact")
	print ("4.) Print contact list")
	print ("5.) Set contact filename")
	print ("6.) Exit the program")
	choice = int(input("Enter menu choice:"))
	if choice == 1:
		phone = input("Enter phone number:")
		f = input("Enter first name:")
		l = input("Enter last name:")
		pick.add_contact(id = phone, first_name = f, last_name = l)
	elif choice == 2:
		phone = int(input("Enter the phone number you want to modify:"))
		f = input("Enter first name:")
		l = input("Enter last name:")
		pick.modify_contact(id = phone, first_name = f, last_name = l)
	elif choice == 3:
		phone = input("Enter the phone number you want to delete:")
		pick.delete_contact(id = phone)
	elif choice == 4:
		print ("Last Name              First Name             Phone Number")
		check = dict(sorted(pick.t.items(), key=lambda x: (x[1][1].lower(), x[1][0].lower()), reverse = False)) 
		for key,value in check.items():
			print(f'{value[1]:22}{value[0]:22}{str(key):8}')
	elif choice == 5:
		filename = input("Enter a contact filename you want to set:")
		pick.different_filename(filename)
	elif choice == 6:
		break
