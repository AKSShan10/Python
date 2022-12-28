# num1 = input('Emter a number: ')
#
# try:
#     num = int(num1)
#
# except ValueError:
#     print(num, 'was not a valid number.')
#
# except Exception as e:
#     print('Exception was caught')
#     print(type(e))
#     num = 'Unknown'
#
# print(num)


num1 = input('Emter a number: ')
num2 = input('Emter a second number: ')

try:
    num = int(num1)
    num2 = int(num2)
    total = num/num2

except ValueError:
    print('Num or num2 were not a valid number.')

except ZeroDivisionError:
    print('Numbers could not be divided.')

except Exception as e:
    print('Exception was caught')
    print(type(e))
    num = 'Unknown'

print(num)