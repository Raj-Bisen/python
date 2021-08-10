"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept  N numbers and one number  from user and return First Occurence of number.
# input :    5          1,2,6,2,5      
# output :    First occurence is : 1                 
   
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def FirstOccurence(List,Length,iNo):
    if (List == 0 ) | (Length <= 0):  
        return
    for i in range(len(List)):
        if List[i]  == iNo:
            break
    
    if i == len(List)-1 :
        return -1
    else:
        return i
   
def main():   
    Arr=  []
    print("Enter the number of elements :")
    Size = int(input())
    
    for i in range (Size):
        print("Enter element number : ",i+1)
        Value1 = int(input())
        Arr.append(Value1)
    
    print("Enter the number u want to search : ")
    Value2 = int(input())
    
    print("*************************")
    ret = FirstOccurence(Arr,Size,Value2)
    if ret == -1:
        print("There is no such element ")
    else:
        print("First Occurence is :",ret)
    print("*************************")
    
if __name__=="__main__":
    main()