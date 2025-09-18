def find_max_sub_array(arr: list[int]) -> int:
  sum_of_max_subarray = arr[0]

  sum_of_curr_subarray = 0

  for num in arr:
    if sum_of_curr_subarray < 0:
      sum_of_curr_subarray = 0

    sum_of_curr_subarray += num

    sum_of_max_subarray = max(sum_of_curr_subarray, sum_of_max_subarray)

  return sum_of_max_subarray

print('find_max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]):',
      find_max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))