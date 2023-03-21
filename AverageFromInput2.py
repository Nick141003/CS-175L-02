#Nicholas Stevens
#CS 175L 02
# AverageFromInput
'''
def main():
    total = 0
    count = 0
    numbers_file = open('numbers.txt','r')
    for line in random_numbers_file:
        number = float(line)
        count += 1
        total += number
    average = total / count
    print("The average  of the numbers in 'numbers.txt' is:", format(average,'.2f'))           

main()
'''
def main():
    total = 0
    count = 0
    numbers_file = open('numbers.txt','r')
    for line in random_numbers_file:
        number = float(line)
        count += 1
        total += number
def calculate_average():
    average = total / count
def print_average_and_error_checking():
    print("The average  of the numbers in 'numbers.txt' is:", format(average,'.2f'))  
    except IOError:
        print('Error has occured')
    except ValueError:
        print('Error has occured')

main()

    
    
