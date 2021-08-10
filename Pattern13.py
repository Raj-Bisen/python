"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept number from user and display below pattern.
# input :    Row= 4      Col = 4     
# output :                  *         
#                           *    *         
#                    *    *    *    
#              *    *    *    *             
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def DisplayPattern(no1,no2):
    for i in range(1,no1+1):
        for j in range(no2,0,-1):
            if i < j:
                print(" ",end = "    ")
            else:
                print("#",end = "    ")
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