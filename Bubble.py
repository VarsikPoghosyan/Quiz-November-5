class Node():

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

def bubble_sort(array):
    length = len(array)
    for i in range(length-1):
        swapped = False
        for j in range(length (1-i)):
            if array[j] > array[j+1]:
                swapped = True
                array[j], array[j+1] = array[j+1], array[j]
        if not swapped: break
    return array

if __name__ == '__main__':

        raw_input = input
    user_input = raw_input('Enter numbers:').strip()
    unsorted = [int(item) for item in user_input.split(',')]
