# Accept 2 number from user and return Division
#Input : 10   5
#Output : 2

def Division(No1 , No2):
    if No2 > No1:
        return 
        
    result = No1 / No2
    return result

def main():
    print("Enter first number")
    value1 = int(input())
    
    print("Enter second number")
    value2 = int(input())
    

    ret = Division(value1,value2)
    print("Division is : ",ret)

if __name__=="__main__":
    main()