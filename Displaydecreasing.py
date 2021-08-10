# Accep number from user and Display decreasing order from that number.
# input : 5
# output : 5  4   3  2   1
def Display(no):
    for i in range(no,0,-1):
        print(i)


def main():
    print("Enter the number")
    value1 = int(input())
    Display(value1)
    
if __name__=="__main__":
    main()