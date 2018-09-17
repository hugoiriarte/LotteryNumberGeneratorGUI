#Imports easyFrame from the breezypythongui folder
from breezypythongui import EasyFrame
#imports random
import random
#sets up the main class
class Addition(EasyFrame):
	#Main function
	def __init__(self):
		#App title
		EasyFrame.__init__(self, title = "Lottery Number Generator")
		#5 text fields with no text inside
		self.outputField0 = self.addTextField(text = "", row = 0, column = 0, state = "readonly")
		self.outputField1 = self.addTextField(text = "", row = 0, column = 1, state = "readonly")
		self.outputField2 = self.addTextField(text = "", row = 0, column = 2, state = "readonly")
		self.outputField3 = self.addTextField(text = "", row = 0, column = 3, state = "readonly")
		self.outputField4 = self.addTextField(text = "", row = 0, column = 4, state = "readonly")
		#Button that will run the generate function
		self.addButton(text = "Generate", row = 1, column = 0, command = self.generate)
	#establishing the generate function	
	def generate(self):
		#Empty array
		arrayList = []
		#for loop that will generate a random number between 1 and 99
		for x in range(5):
			randomNum = random.randint(1,99)
			#appends every itiration the the empty array list
			arrayList.append(randomNum)
		#outputs the array list per index
		self.outputField0.setText(arrayList[0])
		self.outputField1.setText(arrayList[1])
		self.outputField2.setText(arrayList[2])
		self.outputField3.setText(arrayList[3])
		self.outputField4.setText(arrayList[4])
#establishing the main function		
def main():
	#Runs the addition method
	Addition().mainloop()
#Call to the main function	
main()