# Accept number from user and check whether 1st number is divisible by 2nd number or not.
#input : 10  5
#output : true
#input: 2   5
#output: false

def ChckNum(no1 , no2):
    if ((no1 % no2)==0): 
        return True
    
    else:
        return False

def main():
    print("Enter the number")
    value1= int(input())
    
    print("Enter second number")
    value2 = int(input())
    
    bret = ChckNum(value1,value2)
    if (bret == True):
        print("1st Number is  divisible by 2nd Number")
    else:
        print("1st Number is  not divisible by 2nd Number")
    
    

    

if __name__=="__main__":
    main()