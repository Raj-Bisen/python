"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept number from user and display below pattern.
# input :    Row= 4      Col = 3     
# output : 1    2    3
#                1    2    3
#                1    2    3
#                1    2    3
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def DisplayPattern(no1,no2):
    iCnt = 1
    for i in range(0,no1):
        iCnt = 1
        for j in range(0,no1-1):
            print(iCnt,end = "  ")
            iCnt +=1
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