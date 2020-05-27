# Treap
A treap data structure implementation in python. 
A Treap is a combination of a Binary Search Tree data structure, and a Max Heap data structure.
The Treap is made up of nodes that contain a key and a priority and is ordered like a BST in terms of its keys,
and ordered like a max heap in terms of its priorities. 
The keys can be a String, float, or int. The priority is a randomly generated priority based on the random.random function. 
By using a random priority, and by always mainting the heap priority, we are ensuring that there is a high probability
of maintaining the balanced binary tree, no matter how the keys are inserted. This allowed us to keep 
all the benefits of having a balanced binary tree.
