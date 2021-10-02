def main():
    #write your code below this line
    numbers = []
    numbers.append(3)
    numbers.append(2)
    numbers.append(6)
    numbers.append(-1)
    print(sum_list(numbers))

def sum_list(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

if __name__ == '__main__':
    main()
