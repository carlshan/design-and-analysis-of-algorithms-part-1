# Week 3 Homework

## Optional Theory Problems

1. Prove that the worst-case expected running time of every randomized comparison-based sorting algorithm is  Ω(𝑛log𝑛) . (Here the worst-case is over inputs, and the expectation is over the random coin flips made by the algorithm.)

2. Suppose we modify the deterministic linear-time selection algorithm by grouping the elements into groups of 7, rather than groups of 5. (Use the "median-of-medians" as the pivot, as before.) Does the algorithm still run in  𝑂(𝑛)  time? What if we use groups of 3?

3. Given an array of  𝑛  distinct (but unsorted) elements  𝑥1,𝑥2,…,𝑥𝑛  with positive weights  𝑤1,𝑤2,…,𝑤𝑛  such that  ∑𝑛𝑖=1𝑤𝑖=𝑊 , a weighted median is an element  𝑥𝑘  for which the total weight of all elements with value less than  𝑥𝑘  (i.e.,  ∑𝑥𝑖<𝑥𝑘𝑤𝑖 ) is at most  𝑊/2 , and also the total weight of elements with value larger than  𝑥𝑘  (i.e.,  ∑𝑥𝑖>𝑥𝑘𝑤𝑖 ) is at most  𝑊/2 . Observe that there are at most two weighted medians. Show how to compute all weighted medians in  𝑂(𝑛)  worst-case time.

4. We showed in an optional video lecture that every undirected graph has only polynomially (in the number  𝑛  of vertices) different minimum cuts. Is this also true for directed graphs? Prove it or give a counterexample.

5. For a parameter  𝛼≥1 , an  𝛼 -minimum cut is one for which the number of crossing edges is at most  𝛼  times that of a minimum cut. How many  𝛼 -minimum cuts can an undirected graph have, as a function of  𝛼  and the number  𝑛  of vertices? Prove the best upper bound that you can.
