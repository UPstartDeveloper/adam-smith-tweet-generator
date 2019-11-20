#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        '''Initialize this hash table with the given initial size.'''
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        '''Return a formatted string representation of this hash table.'''
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        '''Return a string representation of this hash table.'''
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        '''Return the bucket index where the given key would be stored.'''
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
           Running time: O(n^2)
           This is because we require a traversal not only of the list of the
           buckets, but of the list representing the data of the Nodes in each
           bucket (a LinkedList object).

        """
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
           Running time: O(n^2)
           Same reason as for the keys() method.
           In both of these methods, the best running time is traversing
           through a HashTable where the buckets contain Nodes pointing to
           non-primitive data types (not lists, tuples, dictionaries, etc).
           Otherwise, the running time would become O(n^3).

        """
        # Collect all values in each bucket
        all_values = list()
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
           Running time: O(n^2)
           The method itself only requires traversal of the buckets list, but
           because it invokes the LinkedList.items() method, there is also the
           hidden cost of having to traverse through the Nodes in each bucket.
           Therefore in all cases as the number of buckets, or the number of
           Nodes in each bucket increases, the running time of the method
           increases in quadratic time.

        """
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
           Running time: O(n)
           This method returns an acculmulator variable, num_entries. In order
           to calculate num_entries, we requires a traversal of all the
           LinkedLists in self.buckets, which will run in linear time.

        """
        num_entries = 0
        for bucket in self.buckets:
            num_entries += bucket.num_nodes
        return num_entries

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
           Running time: O(n^2)
           The method requires a traversal of the buckets, and a traversal of
           the nodes in each bucket using the LinkedList.items() method.

           In the best case, the item we are looking for exists at a head node.
           In this scenario, the HashTable.contains() method would only take
           O(n) time, because now we only depend on traversing through the
           buckets until we find the one whose head node contains the key.

           On average, the HashTable.contains() method will still take O(n^2)
           running time, because in as number of buckets (and the number of
           Nodes in each bucket) increases, then we will most likely have to
           search multiple Nodes in a bucket to find if it contains the key.

           In the worst case, the key does not exist and we need O(n^2) running
           time because we traverse all Nodes in all the buckets of the
           HashTable instance.

        """
        for bucket in self.buckets:
            # Check if key-value entry exists in bucket
            item_from_bucket = bucket.find(lambda data: data[0] == key)
            if item_from_bucket is not None and item_from_bucket[0] == key:
                return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
           Running time: O(n^2)
           In the best case, the key cannot be retrieved from the HashTable,
           and this method raises the KeyError. To do this the method itself
           run in constant, however the hidden cost of using the
           HashTable.contains() method adds on O(n^2).

           As the number of buckets and the size of each bucket increases, the
           worst and the average case will both require O(n^2). This is because
           to find the value associated with an existing key in the list, we
           first require a quadratic traversal to discover that the key exists,
           and then another to discover in which Node of which bucket the key
           value pair are together.

        """
        # determine if key exists
        if self.contains(key) is False:
            raise KeyError(f'Key not found: {key}')
        else:
            # Find bucket where given key belongs
            for bucket in self.buckets:
                # Check if key-value entry exists in bucket
                for key_in_bucket, value in bucket.items():
                    # If found, return value associated with given key
                    if key == key_in_bucket:
                        return value

    def get_bucket_containing_key(self, key):
        '''Return the bucket(LinkedList) whose Nodes reference the key.'''
        index = index = self._bucket_index(key)
        return self.buckets[index]

    def set(self, key, value):
        """Insert or update the given key with its associated value.
           Running time: O(n)
           This is because the method's runtime increases asymptotically
           only with respect to the length of the bucket it has to traverse
           over. This is because the step before, finding the bucket the key
           belongs in takes constant time, since it uses the _bucket_index
           helper method.

           Even in the worst case, when the key is not yet in the bucket,
           the method will only take O(n) to decide it needs to append
           a new key value pair to the bucket, where n is the number of
           nodes in that LinkedList object. This is because at the point where
           the method has traversed through all current nodes in the
           LinkedList, it already knows not to check any of the other buckets.

        """
        new_pair = (key, value)
        # Find bucket where given key belongs
        bucket = self.get_bucket_containing_key(key)
        # Try to update an exisiting key value pair
        try:
            current_value = self.get(key)
            # update an existing key value pair
            current_pair = (key, current_value)
            bucket.replace(current_pair, new_pair)
        except KeyError:
            # insert the key value pair
            bucket.append(new_pair)

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
           Running time: O(n^2)
           The methods runs in quadratic time because of using the get method
           in the beginning to check if the key-value entry already exists in
           the HashTable.

           The runtime of this step overturns the runtime of all the other
           operations in this method. That said, there may still  be a notable
           difference between the best and worst case scenarios.

           In the best case, the key value entry is
           referenced by the head node of the bucket, in which case deleting
           the node requires constant time. Alternatively, the key value
           entry may not even exist.

           In the worst case, the node to delete is at the tail node of the
           bucket, which then requires O(n) time to delete, where n is the
           number of nodes in the bucket.

        """
        # Check if key-value entry exists in bucket
        value = self.get(key)
        if value is not KeyError:
            # Find bucket where given key belongs
            bucket = self.get_bucket_containing_key(key)
            kv_pair = (key, value)
            bucket.delete(kv_pair)
        else:
            # Otherwise, raise error to tell user delete failed
            raise KeyError(f'Key not found: {key}')

    def __iter__(self):
        '''Returns HashTable as an iterable.'''
        return iter(self.items())

    def __getitem__(self, key):
        """Return a value encapsulated anywhere in this object.
           Subscripting syntax enabled.

           Parameters:
           key(str, tuple, int, or float): the data that gets hashed to
                be stored in the HashTable

           Returns:
           (any type of object): the data associated with the key

        """
        return self.get(key)

    def __setitem__(self, key, value):
        """Set a key-value pair. Implements subscripting syntax.

           Parameters:
           key(str, tuple, int, or float): the data that gets hashed to
                be stored in the HashTable

           Returns:
           (any type of object): the data associated with the key

        """
        return self.set(key, value)

    def __iter__(self):
        '''Return a list of the keys.'''
        return self.keys()

    def __contains__(self, key):
        '''Returns True or False based on the key in the HashTable or not.'''
        return key in self.keys()

    def __delitem__(self, key):
        '''Delete a key value pair from the HashTable given the key.'''
        self.delete(key)


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    # test_hash_table()
    ht = HashTable()
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        ht.set(key, value)
    for key, value in ht:
        print(key, value)
