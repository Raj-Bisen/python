# accept number from user and display its factors
# input : 6
# output : 1    2   3
def DisplayFactors(no):
    iCnt = 1 
    for i in range(1,int(no/2)+1):       # no = 6
        if no%iCnt == 0:
            print (iCnt)
        iCnt = iCnt +1
    
    
    #while(iCnt <= no/2):
       # if((no % iCnt) == 0):
           # print(iCnt)
       # iCnt = iCnt + 1
    
    
def main():
    print("Enter the number")
    value = int(input())
    print("**************************")
    DisplayFactors(value)
    print("**************************") 

if __name__=="__main__":
    main()