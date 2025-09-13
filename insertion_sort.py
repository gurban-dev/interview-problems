def insertion_sort(arr):
  for i in range(1, len(arr)):
    # 1st iteration:
    # current = 2
    current = arr[i]

    # j will be used to access the elements that
    # precede the current one.

    # 1st iteration:
    # j = 0
    j = i - 1

    # Move each of the preceding elements to the right
    # so that the current element can be inserted in
    # the appropriate position.

    # 1st iteration:
    # while j >= 0 and arr[0] > 2:
    while j >= 0 and arr[j] > current:
      # 1st iteration:
      # arr[1] = 5
      arr[j + 1] = arr[j]

      # 1st iteration:
      # j = -1
      j -= 1
    
    # 1st iteration:
    # arr[0] = 2
    arr[j + 1] = current

  # 1st iteration:
  # arr = [2, 5, 4, 6, 1, 3]

  return arr

# Example
arr = [5, 2, 4, 6, 1, 3]

print('insertion_sort(arr):', insertion_sort(arr))