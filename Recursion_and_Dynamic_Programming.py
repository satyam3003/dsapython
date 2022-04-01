"""
QUESTION 1: Write a function to find the length of the longest common subsequence between two sequences. E.g. Given the strings "serendipitous" and "precipitation", the longest common subsequence is "reipito" and its length is 7.

A "sequence" is a group of items with a deterministic ordering. Lists, tuples and ranges are some common sequence types in Python.

A "subsequence" is a sequence obtained by deleting zero or more elements from another sequence. For example, "edpt" is a subsequence of "serendipitous".
"""
import time

T0 = {
    'input': {
        'seq1': 'serendipitous',
        'seq2': 'precipitation'
    },
    'output': 7
}

T1 = {
    'input': {
        'seq1': [1, 3, 5, 6, 7, 2, 5, 2, 3],
        'seq2': [6, 2, 4, 7, 1, 5, 6, 2, 3]
    },
    'output': 5
}

T2 = {
    'input': {
        'seq1': 'longest',
        'seq2': 'stone'
    },
    'output': 3
}

T3 = {
    'input': {
        'seq1': 'asdfwevad',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
}

T4 = {
    'input': {
        'seq1': 'dense',
        'seq2': 'condensed'
    },
    'output': 5
}

T5 = {
    'input': {
        'seq1': '',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
}

T6 = {
    'input': {
        'seq1': '',
        'seq2': ''
    },
    'output': 0
}

T7 = {
    'input': {
        'seq1': 'abcdef',
        'seq2': 'badcfe'
    },
    'output': 3
}

lcq_tests = [T0, T1, T2, T3, T4, T5, T6, T7]


def lcs_recursion(seq1, seq2, idx1=0, idx2=0):
    if len(seq1) == idx1 or len(seq2) == idx2:
        return 0
    elif seq1[idx1] == seq2[idx2]:
        return 1 + lcs_recursion(seq1, seq2, idx1 + 1, idx2 + 1)
    else:
        option1 = lcs_recursion(seq1, seq2, idx1 + 1, idx2)
        option2 = lcs_recursion(seq1, seq2, idx1, idx2 + 1)
        return max(option1, option2)


for lcq in lcq_tests:
    print(lcs_recursion(**lcq['input']) == lcq['output'])

"""
Time complexity of this becomes O(2^m*n)
"""


# memoization approach

def lac_memo(seq1, seq2):
    memo = {}

    def recursion(idx1=0, idx2=0):
        key = (idx1, idx2)
        if key in memo:
            return memo[key]
        elif len(seq1) == idx1 or len(seq2) == idx2:
            memo[key] = 0
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recursion(idx1 + 1, idx2 + 1)
        else:
            memo[key] = max(recursion(idx1 + 1, idx2), recursion(idx1, idx2 + 1))
        return memo[key]

    return recursion()


print("\n\nmemoization:")
for lcq in lcq_tests:
    print(lac_memo(**lcq['input']) == lcq['output'])

"""
Time complexity of this becomes O(m*n)
"""


# dynamic programming approach
def lac_dynamic(seq1, seq2):
    n1, n2 = len(seq1), len(seq2)
    table = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    for i in range(n1):
        for j in range(n2):
            if seq1[i] == seq2[j]:
                table[i + 1][j + 1] = 1 + table[i][j]
            else:
                table[i + 1][j + 1] = max(table[i + 1][j], table[i][j + 1])
    return table[-1][-1]


print("\n\ndynamic programming:")
for lcq in lcq_tests:
    print(lac_dynamic(**lcq['input']) == lcq['output'])

"""
Time complexity of this becomes O(m*n)
"""


# todo: fibonacci sequence

# 1. recursion

def fib_recursion(n):
    if n < 2:
        return n
    else:
        return fib_recursion(n - 1) + fib_recursion(n - 2)


print(fib_recursion(10))
"""This method is basic most solution but its time complexity is very high"""


# 2. memoization

def fib_memo(n):
    memo = [None] * (n + 1)

    # print(memo)
    def memo_f(n):
        if memo[n] is not None:
            return memo[n]
        elif n < 2:
            memo[n] = n
        else:
            memo[n] = memo_f(n - 1) + memo_f(n - 2)
        return memo[n]

    # memo_f(n)
    # return memo   #<- if you want entire list run this and above command
    return memo_f(n)


print(fib_memo(100))

"""This method is good and time complexity is O(N) but many recursions are taking place so it causes problem if 
we want answer for 1000 or more"""


# dynamin approach

def fib_dynamin(n):
    if n < 2:
        return n
    table = [None for x in range(n + 1)]
    table[:2] = [0, 1]

    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]

    return table


print(fib_dynamin(10))

"""
0-1 Knapsack Problem
Problem statement
You’re in charge of selecting a football (soccer) team from a large pool of players. Each player has a cost, and a rating. 
You have a limited budget. What is the highest total rating of a team that fits within your budget. Assume that there’s
 no minimum or maximum team size.

General problem statemnt:

Given n elements, each of which has a weight and a profit, determine the maximum profit that can be obtained by 
selecting a subset of the elements weighing no more than w."""

test0 = {
    'input': {
        'capacity': 165,
        'weights': [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
        'profits': [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    },
    'output': 309
}

test1 = {
    'input': {
        'capacity': 3,
        'weights': [4, 5, 6],
        'profits': [1, 2, 3]
    },
    'output': 0
}

test2 = {
    'input': {
        'capacity': 4,
        'weights': [4, 5, 1],
        'profits': [1, 2, 3]
    },
    'output': 3
}

test3 = {
    'input': {
        'capacity': 170,
        'weights': [41, 50, 49, 59, 55, 57, 60],
        'profits': [442, 525, 511, 593, 546, 564, 617]
    },
    'output': 1735
}

test4 = {
    'input': {
        'capacity': 15,
        'weights': [4, 5, 6],
        'profits': [1, 2, 3]
    },
    'output': 6
}

test5 = {
    'input': {
        'capacity': 15,
        'weights': [4, 5, 1, 3, 2, 5],
        'profits': [2, 3, 1, 5, 4, 7]
    },
    'output': 19
}

tests = [test0, test1, test2, test3, test4, test5]


# recursion

def knapsack_recursion(weight, profit, capicity, idx=0):
    if len(weight) == idx:
        return 0
    elif weight[idx] > capicity:
        return knapsack_recursion(weight, profit, capicity, idx + 1)
    else:
        option1 = knapsack_recursion(weight, profit, capicity, idx + 1)
        option2 = profit[idx] + knapsack_recursion(weight, profit, capicity - weight[idx], idx + 1)
        return max(option1, option2)


print("\n\nrecursion programming:")
for test in tests:
    print(knapsack_recursion(test['input']['weights'], test['input']['profits'], test['input']['capacity']) == test[
        'output'])


# memoization

def knapsack_memo(weight, profit, capicity, idx=0):
    memo = {}

    def memo_k(capicity, idx):
        key = (capicity, idx)

        if key in memo:
            return memo[key]
        if len(weight) == idx:
            memo[key] = 0
        elif weight[idx] > capicity:
            memo[key] = memo_k(capicity, idx + 1)
        else:
            option1 = memo_k(capicity, idx + 1)
            option2 = profit[idx] + memo_k(capicity - weight[idx], idx + 1)
            memo[key] = max(option1, option2)
        return memo[key]

    return memo_k(capicity, idx)


print("\n\nmemoization programming:")
for test in tests:
    print(knapsack_memo(test['input']['weights'], test['input']['profits'], test['input']['capacity']) == test[
        'output'])


# dynamic

def knapsack_dynamic(weight, profit, capicity):
    n = len(weight)
    results = [[0 for _ in range(capicity + 1)] for _ in range(n + 1)]
    for i in range(n):
        for c in range(1, capicity + 1):
            if weight[i] > c:
                results[i + 1][c] = results[i][c]
            else:
                results[i + 1][c] = max(results[i][c], profit[i] + results[i][c - weight[i]])
    return results[-1][-1]


print("\n\ndynamic programming:")
for test in tests:
    print(knapsack_dynamic(test['input']['weights'], test['input']['profits'], test['input']['capacity']) == test[
        'output'])
