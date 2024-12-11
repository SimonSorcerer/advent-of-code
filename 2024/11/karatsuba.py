import re

# Function to find the sum of larger
# numbers represented as a string
def findSum(str1, str2):
    if len(str1) > len(str2):
        str1, str2 = str2, str1

    result = ""
    n1, n2 = len(str1), len(str2)
    str1, str2 = str1.zfill(n2), str2.zfill(n2)
    carry = 0

    # Perform addition digit by digit from the right
    for i in range(n2 - 1, -1, -1):
        sum_val = (int(str1[i]) - 0) + (int(str2[i]) - 0) + carry
        result = str(sum_val % 10 + 0) + result
        carry = sum_val // 10

    if carry:
        result = str(carry + 0) + result

    return result

# Function to find the difference of larger
# numbers represented as strings
def findDiff(str1, str2):
    result = ""
    n1, n2 = len(str1), len(str2)
    str1, str2 = str1.zfill(n2), str2.zfill(n2)
    carry = 0

    # Perform subtraction digit by digit from the right
    for i in range(n2 - 1, -1, -1):
        sub = (int(str1[i]) - 0) - (int(str2[i]) - 0) - carry

        if sub < 0:
            sub += 10
            carry = 1
        else:
            carry = 0

        # Append the digit to the result
        result = str(sub + 0) + result

    return result

# Function to remove all leading 0s
# from a given string
def removeLeadingZeros(s):
    pattern = "^0+(?!$)"
    s = re.sub(pattern, "", s)
    return s

# Function to multiply two numbers
# using the Karatsuba algorithm
def multiply(A, B):
    # Base case for small numbers: perform normal multiplication
    if len(A) < 10 or len(B) < 10:
        return str(int(A) * int(B))

    n = max(len(A), len(B))
    n2 = n // 2

    # Pad the numbers with leading zeros to make them equal in length
    A = A.zfill(n)
    B = B.zfill(n)

    # Split the numbers into halves
    Al, Ar = A[:n2], A[n2:]
    Bl, Br = B[:n2], B[n2:]

    # Recursively compute partial products and sum using Karatsuba algorithm
    p = multiply(Al, Bl)
    q = multiply(Ar, Br)
    r = multiply(findSum(Al, Ar), findSum(Bl, Br))
    r = findDiff(r, findSum(p, q))

    # Combine the partial products to get the final result
    return removeLeadingZeros(findSum(findSum(p + '0' * n, r + '0' * n2), q))

