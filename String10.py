"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept string from user and Convert chracters of string from  Uppercase to  lowercase
# input : R a J A
# ouput : raja

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def ConverttoLower(List):  
    #for i  in  (List):
    print("Updated string is : ")
    print(List.lower())
       
def main():
    print("Enter the string :")
    Arr = input()
    ConverttoLower(Arr)  
	
if __name__=="__main__":
	main()