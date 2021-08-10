"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept string from user and Reverse the string
# input : raj
# ouput : jar
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def ReverseString(List):  
    str = ""
    for i in (List):
        str = i + str
    return str   
    
def main():
    print("Enter the string :")
    Arr = input()
    ret = ReverseString(Arr)
    print("Reversed  string is : ",ret)    
	
if __name__=="__main__":
	main()