"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept  N number from user and display only even numbers on screen.
# input :    5          1,2,3,4,5
# output :  Even numbers are :  2,4                  
   
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def DisplayEvenNum(List,Length):
    if (List == 0 ) | (Length <= 0):  
        return
    print("*************************")
    print("Even numbers are : ")
    for i in range(len(List)):
        if List[i] % 2 == 0:
            print(List[i])
    print("*************************")
    
def main():   
    Arr=  []
    print("Enter the number of elements :")
    Size = int(input())
    
    for i in range (Size):
        print("Enter element number : ",i+1)
        Value  = int(input())
        Arr.append(Value)
    
    DisplayEvenNum(Arr,Size)

if __name__=="__main__":
    main()