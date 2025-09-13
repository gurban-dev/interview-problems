'''
Original list:
2 4 7 9 1

1st pass: 2 4 7 1 9
# of comparisons: n - 1

2nd pass: 2 4 1 7 9
# of comparisons: n - 2

3rd pass: 2 1 4 7 9
# of comparisons: n - 3

4th pass: 1 2 4 7 9
# of comparisons: n - 4

Worst-case time complexity: O(n^2)

Each pass has fewer comparisons than the previous one.
'''