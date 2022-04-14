from msilib import sequence
from typing import *


# while 문으로 작성한 선형 검색 
def seq_search_while(a:Sequence, key:Any) -> int :
    
    i = 0

    while True:
        if a[i]==key:
            return i 
        if i == len(a):
            return -1

        i += 1

def seq_search_for(a:sequence, key:Any) -> int:

    for x in range(len(a)):
        if a[x] == key:
            return x
    
    return -1 



    
if __name__ == "__main__":
    num = int(input("원소의 수를 입력하세요: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input("검색할 값을 입력하세요: "))

    idx = seq_search_while(x,ky)

    if idx == -1: print("검색할 값이 존재하지 않습니다")
    else: print(f"검색 값은 x[{idx}] 에 있습니다")

