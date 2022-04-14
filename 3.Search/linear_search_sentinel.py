from typing import *

def seq_search(a:Sequence, key:Any) -> int:

    i = 0 
    a.append(key)

    while True:
        if a[i] == key:
            break
        i +=1 

    return -1 if i == len(a) else i 

    
if __name__ == "__main__":
    lis = [6,4,3,2,1,2,8]
    key = 2
    print(seq_search(lis,key))