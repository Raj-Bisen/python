# Accept number from user and Display its table
#input : 2
#ouput : 2  4   6   8   10  12  14  16  18  20
def DisplayTable(no):
    print("**************************")
    iCnt = 1
    #while(iCnt <= 10):
        
       # print(no * iCnt)
       # iCnt = iCnt +1
           
       
    for i in range(0,10):
        print(no * iCnt)
        iCnt = iCnt + 1
    print("**************************") 
    
def main():
   
    print("Enter the number")
    value1 = int(input())
    
    bret = DisplayTable(value1)
    

if __name__=="__main__":
    main()