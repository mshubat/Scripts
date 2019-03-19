'''
The following code finds the largest hour glass present in a 6x6
Matrix (whose values fall between -9 to 9 inclusive) and prints
out its sum.

Where an hourglass is defined as the following shape:

2 2 2   OR   1 5 6   OR   7 0 7   OR   -1 -2 -3
  2            2            2             -4
2 2 2        4 4 4        9 1 1        -5 -6 -7

INPUT:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Contains Hourglass's
1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0

Hourglass with the maximum sum (19) is:

2 4 4
  2
1 2 4
'''


def biggest_hourglass(matrix):
    largest_sum = -10000
    temp_sum = 0
    if matrix == None:
        return 0
    for row in range(4):
        for col in range(4):
            temp_sum = 0

            temp_sum += sum(matrix[row][col:col+3])
            temp_sum += matrix[row+1][col+1]
            temp_sum += sum(matrix[row+2][col:col+3])

            if temp_sum > largest_sum:
                largest_sum = temp_sum

    print(largest_sum)


if __name__ == '__main__':
    arr = [[-1, -1, 0, -9, -2, -2],
           [-2, -1, -6, -8, -2, -5],
           [-1, -1, -1, -2, -3, -4],
           [-1, -9, -2, -4, -4, -5],
           [-7, -3, -3, -2, -9, -9],
           [-1, -3, -1, -2, -4, -5]]

    # for _ in range(6):
    #    arr.append(list(map(int, input().rstrip().split())))

    biggest_hourglass(arr)

'''
Basic Matrix Access
== == == == == == == == == == == == ==
'''
matrix = [[-1, -1, 0, -9, -2, -2],
          [-2, -1, -6, -8, -2, -5],
          [-1, -1, -1, -2, -3, -4],
          [-1, -9, -2, -4, -4, -5],
          [-7, -3, -3, -2, -9, -9],
          [-1, -3, -1, -2, -4, -5]]


# Print the Matrix to stdout
for row in matrix:
    for i in range(len(row)):
        print("{} ".format(row[i]), end="")
    print("")

temp_sum = 0
temp_sum += sum(matrix[0][0:3])
temp_sum += matrix[1][1]
temp_sum += sum(matrix[2][0:3])

print(-20 > -19)
print(temp_sum)
print(sum(matrix[0][0:3])+matrix[1][1]+sum(matrix[2][0:3]))
