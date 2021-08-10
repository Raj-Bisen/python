"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept  N number from user and return maximum number .
# input :    5          1,2,6,2,5      
# output :    Maximum : 5                 
   
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def MaximumNum(List,Length):
    Max = List[0]
    if (List == 0 ) | (Length <= 0):  
        return
    for i in range(len(List)):
        if List[i] > Max:
            Max = List[i]
    return Max
    
   
def main():   
    Arr=  []
    print("Enter the number of elements :")
    Size = int(input())
    
    for i in range (Size):
        print("Enter element number : ",i+1)
        Value = int(input())
        Arr.append(Value)
    
    print("*************************")
    ret = MaximumNum(Arr,Size)
    print("Maximum number  is :",ret)
    print("*************************")
    
if __name__=="__main__":
    main()