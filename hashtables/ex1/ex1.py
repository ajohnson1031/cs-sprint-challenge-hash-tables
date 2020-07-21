def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    i = 0
       
    while i < length:
        cache[i] = weights[i]
        i+=1

    indexes = [n for n in cache.keys() if limit - cache[n] in cache.values()][::-1]
    
    return indexes if len(indexes) > 0 else None
