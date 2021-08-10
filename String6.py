"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept string from user and return frequency of capital letters in   string
# input : RAjAji
# ouput : 3

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def Countcap(List):  
    iCnt = 0
    for i  in  (List):
        if (i.isupper()):
            iCnt += 1
    return iCnt    
        
def main():
    print("Enter the string :")
    Arr = input()
    ret = Countcap(Arr)
    print("The count of capital letters  is : ",ret)
	
if __name__=="__main__":
	main()