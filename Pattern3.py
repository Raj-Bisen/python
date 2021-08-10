# Accept number from user and display below pattern.
# input :    Row= 3      Col = 3     
# output : 1    2    3
#                *    *    *
#                1    2    3

def DisplayPattern(no1,no2):
    #iCnt = 1
    for i in range(1,no1+1):
        iCnt = 1
        for j in range(1,no1+1):
            if i % 2 == 0:
                print("*",end = "    ")
            else:
                print(iCnt,end = "    ")
            iCnt = iCnt + 1
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