"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept  N number from user and return addition  N numbers.
# input :    5          10,20,30,40,50
# output :  10+20+30+40+50 = 150                      
                                                  
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def AdditionNNum(List,Length):
    if(List == 0) | (Length <= 0):
        return
    Sum = 0
    for i in range(len(List)):
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
    
    print("*******************************")
    ret = AdditionNNum(Arr,Size)
    print("Addition of n number is : ",ret)
    print("*******************************")
    
if __name__=="__main__":
    main()