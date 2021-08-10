# Accept number from user and display below pattern.
# input : 5
# output : *	*	*	*	*  

def DisplayPattern(no):
	for i in range(0,no):
		print("*",end = ' ')
        
def main():
    print("Enter the number")
    value = int(input())
    print("--------------------------------")
    DisplayPattern(value)
    print("\n--------------------------------\n")

if __name__=="__main__":
    main()