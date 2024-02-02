class multifunctions():
    def OddEven():
        a=int(input("Enter a number :"))
        if (a%2)==0:
            print(a, "is a even number")
            message=(a,"is a even number")
        else:
            print("odd")
            message="odd"
        return message
    def triangle():
        H=int(input("HEIGHT :"))
        B=int(input("BREADTH :"))
        AREA =int(0.5*H*B)
        print("AREA OF TRIANGE = ",AREA) 
        Height1=int(input("Height1 ="))
        Height2=int(input("Height2 ="))
        Breadth=int(input("Height1 ="))
        PERI=Height1+Height2+Breadth
        print("PERIMETER OF TRIANGLE IS :", PERI)
        return PERI
    def FindPercent():    
        S1=int(input("Subject1="))
        S2=int(input("Subject2="))
        S3=int(input("Subject3="))
        S4=int(input("Subject4="))
        S5=int(input("Subject5="))    
        TOTAL=int(S1+S2+S3+S4+S5)
        PERCENT=float(TOTAL/5)
        print(TOTAL)
        print(PERCENT)
        return PERCENT