"""
HEAP DATA STRUCTURE
- A heap is a binary tree with two additional properties:\n
    1. Shape property: A heap is a complete binary tree, which means that all levels of the tree are fully filled except possibly for the last level, which is filled from left to right.
    2. Heap property: In a max heap, for any given node C, if P is a parent node of C, then the key (the value) of P is greater than or equal to the key of C. In a min heap, the key of P is less than or equal to the key of C.
- A heap can be represented as an array, where the root element is at index 0. For any given node at index i, its left child is at index 2i + 1 and its right child is at index 2i + 2.
- The parent of a node at index i is at index (i - 1) // 2.
- The height of a heap is O(log n).
- The time complexity of building a heap is O(n).
- The time complexity of inserting an element into a heap is O(log n).
- The time complexity of extracting the minimum or maximum element from a heap is O(log n).
- The time complexity of deleting an element from a heap is O(log n).
- The time complexity of heap sort is O(n log n).


"""