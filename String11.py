"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept string from user and Toggle the string.   (Toggle = a -> A , A -> a)
# input : R a J a
# ouput : rAjA

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def ToggleString(List):  
    #for i  in  (List):
    print("Updated string is : ")
    print(List.swapcase())
       
def main():
    print("Enter the string :")
    Arr = input()
    ToggleString(Arr)  
	
if __name__=="__main__":
	main()