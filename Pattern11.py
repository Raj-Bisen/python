"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept number from user and display below pattern.
# input :    Row= 4      Col = 4     
# output : A     
#                B     B
#                C     C    C
#                D     D    D    D
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def DisplayPattern(no1,no2):
    k = ord("A")
    for i in range(0,no1):
        for j in range(0,i+1):
            print(chr(k),end = "    ")
        k = k + 1
        print()
            
        
 
def main():
    print("Enter the number of rows : ")
    iRow = int(input())
    print("Enter the number of columns: ")
    iCol = int(input())
    print("--------------------------------")
    DisplayPattern(iRow,iCol)
    print("\n--------------------------------\n")

if __name__=="__main__":
    main()