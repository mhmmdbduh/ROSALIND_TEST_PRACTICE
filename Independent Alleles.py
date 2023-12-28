"""

    Problem

Figure 2. The probability of each outcome for the sum of the values on two rolled dice (black and white), broken down depending on the number of pips showing on each die. You can verify that 18 of the 36 equally probable possibilities result in an odd sum.
Two events A
 and B
 are independent if Pr(A and B)
 is equal to Pr(A)×Pr(B)
. In other words, the events do not influence each other, so that we may simply calculate each of the individual probabilities separately and then multiply.

More generally, random variables X
 and Y
 are independent if whenever A
 and B
 are respective events for X
 and Y
, A
 and B
 are independent (i.e., Pr(A and B)=Pr(A)×Pr(B)
).

As an example of how helpful independence can be for calculating probabilities, let X
 and Y
 represent the numbers showing on two six-sided dice. Intuitively, the number of pips showing on one die should not affect the number showing on the other die. If we want to find the probability that X+Y
 is odd, then we don't need to draw a tree diagram and consider all possibilities. We simply first note that for X+Y
 to be odd, either X
 is even and Y
 is odd or X
 is odd and Y
 is even. In terms of probability, Pr(X+Y is odd)=Pr(X is even and Y is odd)+Pr(X is odd and Y is even)
. Using independence, this becomes [Pr(X is even)×Pr(Y is odd)]+[Pr(X is odd)×Pr(Y is even)]
, or (12)2+(12)2=12
. You can verify this result in Figure 2, which shows all 36 outcomes for rolling two dice.

Given: Two positive integers k
 (k≤7
) and N
 (N≤2k
). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least N
 Aa Bb organisms will belong to the k
-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.

"""

import sys
import math

def main():
    file_name = 'rosalind_lia.txt'
    with open(file_name, 'r') as file:
        k, N = file.read().strip().split(' ')
        k = int(k)
        N = int(N)
    print(k, N)
    print(independent_alleles(k, N))

def independent_alleles(k, N):
    """
    k: positive integer (k <= 7)
    N: positive integer (N <= 2^k)
    """
    p = 2**k
    q = 1 - p
    temp =  sum([binomial(p, i) * q**i * p**(p-i) for i in range(N)])
    print(temp)
    return 1 - temp

def binomial(N, k):
    return math.factorial(N) // (math.factorial(k) * math.factorial(N-k))

if __name__ == '__main__':
    main()