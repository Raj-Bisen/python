"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept string from user and return frequency of A/a in   string
# input : RajA
# ouput : 2

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def CountAa(List):  
    iCnt = 0
    for i  in  (List):
        if ((i == 'a') | (i == 'A')):
            iCnt += 1
    return iCnt    
        
def main():
    print("Enter the string :")
    Arr = input()
    ret = CountAa(Arr)
    print("The count of A/a  is : ",ret)
	
if __name__=="__main__":
	main()