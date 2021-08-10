# Accept number from user and display below pattern.
# input :    Row = 3     Col =  3     
# output : *    *    *
#                *    *    *
#                *    *    *

def DisplayPattern(no1,no2):
    for i in range(0,no1):
        for j in range(0,no1):
            print("*",end = "    ")
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