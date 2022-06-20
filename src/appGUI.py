from tkinter import *
from tkinter import filedialog
from functools import partial
import os

# Define the function you want to call when the filebrowser button is clicked.
def fileClick(clicked):
    pass

def process(clicked):
    pass

if __name__ == '__main__':
    root = Tk()
    root.title("Enigma Machine")
    cwd = os.path.dirname(os.path.realpath(__file__))
    options = ["Segmentation", "Bounding-box"]
    clicked = StringVar()
    clicked.set(options[0])
    heading_txt=StringVar()
    heading=Entry(root,textvariable=heading_txt,justify=CENTER,width=40)
    
    heading.grid(row=0,column=0,padx="5", pady="5")
    e = Entry(root, width=70)
    # e.grid(row=0, column=0)

	####### CODE REQUIRED (START) #######
	# Declare the file browsing button
    file_explore = Button(root, text = ". . .",command = partial(fileClick,clicked), padx="20")
    filename = ""
    file_explore.grid(column = 1, row = 0, padx="5")
	####### CODE REQUIRED (END) #######

	####### CODE REQUIRED (START) #######
	# Declare the drop-down button
    dropdown = OptionMenu(root,clicked,*options)
    # dropdown.config(font=("Nimbus Mono PS",10))
    dropdown.grid(column = 2,row = 0, padx="5", pady="5")
    img_label_1 = Label(root) # label that would contain the original image
    img_label_2 = Label(root) # label with the masked/boxed image
	# both the image labels would be made visible when a file is selected
	####### CODE REQUIRED (END) #######

	# This is a `Process` button, check out the sample video to know about its functionality
    myButton = Button(root, text="Process", command=partial(process, clicked))
    myButton.grid(row=0, column=3)

	
	####### CODE REQUIRED (START) ####### (1 line)
	# Execute with mainloop()
    root.mainloop()
	####### CODE REQUIRED (END) #######