def input_validator (start, end):
    while True :
        try :
            user_input = int(input('enter a number:'))
            if start <= user_input <= end :
                return user_input
            else :
                print(f'invalid input,please enter a number {start} and {end}')
                continue
        except ValueError:
            print('invalid input,please enter a number ')
            continue
if __name__ == '__main__':
    print (input_validator(1,10))