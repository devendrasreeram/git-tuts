while True:
    operator=input("enter a operator(+ - * / // % ** < > ):")
    if operator in ('+','-','*','/','**','//','%','<','>'):
            try:
                a=float(input("enter first value:"))
                b=float(input("enter second value:"))
            except ValueError:
                continue
            if operator=="+":
                result=a+b
                print("="*50)
                print(round(result))
            elif operator=="-":
                result=a-b
                print("="*50)
                print(round(result))
            elif operator=="*":
                result=a*b
                print("="*50)
                print(round(result))
            elif operator=="/":
                result=a/b
                print("="*50)
                print(result) 
            elif operator=="//":
                result=a//b
                print("="*50)
                print(result) 
            elif operator=="%":
                result=a%b
                print("="*50)
                print(result)
            elif operator=="**":
                result=a**b
                print("="*50)
                print(result)
            elif operator=="<":
                result=a<b
                print("="*50)
                print(result)
            elif operator==">":
                result=a>b
                print("="*50)
                print(result)
            print("="*50)
            operator=input("let's do another calculation(yes/no):" )
            if(operator=="no"):
                print("\tthanks for using....!")
                break        
    else:
                
        print(f"{operator} is a invalid operator")


