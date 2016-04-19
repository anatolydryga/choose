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
