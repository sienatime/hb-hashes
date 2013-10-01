# implement the following functions for a hash table:

# insert(h, key, value)
# get(h, key)
#     return value

# where h is a list

# start with a hash table size of 100 (so mod hash value by 100 to get bucket)

# python has a hash() function

keys_values = []

def hash_insert(h, key, value):

    keys_values.append( (key,value) )

    hash_index = hash(key) % 1

    if h[hash_index] == []:
        h[hash_index] = [value]
    else: 
        h[hash_index].append(value)

def hash_get(h, key):
    hash_index = hash(key) % 1

    thelist = h[hash_index]
    return thelist
    #return keys_values
    # how do we get the right value using keys_values???

def main():
    # do stuff

    hash_table = [[]] * 100

    hash_insert(hash_table, 1, "one")

    #keep list of tuples that is key, value

    print hash_table

    hash_insert(hash_table, 10, "ten")

    print hash_table

    print hash_get(hash_table, 1)

main()