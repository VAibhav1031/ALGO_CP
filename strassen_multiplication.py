# Strassen  Multiplcation
import random
import time
# simple Multiplcation .

# lets say we
num = [[1, 4], [9, 6]]
num_1 = [[2, 3], [2, 3]]

n = len(num)
result = [[0] * n for _ in range(n)]
for i in range(len(num)):
    for j in range(len(num)):
        for k in range(len(num)):
            result[i][j] += num[i][k] * num_1[k][j]

# this is the simple Multiplcation you may see, why this  one is difficult one for many people
# print(result)


# currently here we are using the nXn matrix so you must know  k  is the common part in both matrix size mxk kxp
# so you can change like that only which will be more helpful and nice


# then comes to the thing like
# How could we improvise this  thing for bigger matrix  only talking in square matrix terms ,  you can have normal one also .
# BEcause square matrix specially with even one is  very easily to use in the Divide and conquer ALgorithm


def add(A, B):
    n = len(A)
    return (
        [[A[0][0] + B[0][0]]]
        if n == 1
        else [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]
    )


def sub_mat(A, B):
    n = len(A)
    return (
        [[A[0][0] - B[0][0]]]
        if n == 1
        else [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]
    )


def split_matrix(mat):
    n = len(mat)
    mid = n // 2

    mat11 = [row[:mid] for row in mat[:mid]]
    mat12 = [row[mid:] for row in mat[:mid]]
    mat21 = [row[:mid] for row in mat[mid:]]
    mat22 = [row[mid:] for row in mat[mid:]]

    return mat11, mat12, mat21, mat22


def combine_quadrant(c11, c12, c21, c22):
    top = [a + b for a, b in zip(c11, c12)]
    bottom = [a + b for a, b in zip(c21, c22)]

    return top + bottom


# we mostly accecpt the even n


def multi(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    M1 = multi(A11, B11)
    M2 = multi(A12, B21)
    M3 = multi(A11, B12)
    M4 = multi(A12, B22)
    M5 = multi(A21, B11)
    M6 = multi(A22, B21)
    M7 = multi(A21, B12)
    M8 = multi(A22, B22)

    C11 = add(M1, M2)
    C12 = add(M3, M4)
    C21 = add(M5, M6)
    C22 = add(M7, M8)

    return combine_quadrant(C11, C12, C21, C22)


def strassenMultiplication(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    a11, a12, a21, a22 = split_matrix(A)
    b11, b12, b21, b22 = split_matrix(B)

    m1 = strassenMultiplication(a11, sub_mat(b12, b22))
    m2 = strassenMultiplication(add(a11, a12), b22)
    m3 = strassenMultiplication(add(a21, a22), b11)
    m4 = strassenMultiplication(a22, sub_mat(b21, b11))
    m5 = strassenMultiplication(add(a11, a22), add(b11, b22))
    m6 = strassenMultiplication(sub_mat(a12, a22), add(b21, b22))
    m7 = strassenMultiplication(sub_mat(a11, a21), add(b11, b12))

    C11 = add(sub_mat(add(m5, m4), m2), m6)
    C12 = add(m1, m2)
    C21 = add(m3, m4)
    C22 = sub_mat(sub_mat(add(m5, m1), m3), m7)

    return combine_quadrant(C11, C12, C21, C22)


def generate_matrix(n):
    return [[random.randint(0, 10) for _ in range(n)] for _ in range(n)]


A1 = [[1, 2], [3, 4]]
B1 = [[5, 6], [7, 8]]
# Expected result: [[19, 22], [43, 50]]

A2 = [[2, 0], [1, 3]]
B2 = [[1, 2], [3, 4]]
# Expected result: [[2, 4], [10, 14]]

A3 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
B3 = [[9, 8, 7, 6], [5, 4, 3, 2], [1, 1, 1, 1], [0, 0, 0, 0]]
# Expected result: B itself (A is identity matrix)


def padUP(A):
    r, c = len(A), len(A[0])
    cur = max(r, c)
    if cur & (cur - 1) == 0:
        # just  add the number of required in the less one
        if min(r, c) == c:
            return [row + [0] * (r - c) for row in A]
        else:
            return A + [[0 for _ in range(cur)] for _ in range(cur - r)]

    req = 1
    while req < cur:
        req <<= 1

    return [row + [0] * (req - c) for row in A] + [
        [0 for _ in range(req)] for _ in range(req - r)
    ]


def strassen_pad_up(A, B):
    r1, c1 = len(A), len(A[0])
    r2, c2 = len(B), len(B[0])

    if (r1, c1) >= (r2, c2):
        new_A = padUP(A)
        req_r, req_c = len(new_A) - r2, len(new_A[0]) - c2
        new_B = [row + [0] * req_c for row in B] + [
            [0] * (c2 + req_c) for _ in range(req_r)
        ]
    else:
        new_B = padUP(B)
        req_r, req_c = len(new_B) - r1, len(new_B[0]) - c1
        new_A = [row + [0] * req_c for row in A] + [
            [0] * (c1 + req_c) for _ in range(req_r)
        ]

    return new_A, new_B


# N = 256
# new_A = generate_matrix(N)
# new_B = generate_matrix(N)
#
# # print(new_A)
# st = time.time()
# multi(new_A,new_B)
# et = time.time()
# print(f"Divide and conquer(fcked) time: {(et-st)*1000:.2f}ms")
#
# st_ = time.time()
# strassenMultiplication(new_A,new_B)
# et_ = time.time()
# print(f"Strassen time :{(et_-st_)*1000:.2f}ms")
#
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8], [9, 10]]

new_A, new_B = strassen_pad_up(A, B)
print("A:")
for row in new_A:
    print(row)
print("B:")
for row in new_B:
    print(row)


def unpad(matrix, r, c):
    return [row[:c] for row in matrix[:r]]


def test_strassen():
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    print()
    padded_A, padded_B = strassen_pad_up(A, B)
    for row in padded_A:
        print(row)
    print()
    for row in padded_B:
        print(row)
    padded_result = strassenMultiplication(padded_A, padded_B)
    final_result = unpad(padded_result, len(A), len(B[0]))

    print("\nFinal Result:")
    for row in final_result:
        print(row)


test_strassen()
