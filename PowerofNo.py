# Accept number from user return its power
#input : 2    4 
#ouput : 16
def DisplayPower(no1 , no2):
    
    iCnt = 1 
    iMult = 1
    #for i in range(no2):       # no1 = 2 , no2 = 4
        #iMult = iMult * no1
    #return iMult
  
    while(iCnt <= no2):
        iMult = iMult * no1
        iCnt = iCnt +1
    return iMult
  
    
def main():
   
    print("Enter the number")
    value1 = int(input())
    
    print("Enter the number")
    value2 = int(input())
    print("**************************") 
    
    bret = DisplayPower(value1,value2)
    print("Power is : ",bret)
    
    print("**************************") 

if __name__=="__main__":
    main()