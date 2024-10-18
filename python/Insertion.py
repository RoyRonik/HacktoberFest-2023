import random

def insertionSort(ar):
    n = len(ar) 
    if n <= 1:
        return 
 
    for i in range(1, n):  
        key = ar[i] 
        j = i-1

        while j >= 0 and key < ar[j]:  
            ar[j+1] = ar[j] 
            j -= 1
        ar[j+1] = key 

ar = [random.randint(1,100) for i in range(11)]
print("The generated random list is:",ar)
insertionSort(ar)
print(ar)
