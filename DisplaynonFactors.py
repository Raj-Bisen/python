# accept number from user and Display its non factors
# input : 6
# output : 4    5
def NonFactors(no):
    iCnt = 1 
    for i in range(1,no):       # no1 = 6
        if no % iCnt != 0 :
            print(iCnt)
        iCnt = iCnt +1
   
    #while(iCnt <= no):
       # if((no % iCnt) != 0):
            #print(iCnt)
      #iCnt = iCnt + 1
    
def main():
    print("Enter the number")
    value = int(input())
    print("**************************") 
    NonFactors(value)
    print("**************************") 

if __name__=="__main__":
    main()