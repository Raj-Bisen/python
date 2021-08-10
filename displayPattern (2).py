# Accept number from user and print below pattern
#Input : 2
# output : *    *
def Display(no):
    #for i in range(no):
        #print("*")
    iCnt = 0   
    while(iCnt < no):
        print("*")
        iCnt = iCnt +1

def main():
    print("Enter the number")
    value1 = int(input())
    
    Display(value1)
    

    

if __name__=="__main__":
    main()