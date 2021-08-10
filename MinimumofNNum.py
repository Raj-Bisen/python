"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept  N number from user and return minimum number .
# input :    5          1,2,6,2,5      
# output :    Minimum : 1                 
   
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def MinimumNum(List,Length):
    Min = List[0]
    if (List == 0 ) | (Length <= 0):  
        return
    for i in range(len(List)):
        if List[i] < Min:
            Min = List[i]
    return Min
    
   
def main():   
    Arr=  []
    print("Enter the number of elements :")
    Size = int(input())
    
    for i in range (Size):
        print("Enter element number : ",i+1)
        Value = int(input())
        Arr.append(Value)
    
    print("*************************")
    ret = MinimumNum(Arr,Size)
    print("Minimum number  is :",ret)
    print("*************************")
    
if __name__=="__main__":
    main()