# Accept number from user and Display that numbers of even numbers on screen
#input : 6
#ouput : 2  4   6   8   10  12

def DisplayEven(no):
    iCnt = 1
    print("***********************") 
    for i in range(2*no):
        if(iCnt % 2) == 0:
            print(iCnt)
        iCnt = iCnt + 1
    print("***********************")    
    #while(iCnt <= 2* no):
        #if(iCnt % 2) == 0:
         #   print(iCnt)
       # iCnt = iCnt +1
    
    
def main():
    print("Enter the number")
    value = int(input())
    DisplayEven(value)
    
if __name__=="__main__":
    main()