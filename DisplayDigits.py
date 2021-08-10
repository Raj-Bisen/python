# Accept number from user and Display digits of that number.
# input :      1435
# output :      5
#                     3
#                     4
#                     1

def DisplayDigits(no):
    iDigit = 0
    while (no != 0):
        iDigit = int(no % 10)
        print(iDigit)
        no = int(no / 10)
    
def main():
    print("Enter the number")
    value = int(input())
    print("*****************************") 
    DisplayDigits(value)
    print("*****************************")  

if __name__=="__main__":
    main()