"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept  N number from user and return sum of  even numbers.
# input :    5          1,2,3,4,5
# output :    2+4 = 6                 
   
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def SumEvenNum(List,Length):
    Sum = 0
    if (List == 0 ) | (Length <= 0):  
        return
    for i in range(len(List)):
        if List[i] % 2 == 0:
            Sum = Sum + List[i]
    return Sum
   
def main():   
    Arr=  []
    print("Enter the number of elements :")
    Size = int(input())
    
    for i in range (Size):
        print("Enter element number : ",i+1)
        Value  = int(input())
        Arr.append(Value)
    print("*************************")
    ret = SumEvenNum(Arr,Size)
    print("Addition of even number is :",ret)
    print("*************************")
    
if __name__=="__main__":
    main()