def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    hashtable = {}
    i = 0
    holder_array = []
    
    
    while i < len(arrays):
        for j in arrays[i]:
            if j not in hashtable:
                hashtable[j] = 0
            else:
                hashtable[j] += 1
        i+=1  
    
    result = [n for n in hashtable.keys() if hashtable[n] >= 1]
    
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
