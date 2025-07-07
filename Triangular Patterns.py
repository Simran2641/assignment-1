print("Lower Triangular Pattern:")
def lower_triangular(rows):
    for i in range(1, rows+1):
        print('* ' * i)

lower_triangular(5)

print("Upper Triangular Pattern:")
def upper_triangular(rows):
    for i in range(rows, 0, -1):
        print('* ' * i)

upper_triangular(5)

print("Pyramid Pattern:")
def pyramid(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '* ' * i)

pyramid(5)
