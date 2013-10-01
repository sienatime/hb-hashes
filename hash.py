# implement the following functions for a hash table:

# insert(h, key, value)
# get(h, key)
#     return value

table_size = 100

def hash_insert(h, key, value):
    hash_index = hash(key) % table_size

    list_of_values = h[hash_index]

    #if key is already there, replace it with new value
    for tuples in list_of_values:
        if key == tuples[0]:
            list_of_values.remove(tuples)
    
    list_of_values.append( (key, value) )

def hash_get(h, key):
    hash_index = hash(key) % table_size

    for tuples in h[hash_index]:
        if key == tuples[0]:
            return tuples[1]

def main():
    # do stuff

    hash_table = []

    # NOTE: hash_table = [[]] * table_size will make each empty list point to the same object so don't do it.
    for i in range(table_size):
        hash_table.append([])

    hash_insert(hash_table, 1, "one")
    hash_insert(hash_table, 10, "ten")
    hash_insert(hash_table, "some key","some value")
    #print "hash_table:", hash_table
    print "get key 10:", hash_get(hash_table, 10)
    print "get some key:", hash_get(hash_table, "some key")
    hash_insert(hash_table, "some key","another value")
    print "get some key:", hash_get(hash_table, "some key") 

main()