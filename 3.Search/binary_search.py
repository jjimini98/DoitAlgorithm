from typing import *

from argon2 import PasswordHasher

def bin_search(a : Sequence , key : Any) -> int:
    a.sort() 
    pl = 0 #시작값 
    pr = len(a) -1 #끝값 

    while True:
        pc = (pl+pr)//2 #중앙값 
        if a[pc] > key:
            pr = pc -1 

        elif a[pc] < key:
            pl = pc +1 
        elif a[pc] == key: return pc 

        if pl > pr : break 
    return -1 

if __name__ == "__main__":
    a = [5,95,23,12,33,50,10,2]
    key = 12
    print(bin_search(a,key))