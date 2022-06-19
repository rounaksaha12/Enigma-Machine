import numpy as np

def randplugboard(M):
    # generates a valid random combination of plugboard pairings
    max_possible_pairs=np.int64(M/2)
    min_admissible_pairs=np.int64(0.7692*max_possible_pairs) # 20/26 = 0.7692
    # randomly generate the number of pairs
    p=np.random.randint(min_admissible_pairs,max_possible_pairs+1)
    # generate a random permutation of [1,2,...,M]
    arr=np.random.choice(M,size=M,replace=False)
    # pair of i with i+1 for i in [0,2,4,...,2*p]
    arr=arr[:2*p]
    arr=np.reshape(arr,(p,2))
    return arr

def randselrotors(max_rotor_cnt):
    # generates a valid random combination of rotors
    arr=np.random.choice(max_rotor_cnt,3,replace=False)
    tup=tuple(arr)
    return tup

def randstartpos(M):
    # generates a random valid start pos (tuple of rotor readings visible)
    arr=np.random.choice(M,3)
    tup=tuple(arr)
    return tup

def randrotor(max_rotor_cnt,M):
    # generates random mappings for each of the available rotors
    arr=np.empty((max_rotor_cnt,M))
    for i in range(max_rotor_cnt):
        r=np.random.choice(M,size=M,replace=False)
        for j in range(M):
            arr[i][j]=r[j]
    return arr

def randreflector(M):
    max_possible_pairs=np.int64(M/2)
    min_admissible_pairs=np.int64(0.95*max_possible_pairs)
    # randomly generate the number of pairs
    p=np.random.randint(min_admissible_pairs,max_possible_pairs+1)
    # generate a random permutation of [1,2,...,M]
    arr=np.random.choice(M,size=M,replace=False)
    # pair of i with i+1 for i in [0,2,4,...,2*p]
    arr=arr[:2*p]
    arr=np.reshape(arr,(p,2))
    return arr