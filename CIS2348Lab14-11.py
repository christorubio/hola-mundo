#Chris Rubio
#1530668

def selection_sort_descend_trace(numbers):
    for i in range(len(numbers)-1):
        index = i
        for j in range(i + 1, len(numbers)):
            if numbers[index] < numbers[j]:
                index = j
        numbers[i], numbers[index] = numbers[index], numbers[i]
        for x in numbers:
            print(x,end=" ")
        print()
    return numbers

if __name__ == "__main__":
    numbers = [int(x) for x in input("").split()]
    selection_sort_descend_trace(numbers)
