"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept string from user and return frequency of small letters in   string
# input : RAjAJi
# ouput : 2

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def Countsmall(List):  
    iCnt = 0
    for i  in  (List):
        if (i.islower()):
            iCnt += 1
    return iCnt    
        
def main():
    print("Enter the string :")
    Arr = input()
    ret = Countsmall(Arr)
    print("The count of small letters  is : ",ret)
	
if __name__=="__main__":
	main()