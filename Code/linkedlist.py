#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.num_nodes = 0  # number of Node objects in the list
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
           Running time: O(1) because the number of operations is constant.
        """
        return self.num_nodes

    def start_with_first_node(self, new_node):
        """Add the first node to the LinkedList.
           Param: new_node(Node): the node to be added
        """
        self.head = self.tail = new_node

    def append(self, item):
        """Insert the given item at the tail of this linked list.
           Running time: O(1) because either we have to make a new node to
           begin the list, or we go straight to the tail and add a new node.
           No matter the case, we know exactly where in the list we have to go.
        """
        new_node = Node(item)
        self.num_nodes += 1
        if self.is_empty() is True:
            self.start_with_first_node(new_node)
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
           Running time: O(1) because we always have to locate the head
           or we initialize it, which is one operation because head is always
           at the start of the list.
        """
        new_head = Node(item)
        if self.is_empty() is not True:
            old_head = self.head
            self.head = new_head
            self.head.next = old_head
        else:
            self.start_with_first_node(new_head)
        self.num_nodes += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
           Best case running time: O(1) because if we find the node that
           satisfies quality at self.head, then we exit after just
           one iteration.

           Worst case running time: O(n) because if no node matches with the
           given quality, then we will have to check every node in the list
           before completing this method.
        """
        node = self.head
        while node is not None:
            # this node matches
            if quality(node.data) is True:
                return node.data
            # this node does not match, move on to the next
            else:
                node = node.next
        # no matches in the list
        else:
            return None

    def data_is_inside(self, item):
        """Returns True if there is a Node in the list whose data reference
           is the given item.
        """
        return self.find(lambda data: data == item) == item

    def value_error(self, item):
        """Print the ValueError message."""
        raise ValueError(f'Item not found: {item}')

    def find_matching_node(self, item):
        """Returns a tuple, containing the node whose data reference matches
           the item. Also returns the node before it as well.
        """
        node = self.head
        node_before = None
        while not node.data == item:
            node_before = node
            node = node.next
        return tuple((node, node_before))

    def discover_item(self, item):
        '''Returns True if the item to be deleted is referenced by a Node,
           or raises ValueError.
        '''
        # discover if the data we are looking for exists in the list
        is_inside = self.data_is_inside(item)
        # item does not exist
        if is_inside is False:
            self.value_error(item)
        else:
            return is_inside

    def remove_tail(self, previous_node):
        """Helper for removing the last Node in the list."""
        previous_node.next = None
        self.tail = previous_node

    def remove_deleted_node(self, previous_node, node_being_deleted):
        """Helper for shifting the nodes so as to no longer point to the
           deleted node.
        """
        previous_node.next = node_being_deleted.next

    def remove_last(self):
        """Remove the head and tail from the list in one operation."""
        self.head = self.tail = None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
           Best case running time: O(1) because if we are deleting the head,
           then we do not go through any iterations in the while loop, because
           the node we examine starts out initialized to self.head.

           Worst case running time: O(n) because if the node is the tail, and
           the head and tail are separate, then we have to check every
           node in the list before we conclude that the tail contains item.
        """
        # discover if the data we are looking for exists in the list
        if self.discover_item(item) is True:
            # item does exist in the list
            self.num_nodes -= 1  # decrement the number of nodes
            # find the node with the data to delete
            node = self.find_matching_node(item)[0]
            node_before = self.find_matching_node(item)[1]
            # only one node left in the list
            if self.head.next is None:
                self.remove_last()
            # item to delete is the head of the list
            elif (self.head.data == node.data and
                  self.head.next == node.next):
                self.head = self.head.next
            # the node being deleted is the tail
            elif (self.tail.data == node.data and
                  self.tail.next == node.next):
                self.remove_tail(node_before)
            # shift the nodes left so they no longer include the deleted node
            else:
                self.remove_deleted_node(node_before, node)

    def replace(self, current_data, data_to_replace):
        """Find a Node object with a data reference equal to current_data, and
           then set that reference to data_to_replace instead.
           Raises ValueError otherwise.
        """
        if self.data_is_inside(current_data) is True:
            node = self.find_matching_node(current_data)[0]
            node.data = data_to_replace
        else:
            self.value_error(current_data)

    def __iter__(self):
        """
            Return a generator of the data referenced by the Nodes
            in this LinkedList.
        """
        node = self.head
        while node is not None:
            item = node.data
            node = node.next
            yield(item)


class DoublyLinkedList(LinkedList):
    def __repr__(self):
        """Return a string representation of this doubly linked list."""
        return 'DoublyLinkedList({!r})'.format(self.items())

    def append(self, item):
        """Insert the given item at the tail of this linked list.
           Initialize .previous attribute of Nodes as needed.
           Running time: O(1), for same reason as above in the
           append method in the LinkedList class.
        """
        new_node = Node(item)
        self.num_nodes += 1
        if self.is_empty() is True:
            self.start_with_first_node(new_node)
        elif self.num_nodes == 1:
            self.head.next = self.tail
            self.tail.previous = self.head
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this doubly linked list.
          Running time: O(1), for same reason as above in the
          prepend method in the LinkedList class.
        """
        new_head = Node(item)
        if self.is_empty() is not True:
            old_head = self.head
            new_head.next = old_head
            old_head.previous = new_head
            self.head = new_head
        else:
            self.start_with_first_node(new_head)
        self.num_nodes += 1

    def remove_the_node(self, node_to_delete, node_before):
        """Remove the node to be deleted, accounting for different scenarios
           of where the node is in the list.
        """
        # only one node left in the list
        if self.head.next is None:
            self.remove_last()
        # item to delete is the head of the list
        elif (self.head.data == node.data and
              self.head.next == node.next):
            self.head = self.head.next
            self.head.previous = None
        # the node being deleted is the tail
        elif (self.tail.data == node.data and
              self.tail.next == node.next):
            self.remove_tail(node_before)
        # shift the nodes left so they no longer include the deleted node
        else:
            self.remove_deleted_node(node_before, node)
            node_after = node.next
            node_after.previous = node_before

    def delete(self, item):
        """Delete the given item from this doubly linked list,
           or raise ValueError.
           Best and worst case running time same as the delete() method in the
           LinkedList class.
        """
        # discover if the data we are looking for exists in the list
        if self.discover_item(item) is True:
            # item does exist in the list
            self.num_nodes -= 1  # decrement the number of nodes
            # find the node with the data to delete
            node = self.find_matching_node(item)[0]
            node_before = self.find_matching_node(item)[1]
            self.remove_the_node(node, node_before)


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    # test_linked_list()
    ll = LinkedList(['A', 'B', 1, 5, 6.7777, ['Zain']])
    # number_of_nodes = ll.length()
    # print(f'Number of Nodes: {number_of_nodes}')
    # print(f'list: {ll}')
    print("Data in this LinkedList:")
    for item in ll:
        print(item)
