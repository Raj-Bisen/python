"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept number from user and display below pattern.
# input :    Row= 4      Col = 4     
# output : A     
#                A     B
#                A     B    C
#                A     B    C    D
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def DisplayPattern(no1,no2):
    for i in range(0,no1):
        k = ord("A")
        for j in range(0,i+1):
            print(chr(k),end = "    ")
            k += 1
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