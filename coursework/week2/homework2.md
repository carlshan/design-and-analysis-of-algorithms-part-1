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