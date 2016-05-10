# Choose

several implementations of binomial coefficient
calculation: choose(n, k)

# Use Formula with Factorials

We can define choose k from n in terms of factorials. This implementation is
slow because factorial computation is time-consuming and it is really easy to
hit limit for integers or reach stackoverflow.

In Python if integer is too big - big integer is
used instead. Note that this will fail in R.

See `choose_factorial.py` and `test_choose_factorial.py`
for implementation and testing.

# Use Pascal Triangle Rule with Recursion

We can use Pascal rule and recursively compute combinations,
with pure recursive combination it is really easy to hit
maximum recursion depth.

The function has a wrapper function - common pattern for
functional programming. See `choose_triangle.py` for implementation.

We can use dynamic programming to achieve faster computation by either top down
or bottom up implementation. See `choose_triangle_topDown_DP.py` and
`choose_triangle_bottomUp_DP.py` for the code.

The test for these implementations can be found in `test_choose_triangle.py`.

# Testing

In bash:
```
py.test
```
Some of the tests are skipped, because they are too slow.

# Timing

We can compare impementation of Pascal rule:
```
python time_triangle_implementations.py
```
We frist compare all three implementations, after we also compare bottom up and
top down approach by generating more binomial coefficients.
