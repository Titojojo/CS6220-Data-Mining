def all_itemsets(item_list, k):
    """
    Takes a list of unique items and an integer k, 
    return a list of all possible unique itemsets with non-repeating k items.
    """
    res = []
    n = len(item_list)

    def backtrack(comb, idx, remaining):
        if remaining == 0:
            res.append(comb[:])
        else:
            for i in range(idx, n):
                comb.append(item_list[i])
                backtrack(comb, i + 1, remaining - 1)
                comb.pop()
    
    backtrack([], 0, k)
    return res