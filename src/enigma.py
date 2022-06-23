import numpy as np
import os

src_dir=os.path.dirname(os.path.realpath(__file__))
# par_dir=os.path.dirname(src_dir)
data_dir=src_dir+r'/data'

character_set_file=data_dir+r'/character_set.txt'
rotor_info_file=data_dir+r'/rotor_info.txt'
selected_rotors_file=data_dir+r'/selected_rotors.txt'
start_pos_file=data_dir+r'/start_pos.txt'
reflector_info_file=data_dir+r'/reflector_info.txt'
plugboard_info_file=data_dir+r'/plugboard_info.txt'

def construct_mapping(x,y,M):
    # returns numpy array containing [1,2,...,M] with y in x-th posn
    arr=np.arange(M)
    arr=(arr-(x-y)+M)%M
    return arr

def construct_rev(rotor):
    # returns inverse of the rotor mappings
    rev=np.empty_like(rotor)
    for i,v in enumerate(rotor):
        rev[v]=i
    return rev

def make_pairs(pairs_list,M):
    # reads (x,2) dimentional np array and returns an np.arr where members of each line is paired
    paired=np.arange(M)
    for arr in pairs_list:
        paired[arr[0]]=arr[1]
        paired[arr[1]]=arr[0]
    return paired

class enigma:
    def __init__(
        self,
        char_info=character_set_file,
        rotor_info=rotor_info_file,
        selected_rotors=selected_rotors_file,
        start_pos=start_pos_file,
        reflector=reflector_info_file,
        plugboard=plugboard_info_file
    ):
        # setup character to index and index to character mappings
        f=open(char_info)
        self.idx_to_char=f.readline()
        self.idx_to_char=self.idx_to_char[:-1]
        self.char_cnt=len(self.idx_to_char)
        self.char_to_idx={}
        for i,v in enumerate(self.idx_to_char):
            self.char_to_idx[v]=i
        f.close()
        
        # setup rotors
        if isinstance(rotor_info,np.ndarray):
            self.rotor_set=rotor_info
        else:
            self.rotor_set=np.loadtxt(rotor_info,dtype=np.int64)
        self.max_rotor_cnt=self.rotor_set.shape[0]

        # put selected rotors in position
        if not isinstance(selected_rotors,tuple):
            f=open(selected_rotors)
            selected_rotors=[]
            for item in f.readline().split(' '):
                selected_rotors.append(np.int64(item))
            f.close()
        self.rotors=[]
        for i in selected_rotors:
            self.rotors.append(self.rotor_set[i-1]) 
        # set the inverse rotor mappings
        self.rotors_inv=[]
        for rotor in self.rotors:
            self.rotors_inv.append(construct_rev(rotor))

        # configure rotors to align at the start position
        if not isinstance(start_pos,tuple):
            f=open(start_pos)
            start_pos=[]
            for item in f.readline().split(' '):
                start_pos.append(np.int64(item))
            start_pos=list(start_pos)
            f.close()
        self.start_pos=start_pos

        self.reset()

        # setup reflector
        if not isinstance(reflector,np.ndarray):
            reflector=np.loadtxt(reflector,dtype=np.int64)
        self.reflector=make_pairs(reflector,self.char_cnt)

        # setup plugboard
        if not isinstance(plugboard,np.ndarray):
            plugboard=np.loadtxt(plugboard,dtype=np.int64)
        self.plugboard=make_pairs(plugboard,self.char_cnt)

    def reset(self):
        # start_pos is a tuple of visible indices of the rotors during initial setting 
        self.zero_to_one=construct_mapping(self.start_pos[0],self.start_pos[1],self.char_cnt)
        self.one_to_two=construct_mapping(self.start_pos[1],self.start_pos[2],self.char_cnt)
        self.two_to_one=construct_mapping(self.start_pos[2],self.start_pos[1],self.char_cnt)
        self.one_to_zero=construct_mapping(self.start_pos[1],self.start_pos[0],self.char_cnt)
        self.vis=list(self.start_pos)

    def rotate_rotor_zero(self):
        self.zero_to_one=(self.zero_to_one-1+self.char_cnt)%self.char_cnt
        self.one_to_zero=(self.one_to_zero+1)%self.char_cnt
        self.vis[0]=(self.vis[0]+1)%self.char_cnt
    
    def rotate_rotor_one(self):
        self.one_to_zero=(self.one_to_zero-1+self.char_cnt)%self.char_cnt
        self.zero_to_one=(self.zero_to_one+1)%self.char_cnt
        self.one_to_two=(self.one_to_two-1+self.char_cnt)%self.char_cnt
        self.two_to_one=(self.two_to_one+1)%self.char_cnt
        self.vis[1]=(self.vis[1]+1)%self.char_cnt
        
    def rotate_rotor_two(self):
        self.two_to_one=(self.two_to_one-1+self.char_cnt)%self.char_cnt
        self.one_to_two=(self.one_to_two+1)%self.char_cnt
        self.vis[2]=(self.vis[2]+1)%self.char_cnt

    def convert(self,plain_txt):
        # encrypt plain text / decrypt cipher text
        self.reset()
        cipher=''
        
        for char in plain_txt:
            if char not in self.char_to_idx:
                cipher+=char
                continue
            p=self.char_to_idx[char]
            p=self.plugboard[p]
            p=self.rotors[0][p]
            p=self.zero_to_one[p]
            p=self.rotors[1][p]
            p=self.one_to_two[p]
            p=self.rotors[2][p]
            p=self.reflector[p]
            p=self.rotors_inv[2][p]
            p=self.two_to_one[p]
            p=self.rotors_inv[1][p]
            p=self.one_to_zero[p]
            p=self.rotors_inv[0][p]
            p=self.plugboard[p]
            
            e=self.idx_to_char[p]
            cipher+=e
            
            self.rotate_rotor_zero()
            if self.vis[0]==0:
                self.rotate_rotor_one()
                if self.vis[1]==0:
                    self.rotate_rotor_two()
            print('*')
        return cipher

def main():
    en=enigma()
    plain_text='Plain text nothing special here!'
    cipher=en.convert(plain_text)
    print('Encrypted text: '+cipher)
    retrieved_text=en.convert(cipher)
    print('Retrieved text: '+retrieved_text)


if __name__=='__main__':
    main()
