# Package-Delivery-Program

Section F:
F.  Justify the package delivery algorithm used in the solution as written in the original program by doing the following:
1.  Describe two or more strengths of the algorithm used in the solution.
-The nearest neighbor algorithm is simple to implement compared to other complex algorithms.
-The nearest neighbor algorithm is efficient.
-Near optimal algorithm.

2.  Verify that the algorithm used in the solution meets all requirements in the scenario.
-The algorithm used in my solution does meet all requirements for the scenario.

3.  Identify two other named algorithms that are different from the algorithm implemented in the solution and would meet all requirements in the scenario.
-Two other named algorithms include farthest insertion algorithm and greedy algorithm.

a.  Describe how both algorithms identified in part F3 are different from the algorithm used in the solution.
-Greedy algorithm first calculates all possible distances (edges) between any two address (vertices) and adds the shortest distance. This process repeats until a 
cycle containing all the locations is created. This is different from the nearest neighbor algorithm because the nearest neighbor only compares the distances from the current vertex to
all possible destination vertices.
-Farthest insertion algorithm is a type of insertion algorithm that adds new destinations in a delivery route as the number of destinations in the route grows. 
It first determines a destination that is the further from any one address already visited, and then it is placed between two destinations in the route that leads 
to the shortest possible delivery route. This is different from the nearest neighbor algorithm because nearest neighbor is sub-optimal and does not lead to the shortest route,
whereas the farthest insertion algorithm yields the shortest possible route under the algorithm's functionality.

Section G:
If I were to do the project different, I would like to use package destination address as the hash key to make use of the hash function of the HashMap. Despite not 
having to use packageID as the key, if I were to use the destination address as the key, then I could add Package objects with similar destination addresses into the
values of the key-value pairs. This would make it easy to identify those packages that can be delivered together. In addition, I would create a GUI to compliment the
program and built upon the CLI that is originally required.

Section H:
There are other data structures I can use other than HashMap. I could use a linked list and a binary search tree.

H1A. Describe how each data structure identified in H1 is different from the data structure used in the solution.

-Linked lists are similar to arrays, but instead make use of pointers to denote the next piece of data or node in the list. 
This allows the linked list data to be stored in memory at random. In contrast, HashMaps utilize storing data as key-value pairs. 
It is typically more efficient to retrieve a specific data point with a HashMap compared to a linked list. In addition, 
HashMap uses less memory than a linked list. Linked lists data structure has an O(1) time complexity for insertion and 
deletion at the beginning or end of the list, but it has an O(n) time complexity for any insertion, removal, or lookup function. 
In contrast, HashMap has a O(n) time complexity as worst-case, but does have an average time complexity of O(1).
-Binary search trees (BSTs) make use of a tree structure and has an ordering property. All values that are less than the 
node are placed to the left of three, whereas all values that are greater than the node are placed to the right of the tree. 
In contrast, the HashMap, as stated above, utilizes key-value pairs to store data. Data is retrieved by using the key to return the value.
In practice, searching through a binary search tree is efficient because the set of data that is being searched is continuously 
cut in half until the value is found, leading to an average time complexity of O(log n). In addition, insertion and deletion 
has an O(log n) time complexity on average. Despite this, the worst case scenario of a BST is O(n) if the BST is unbalanced. 
The time complexity again for a HashMap is O(n) time complexity as worst-case, but does have an average time complexity of O(1).