#Simple calculator Krish Patil
for _ in range(10):
    match (int(input(f"1. +\n2. -\n3. x\n4. /\n5. %\n6. min\n7. mx\nEnter serial number of operation to perform (1,..7): "))) :
        case 1: 
            print()
            def add(*nums):
                m_ans=0
                for i in nums:
                    m_ans+=i
                print("Answer : "+str(m_ans))
            nos=[]
            for i in range(int(input("Enter number of operands : "))):
                nos.append(int(input(f"Enter a number/value : ")))
            add(*nos)
            print()
        case 2:
            print()
            def sub(*nums):
                m_ans=nums[0]
                for i in nums[1:]:
                    m_ans-=i
                print("Answer : "+str(m_ans))
            nos=[]
            for i in range(int(input("Enter number of operands : "))):
                nos.append(int(input(f"Enter a number/value : ")))
            sub(*nos)
            print()
        case 3:
            print()
            def mul(*nums):
                m_ans=nums[0]
                for i in nums[1:]:
                    m_ans*=i
                print("Answer : "+str(m_ans))
            nos=[]
            for i in range(int(input("Enter number of operands : "))):
                nos.append(int(input(f"Enter a number/value : ")))
            mul(*nos)
            print()
        case 4:
            print()
            div = lambda n,n2: n/n2
            print("Answer : " +  str(div(int(input(f"Divide : ")),int(input(f"by : ")))))
            print()
        case 5:
            print()
            perc = lambda n,n2: n%n2
            print("Answer : " +  str(perc(int(input(f"Enter a number : ")),int(input(f"Enter another number : ")))))
            print()
        case 6:
            print()
            f_min = lambda n,n2: n2 if n>n2 else n
            print("Answer : " +  str(f_min(int(input(f"Enter a number : ")),int(input(f"Enter another number : ")))))
            print()
        case 7:
            print()
            f_max = lambda n,n2: n if n>n2 else n2
            print("Answer : " +  str(f_max(int(input(f"Enter a number : ")),int(input(f"Enter another number : ")))))
            print()
        case _:
            print()
            print("Wrong Choice, Try Again!") # default acse that will print on out of index input
            print()