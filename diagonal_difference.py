def diagonalDifference(arr):
    diagonal_left_to_right = 0
    diagonal_right_to_left = 0
    for i in range(len(arr)):
        diagonal_left_to_right += arr[i][i]
        diagonal_right_to_left += arr[i][len(arr)-1-i]
    difference = diagonal_left_to_right - diagonal_right_to_left
    if difference < 0:
        difference = difference * -1
    return difference
    
print(diagonalDifference([
    [11, 2, 4], 
    [4, 5, 6], 
    [10, 8, -12]
]))