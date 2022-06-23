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
s=s[:-1]
char_cnt=len(s)
f.close()

max_rotor_cnt=0
f=open(rotor_info_file)
while True:
    if not f.readline():
        break
    max_rotor_cnt+=1
f.close()

def change_rotors(rand=True,rotor_info=None):
    if rand:
        rotor_info=randset.randrotor(max_rotor_cnt,char_cnt)
    else:
        if not isinstance(rotor_info,np.ndarray):
            rotor_info=np.loadtxt(rotor_info,dtype=np.int64)
    np.savetxt(rotor_info_file,rotor_info,fmt='%1d')

def change_reflector(rand=True,reflector_info=None):
    if rand:
        reflector_info=randset.randreflector(char_cnt)
    else:
        if not isinstance(reflector_info,np.ndarray):
            reflector_info=np.loadtxt(reflector_info,dtype=np.int64)
    np.savetxt(reflector_info_file,reflector_info,fmt='%1d')

def main():
    # change_rotors()
    # change_reflector()
    # rotor_input='/home/rounak/Documents/jupyter/environment/Enigma/src/temp_file.txt'
    # change_rotors(rand=False,rotor_info=rotor_input)
    pass

if __name__=='__main__':
    main()