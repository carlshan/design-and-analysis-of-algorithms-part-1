# Week 2

## Theory
### Question 1
Give the best upper bound that you can on the solution to the following recurrence:  $𝑇(1)=1$  and  $𝑇(𝑛) ≤ 𝑇(floor(\sqrt{n})) + 1$  for  $𝑛>1$.
(Here [x] denotes the "floor" function, which rounds down to the nearest integer.)

**Answer:** Using the "Master Method", it would seem $a=1$, $d=0$ and $b$ is varies depending on $n$. However, despite $b$ not being a constant, this would put us in Case 1 and ergo
$O(N^0 * (log(N))$, which would be $O(log(N))$.

### Question 2
You are given an n by n grid of distinct numbers. A number is a local minimum if it is smaller than all of its neighbors.
(A neighbor of a number is one immediately above, below, to the left, or the right. Most numbers have four neighbors; numbers on the side have three; the four corners have two.)
Use the divide-and-conquer algorithm design paradigm to compute a local minimum with only $O(n)$ comparisons between pairs of numbers.
(Note: since there are  𝑛2  numbers in the input, you cannot afford to look at all of them.
Hint: Think about what types of recurrences would give you the desired upper bound.)

**Answer**: Using the Master Method we would have to be in Case 2, where $a < b^d$ and $d=1$. This also implies that $b>1$ and $a<b$.

## Programming
The file contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order.
The integer in the  𝑖𝑡ℎ  row of the file gives you the  𝑖𝑡ℎ  entry of an input array.

Your task is to compute the total number of comparisons used to sort the given input file by QuickSort.
As you know, the number of comparisons depends on which elements are chosen as pivots, so we'll ask you to explore three different pivoting rules.

You should not count comparisons one-by-one. Rather, when there is a recursive call on a subarray of length  𝑚 , you should simply add  𝑚−1  to your
running total of comparisons.

(This is because the pivot element is compared to each of the other  𝑚−1  elements in the subarray in this recursive call.)

WARNING: The Partition subroutine can be implemented in several different ways, and different implementations can give you differing numbers of comparisons.

For this problem, you should implement the Partition subroutine exactly as it is described in the video lectures (otherwise you might get the wrong answer).

Part 1: For the first part of the programming assignment, you should always use the first element of the array as the pivot element.

Part 2: Compute the number of comparisons (as in Problem 1), always using the final element of the given array as the pivot element. Again, be sure to implement the Partition subroutine exactly as it is described in the video lectures.

Recall from the lectures that, just before the main Partition subroutine, you should exchange the pivot element (i.e., the last element) with the first element.

Part 3: Compute the number of comparisons (as in Problem 1), using the "median-of-three" pivot rule. [The primary motivation behind this rule is to do a little bit of extra work to get much better performance on input arrays that are nearly sorted or reverse sorted.] In more detail, you should choose the pivot as follows. Consider the first, middle, and final elements of the given array. (If the array has odd length it should be clear what the "middle" element is; for an array with even length  2𝑘 , use the  𝑘𝑡ℎ  element as the "middle" element. So for the array 4 5 6 7, the "middle" element is the second one ---- 5 and not 6!) Identify which of these three elements is the median (i.e., the one whose value is in between the other two), and use this as your pivot. As discussed in the first and second parts of this programming assignment, be sure to implement Partition exactly as described in the video lectures (including exchanging the pivot element with the first element just before the main Partition subroutine).

EXAMPLE: For the input array 8 2 4 5 7 1 you would consider the first (8), middle (4), and last (1) elements; since 4 is the median of the set {1,4,8}, you would use 4 as your pivot element.

SUBTLE POINT: A careful analysis would keep track of the comparisons made in identifying the median of the three candidate elements. You should NOT do this. That is, as in the previous two problems, you should simply add  𝑚−1  to your running total of comparisons every time you recurse on a subarray with length  𝑚 .


