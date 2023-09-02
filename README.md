# Package-Delivery-Program

https://www.youtube.com/watch?v=9HFbhPscPU0 used for Hash Table functions

Section F:
F.  Justify the package delivery algorithm used in the solution as written in the original program by doing the following:
1.  Describe two or more strengths of the algorithm used in the solution.
-The nearest neighbor algorithm is simple to implement compared to other complex algorithms.
-The nearest neighbor algorithm is suitable for non-linear and random data such as determining the next shortest distance out of remaining distances.

2.  Verify that the algorithm used in the solution meets all requirements in the scenario.
-The algorithm used in my solution does meet all requirements for the scenario.

3.  Identify two other named algorithms that are different from the algorithm implemented in the solution and would meet all requirements in the scenario.
-Two other named algorithms include Dijkstra's algorithm and greedy algorithm.

a.  Describe how both algorithms identified in part F3 are different from the algorithm used in the solution.
Greedy algorithm takes into account the most optimal solution at a certain point in time, but may not lead to the most optimal path.
Dijkstra's algorithm starts at an initial vertex, then finds the shortest path to the next vertex, and keeps repeating until it reaches the final vertex. 
In addition, a pointer to the previous vertex is taken. The algorithm terminates once all the vertices are visited.


Section G:
If I were to do the project different, I would like to use package destination address as the hash key to make use of the hash function of the HashMap. Despite not 
having to use packageID as the key, if I were to use the destination address as the key, then I could add Package objects with similar destination addresses into the
values of the key-value pairs. This would make it easy to identify those packages that can be delivered together. In addition, I would create a GUI to compliment the
program and built upon the CLI that is originally required.

H. There are other data structures I can use other than HashMap. I could use a linked list and a binary search tree.
Linked lists are similar to arrays, but instead make use of pointers to denote the next piece of data that is accessed. Unlike arrays, linked lists can be in random order
in memory. This data structure has an O(n) time complexity.
Binary search trees make use of a tree structure and has an ordering property. All values that are less than the node are placed to the left of three, whereas all values that are greater
than the node are placed to the right of the tree. In practice, searching through a binary search tree is efficient because the set of data that is being searched is 
continuously cut in half until the value is found, therefore has an O(log n) time complexity.