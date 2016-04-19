# Choose

several implementations of binomial coefficient
calculation: choose(n, k)

# Use Formula with Factorials

We can define choose k from n in terms of
factorials. This implementation is slow because
factorial computation is time-consuming and it is
really easy to hit limit for integers.

In Python if integer is too big - big integer is
used instead. Note that this will fail in R.

# Use Pascal Triangle Rule with Recursion

We can use Pascal rule and recursively compute combinations,
with pure recursive combination it is really easy to hit
maximum recursion depth.

The function has a wrapper function - common pattern for
functional programming.
