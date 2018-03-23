import os

stock = {
'bottoms' :["slim Jeans", "joggers", "shorts"],
'jerseys' :["seather jacket", "hoody", "woolen jersey", "ordinary jacket"],
'shoes' :["sneakers", "sandals", "slops", "pumps", "oxfords"]
}

shopping_cart = []

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")

uname = input("Please pick a username: ")

def welcome_note():
	clear_screen()
	print("Hie {}, Have a great shopping experience".format(uname))

def choosing():
	print("We only have BOTTOMS, JERSEYS, SHOES  in stock")
	user_choice = input("Choose section ? ").lower()
	return user_choice

def show_cart():
	if len(shopping_cart) == 0:
		print("Cart is currently empty, Pliz add items!")
		
	else:
		print("Here's your cart:")
		for item in shopping_cart:
			print(item)
		
def main():
	welcome_note()
	choose_sect = choosing()
	while True:
		if choose_sect == 'bottoms':
			print ('item:')
			for item in stock['bottoms']:
				print(item)
			
			while True:
				print("Enter items to shopping cart")
				print("Enter  'Done' to choose another section")
				print("Enter show to view cart")
				print("Enter quit to exit app")
				fnl_choice = input("").lower()
				
				if fnl_choice in stock['bottoms']:
					if fnl_choice in shopping_cart:
						print("{} is already in the cart".format(fnl_choice))
					shopping_cart.append(fnl_choice)
				elif fnl_choice == 'done':
					break
				elif fnl_choice == 'show':
					show_cart()
				elif fnl_choice == 'quit':
					show_cart()
					exit()
				elif fnl_choice not in 'bottoms':
					print("{} not in stock at the moment".format(fnl_choice))
					
		elif choose_sect == 'jerseys':
			print ('item:')
			for item in stock['jerseys']:
				print(item)
			
			while True:
				print("Enter items to shopping cart")
				print("Enter 'Done' to choose another section")
				print("Enter show to view cart")
				print("Enter quit to exit app")
				fnl_choice = input("").lower()
			
				if fnl_choice in stock['jerseys']:
					if fnl_choice in shopping_cart:
						print("{} is already in the cart".format(fnl_choice))
					shopping_cart.append(fnl_choice)
				elif fnl_choice == 'done':
					break
				elif fnl_choice == 'show':
					show_cart()
				elif fnl_choice == 'quit':
					show_cart()
					exit()
				elif fnl_choice not in 'jerseys':
					print("{} not in stock at the moment".format(fnl_choice))
					
		elif choose_sect == 'shoes':
			print ('item:')
			for item in stock['shoes']:
				print(item)
			
			while True:
				print("Enter items to shopping cart")
				print("Enter  'Done' to choose another section")
				print("Enter show to view cart")
				print("Enter quit to exit app")
				fnl_choice = input("").lower()
				
				if fnl_choice in stock['shoes']:
					if fnl_choice in shopping_cart:
						print("{} is already in the cart".format(fnl_choice))
					shopping_cart.append(fnl_choice)
				elif fnl_choice == 'done':
					break
				elif fnl_choice == 'show':
					show_cart()
				elif fnl_choice == 'quit':
					show_cart()
					exit()
				elif fnl_choice not in 'shoes':
					print("{} not in stock at the moment".format(fnl_choice))
					
		choose_sect = choosing()
				
main()


