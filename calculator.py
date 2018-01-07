#author: Awaken prominence
#interpreter: Python3

#program to create calculator


#define welcome function
def welcome():
	print('''
welcome to calculator
*************************************
''')


#define calculate function
def calculate():
    operation=input('''
    please enter math operator to compute:
    + for addition
    - for substraction
    * for multiplication
    / for division
    Your Choice:
    ''')
    num1=int(input('Enter your first number:'))
    num2=int(input('Enter your second number:'))

	#addition
    if operation=='+':
        print('{}+{}='.format(num1,num2))
        print(num1+num2)

	#substraction
    elif operation=='-':
        print('{}-{}='.format(num1,num2))
        print(num1-num2)

	#multiplication
    elif operation=='*':
        print('{}*{}='.format(num1,num2))
        print(num1*num2)

	#division
    elif operation=='/':
        if(divideByZeroException(num2)):
            print('Divide By Zero Exeption')
        else:
            print('{}/{}='.format(num1,num2))
            print(num1/num2)

	#invalid entry
    else:
        print('Invalid Entry. please provide a valid choice..')


#define again() function to ask user to continue using calculator
def again():
	#take input from user
	again=input('''
Continue using Calculator?
please type Y for yes and N for no
''')

	#if 'Y' then run calculate function
	if again=='Y':
		calculate()

	#if 'N' then exit with proper message
	elif again=='N':
		print('Thanks for using calculator. See you again.')

	#invalid entry
	else:
		again()
	

#fuction that checks divide by zero exception
def divideByZeroException(y):
    if(y==0):
        return 1
    return 0
    
#function call
welcome()
calculate()
again()

