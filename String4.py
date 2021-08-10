"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept string from user and return frequency of a in  string
# input : RajaBabu
# ouput : 3

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def Counta(List):  
    iCnt = 0
    for i  in  (List):
        if i == 'a' :
            iCnt += 1
    return iCnt    
        
def main():
    print("Enter the string :")
    Arr = input()
    ret = Counta(Arr)
    print("The Frequency of a is : ",ret)
	
if __name__=="__main__":
	main()