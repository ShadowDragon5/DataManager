"""Function for handling errors"""
import msvcrt as m

def ErrorMessage(*messages, stop = True):
	for mes in messages:
		print(mes)

	print("Press any key to continue...")
	m.getch()

	if (stop):
		quit()
