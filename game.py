class Multiple_choice:
        def __init__(self):
                print("WELCOME")
                print('''
                      press one of the following choices.
                      1 :if you wanna enter a num and know if it is odd num or even
                      2 :get the odd or even numbers from 0 to whatever you want
                      3 :Put a number to print all the numbers that are divisible by this number from[1-10]
                      ''')
                user_choice=int(input("Enter your choice num: "))
                if user_choice==1:
                        self.odd_even()
                elif user_choice==2:
                        self.multi_odd_even()

                elif user_choice==3:
                        self.division()
                else:
                        print("Enter a vaild choice")

        def odd_even(self):
                while True:
                        i=int(input("Enter a number: "))
                        if i % 2 !=0:
                                print(i,"عدد فردي")
                        else:
                                print(i,"عدد زوجي")
        def multi_odd_even(self):
                print('''
                      اذا كنت تريد ارقام فردية ادخل رقم واحد واذا كنت تريد ارقام زوجية ادخل اتنين
                      ''')
                get_value=int(input("Enter a value: "))
                get_number=int(input("enter a number: "))
                if get_value==1:
                        for number in range(get_number):
                                if number % 2 !=0:
                                        print(number)
                elif get_value==2:
                        for number in range(get_number):
                                if number % 2 ==0:
                                        print(number)
        def division(self):
                get=input("enter a number :")
                for i in range(10):
                    if not i % int(get):
                        print(i)
m=Multiple_choice()
