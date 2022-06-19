import numpy as np
import randset
import os

src_dir=os.path.dirname(os.path.realpath(__file__))
data_dir=src_dir+r'/data'

character_set_file=data_dir+r'/character_set.txt'
rotor_info_file=data_dir+r'/rotor_info.txt'
selected_rotors_file=data_dir+r'/selected_rotors.txt'
start_pos_file=data_dir+r'/start_pos.txt'
reflector_info_file=data_dir+r'/reflector_info.txt'
plugboard_info_file=data_dir+r'/plugboard_info.txt'

f=open(character_set_file)
s=f.readline()
char_cnt=len(s)
f.close()

max_rotor_cnt=0
f=open(rotor_info_file)
while True:
    if not f.readline():
        break
    max_rotor_cnt+=1
f.close()

def change_def_plugboard_settings(rand=True,plugboard=None):
    # rand is boolean flag implying whether the data to replace current data with is generated randomly
    # to generate new data from input(i.e rand==False) plugboard can be filename(containing pairs) or numpy array of dim (x,2) where x is no. of pairs
    if rand:
        plugboard=randset.randplugboard(char_cnt)
    else:
        if not isinstance(plugboard,np.ndarray):
            plugboard=np.loadtxt(plugboard,dtype=np.int64)
    np.savetxt(plugboard_info_file,plugboard,fmt='%1d')

def change_def_rotor_settings(randselrotors=True,selrotors=None,randstartpos=True,startpos=None):
    # randselrotors(randstartpos) is boolean flag implying whether the data to replace current data with is generated randomly
    # if randselrotors(randstartpos)=False selrotors(startpos) can be filenames or the actual tuples
    if randselrotors:
        selrotors=randset.randselrotors(max_rotor_cnt)
    else:
        if not isinstance(selrotors,tuple):
            f=open(selrotors)
            s=f.getline.split(' ')
            f.close()
            selrotors=tuple([np.int64(i) for i in s])
    f.open(selected_rotors_file,'w')
    f.write(str(selrotors[0])+' '+str(selrotors[1])+' '+str(selrotors[2])+'\n')
    f.close()

    if randstartpos:
        startpos=randset.randstartpos(char_cnt)
    else:
        if not isinstance(startpos,tuple):
            f=open(startpos)
            s=f.readline().split(' ')
            f.close()
            startpos=tuple([np.int64(i) for i in s])
    f.open(start_pos_file,'w')
    f.write(str(startpos[0])+' '+str(startpos[1])+' '+str(startpos[2])+'\n')
    f.close()


    