from tkinter import *
from tkinter import filedialog
from functools import partial
from datetime import datetime
import os

src_dir=os.path.dirname(os.path.realpath(__file__))
data_dir=src_dir+r'/data'

character_set_file=data_dir+r'/character_set.txt'
rotor_info_file=data_dir+r'/rotor_info.txt'
selected_rotors_file=data_dir+r'/selected_rotors.txt'
start_pos_file=data_dir+r'/start_pos.txt'
reflector_info_file=data_dir+r'/reflector_info.txt'
plugboard_info_file=data_dir+r'/plugboard_info.txt'

# Define the function you want to call when the filebrowser button is clicked.
def fileClick():
    pass

def process():
    pass

if __name__ == '__main__':
    root = Tk()
    root.title("Enigma Machine")
    root.geometry("1400x1400")
    cwd = os.path.dirname(os.path.realpath(__file__))
    
    txtent=Frame(root)
    txtent.grid(row=0,column=1,rowspan=9)
    heading_txt=StringVar()
    heading=Entry(txtent,textvariable=heading_txt,font=("Nimbus Mono PS",12,'bold'),justify=CENTER,width=50)
    heading.insert(0,'Enter title here ...')
    heading.grid(row=0,column=0,padx="5", pady="5",ipadx="10",ipady="10")

    now=datetime.now()
    dt_string=StringVar()
    dt_string.set(now.strftime("%d/%m/%Y %H:%M:%S"))
    time=Entry(txtent,textvariable=dt_string,state=DISABLED,font=("Nimbus Mono PS",12,'bold'),justify=CENTER)
    time.grid(row=0,column=1,padx="5",pady="5",ipadx="10",ipady="10")
    uncr_input=Text(txtent,font=("Nimbus Mono PS",12),width="50",height="7")
    encr_input=Text(txtent,font=("Nimbus Mono PS",12),width="50",height="34")
    output=Text(txtent,font=("Nimbus Mono PS",12),width=50,height=37)

    uncr_input.insert('end','Enter introduction (will not be encrypted)...')
    encr_input.insert('end','Enter content (plain text to be encrypted)...')
    output.insert('end','Output text appears here ...')
    output.configure(state='disabled')

    uncr_input.grid(row=1,column=0,rowspan=2,padx="5", pady="5",ipadx="10",ipady="10")
    encr_input.grid(row=6,column=0,rowspan=7,padx="5", pady="5",ipadx="10",ipady="10")
    output.grid(row=1,column=1,rowspan=6,padx="5", pady="5",ipadx="10",ipady="10")

    # hello=Label(txtent,text="hello")
    # hello.grid(row=8,column=1)

    # hello1=Label(txtent,text="hello")
    # hello1.grid(row=9,column=1)

    # hello2=Label(txtent,text="hello")
    # hello2.grid(row=10,column=1)

    # hello3=Label(txtent,text="hello")
    # hello3.grid(row=11,column=1)

    button_frame=Frame(txtent)
    button_frame.grid(row=7,column=1,rowspan=5)

    convert_button=Button(button_frame,font=('Nimbus Mono PS',12),text='PROCESS INPUT',command=fileClick)
    convert_button.grid(row=0,column=0,columnspan=3,padx=5,pady=5)

    chose_folder_label=Label(button_frame,text="Save to (dir)",font=('Nimbus Mono PS',10))
    chose_folder_label.grid(row=1,column=0)

    path_entry=Entry(button_frame,font=('Nimbus Mono PS',10),width=35)
    path_entry.grid(row=1,column=1,padx=5,pady=5)

    folder_explore = Button(button_frame, text = "BROWSE...",font=('Nimbus Mono PS',10),command = fileClick)
    folder_explore.grid(column = 2, row = 1, padx="5")

    chose_file_label=Label(button_frame,text="Save as (file)",font=('Nimbus Mono PS',10))
    chose_file_label.grid(row=2,column=0)

    file_entry=Entry(button_frame,font=('Nimbus Mono PS',10),width=35)
    file_entry.grid(row=2,column=1,padx=5,pady=5)

    save_button = Button(button_frame, text = "SAVE FILE",font=('Nimbus Mono PS',10),command = fileClick)
    save_button.grid(column = 2, row = 2, padx="5")
    
	####### CODE REQUIRED (START) #######
	# Declare the file browsing button
    #file_explore = Button(root, text = ". . .",command = partial(fileClick,clicked), padx="20")
    filename = ""
    #file_explore.grid(column = 1, row = 0, padx="5")
	####### CODE REQUIRED (END) #######

	####### CODE REQUIRED (START) #######
	# Declare the drop-down button
    #dropdown = OptionMenu(root,clicked,*options)
    # dropdown.config(font=("Nimbus Mono PS",10))
    #dropdown.grid(column = 2,row = 0, padx="5", pady="5")
    img_label_1 = Label(root) # label that would contain the original image
    img_label_2 = Label(root) # label with the masked/boxed image
	# both the image labels would be made visible when a file is selected
	####### CODE REQUIRED (END) #######

	# This is a `Process` button, check out the sample video to know about its functionality
    #myButton = Button(root, text="Process", command=partial(process, clicked))
    #myButton.grid(row=0, column=3)

    my_frame=Frame(root,highlightthickness=2,highlightbackground='black')
    my_frame.grid(row=0,column=0,rowspan=9,padx=5,pady=5)

    engsett_label=Label(my_frame,text='ENIGMA\nSETTINGS',font=('Nimbus Mono PS',10,'bold'))
    engsett_label.grid(row=0,column=0)

    selrotors_label=Label(my_frame,text='Selected\nrotors:',font=('Nimbus Mono PS',10))
    selrotors_label.grid(row=1,column=0)

    selrotors_settings=Text(my_frame,font=('Nimbus Mono PS',10),width=8,height=2)
    f=open(selected_rotors_file)
    selrotors_settings.insert('end',f.read())
    f.close()
    selrotors_settings.grid(row=2,column=0)

    startpos_label=Label(my_frame,text='Startpos:',font=('Nimbus Mono PS',10))
    startpos_label.grid(row=3,column=0)

    startpos_settings=Text(my_frame,font=('Nimbus Mono PS',10),width=8,height=2)
    f=open(start_pos_file)
    startpos_settings.insert('end',f.read())
    f.close()
    startpos_settings.grid(row=4,column=0)

    plugboard_label=Label(my_frame,text='Plugbrd\npairings:',font=('Nimbus Mono PS',10))
    plugboard_label.grid(row=5,column=0)

    plugboard_settings=Text(my_frame,font=('Nimbus Mono PS',10),width=8,height=42)
    f=open(plugboard_info_file)
    plugboard_settings.insert('end',f.read())
    f.close()
    plugboard_settings.grid(row=6,column=0,rowspan=4)


	
	####### CODE REQUIRED (START) ####### (1 line)
	# Execute with mainloop()
    root.mainloop()
	####### CODE REQUIRED (END) #######