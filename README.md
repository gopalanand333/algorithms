# Algorithms
An algorithm is a step by step method of solving a problem. It is commonly used for data processing, calculation and other related computer and mathematical operations.
An algorithm is also used to manipulate data in various ways, such as inserting a new data item, searching for a particular item or sorting an item.

## Algoritm Comlexity
- Space complexity: How much memory does it require?
- Time comlexity: How much time does it require to complete?
### algoritm have a set of input and output values

# Algorithm classification 
- Serial/Parallel
- Exact/approximate 
- Deterministic/non-deterministic

# Some common alogorithms
- Search algorithms 
- Sorting algorithms
- Computational algorithms
- Collection algorithms

### Example: greatest common denominator )GCD of two integers
eg: GCD of 20 and 8 is 8 and 1
`
def gcd(a,b):
    while (b !=0):
        t = b
        b = t % b
    return a
print(gcd(10,20))
`

# Algorithm performance
- Measure how an algorithm responds to dataset size
# Big-O notation
- Classifies performance as the input size grows
- "O" indicates the order of operation: Time Scale to perform an operation
-  Many algo have more than one big O values.
## Common Big-O Terms
- O(1) Constant Time (looking up single element in array)
- O(log n) - Lograthmic (finding an item in a sorted array with binary search)
- O(n)- Linear time (searching in an unsorted array)
- O (n log n)- Log-linear (Complex sorting alogs like heap and merge sort)
- o(n^2)- Quadratic (bubble sort, selection sort)


