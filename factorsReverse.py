# accept number from user and display its factors in Reverse order
# input : 6
# output : 3    2    1
def FactorsRev(no):
    iCnt = int(no/2) 
    for i in range(1,int(no/2)+1):       # no = 6
        if no %  iCnt == 0:
            print(iCnt)
        iCnt = iCnt -1
    
    #while(iCnt >= 1):
        #if((no % iCnt) == 0):
            #print(iCnt)    
        #iCnt = iCnt - 1
        
def main():
    print("Enter the number")
    value = int(input())
    print("**************************") 
    FactorsRev(value)
    print("**************************") 

if __name__=="__main__":
    main()