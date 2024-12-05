# Python3 program to print all Subsequences
# of a string in iterative manner

# function to find subsequence
def subsequence(s, binary, length):
    sub = ""
    for j in range(length):
        if binary & (1 << j):
            sub += s[j]
    return sub


def possibleSubsequences(s):
    length = len(s)
    limit = 2 ** length
    for i in range(1, limit):
        yield subsequence(s, i, length)

s = "abc"
for i in possibleSubsequences(s):
    print(i)

# This code is contributed by ankush_953
