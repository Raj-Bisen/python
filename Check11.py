"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept  N number from user and check whether numbers contains 11 in it or not
# input :    5          1,2,9,11,5      
# output :    True                 
# input : 5         1,2,3,4,5
# output :    False
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def CheckNum(List,Length):
    if (List == 0 ) | (Length <= 0):  
        return
    for i in range(len(List)):
        if List[i]  == 11:
            break
    print("Accepted elements are :",List)
    if i == Length:
        return False
    else :
        return True
   
def main():   
    Arr=  []
    print("Enter the number of elements :")
    Size = int(input())
    
    for i in range (Size):
        print("Enter element number : ",i+1)
        Value = int(input())
        Arr.append(Value)
   
    print("*************************")
    bret = CheckNum(Arr,Size)
    if bret == True:
        print("It contains 11")
    else:
        print("It does not contains 11 ")
    print("*************************")
    
if __name__=="__main__":
    main()