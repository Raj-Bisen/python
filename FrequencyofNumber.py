"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept  N numbers  and one number from user and return Frequency of numbers.
# input :    5          1,2,1,1,5      1
# output :    3                 
   
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def FrequencyNum(List,Length,iNo):
    iCnt = 0
    if (List == 0 ) | (Length <= 0):  
        return
    for i in range(len(List)):
        if List[i]  == iNo:
            iCnt += 1
    return iCnt
   
def main():   
    Arr=  []
    print("Enter the number of elements :")
    Size = int(input())
    
    for i in range (Size):
        print("Enter element number : ",i+1)
        Value1 = int(input())
        Arr.append(Value1)
    
    print("Enter the number to find frequency : ")
    Value2 = int(input())
    
    print("*************************")
    ret = FrequencyNum(Arr,Size,Value2)
    print("Frequency is :",ret)
    print("*************************")
    
if __name__=="__main__":
    main()