"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept number from user and display below pattern.
# input :    Row= 4      Col = 4     
# output : 1    $    $    $
#                *    2    $    $
#                *    *    3    $
#                *    *    *    4
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def DisplayPattern(no1,no2):
    iCnt = 1
    for i in range(0,no1):
        iCnt = 1
        for j in range(0,no1):
            if i==j:
                print(iCnt,end = "    ")
            elif i<j:
                print("$",end = "    ")
            else:
                print("*", end = "    ")
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