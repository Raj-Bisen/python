"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept string from user and return Count of white space in  string
# input : R a j a
# ouput : 3

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def CountWspace(List):  
    iCnt = 0
    for i  in  (List):
        if i == " ":
            iCnt += 1
    return iCnt    
        
def main():
    print("Enter the string :")
    Arr = input()
    ret = CountWspace(Arr)
    print("The count of White spaces   is : ",ret)
	
if __name__=="__main__":
	main()