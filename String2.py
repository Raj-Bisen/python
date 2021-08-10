"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept string from user and display chracters from the string
# input : Raj
# ouput :  R
#                a
#                j
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def DisplayChracaters(List):  
    iCnt = 0
    for i  in  (List):
        print(List[iCnt],"\n")
        iCnt += 1
        
def main():
    print("Enter the string :")
    Arr = input()
    DisplayChracaters(Arr)
	
if __name__=="__main__":
	main()