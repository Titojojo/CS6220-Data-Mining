def cardinality_items(filename):
    '''
    Takes a filename "*.csv" and returns an integer representing the number of unique items in the collection.
    '''
    unique_items = set()
    
    with open(filename, 'r') as file:
        for line in file:
            items = line.strip().split(',')
            for item in items:
                unique_items.add(item.strip())
    
    return len(unique_items)

res = cardinality_items("basket_data.csv")
print("The cardinality is:", res)
