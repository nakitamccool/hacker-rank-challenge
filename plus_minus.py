def plusMinus(arr):
    # [pos, neg, zerp]
    counts = [0, 0, 0]
    for item in arr:
        if item > 0:
            counts[0] += 1
        elif item < 0:
            counts[1] += 1
        else:
            counts[2] += 1
    fractions = [0, 0, 0]
    for i in range(len(fractions)):
        fractions[i] = counts[i]/len(arr)
    return fractions
    
print(plusMinus([-4, 3, -9, 0, 4, 1]))
        
            