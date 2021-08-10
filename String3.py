"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept string from user and return length of  the string
# input : Raj
# ouput : 3

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def StringLength(List):  
    iCnt = 0
    for i  in  (List):
        iCnt += 1
    return iCnt    
        
def main():
    print("Enter the string :")
    Arr = input()
    ret = StringLength(Arr)
    print("The length of string is : ",ret)
	
if __name__=="__main__":
	main()