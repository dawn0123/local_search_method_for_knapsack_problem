# Local Search Method for Knapsack Problem

<p>
    <img src="./image.jpg" width=100%/>
</p>

### Problem Description

Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to given limit and the total value is as large as possible.

* _sample input_
```
values = [20, 5, 10, 40, 15, 25];
weights = [1, 2, 3, 8, 7, 4];
target = 10;
```
* _sample output_
```
60 (1 (20) + 8 (40) = 9 < 10)
```

### Algorithm

We employ single-bit complement moves and use the method of best improvement for neighbour selection to locally search the best fit.