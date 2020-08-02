"""
An implementation of Strassen's Subcubic Matrix Multiplication algorithm
"""

def dot_product(v1, v2):
    """
    Returns the dot product of two arrays.

    params:
        x: array
        y: array
    """
    total = 0
    for x, y in zip(v1, v2):
        total += x * y

    return total


def get_col(matrix, ind):
    col = []
    for row in matrix:
        col.append(row[ind])

    return col


def naive_matrix_mul(m1, m2):
    # Assumes m1 and m2 are same-sized square matrices
    # of dimensions NxN
    # It has time complexity N^2

    N = len(m1)
    output = [
        [ None ] * N
    ] * N
    for i in range(N):
        for j in range(N):
            row = m1[i]
            col = get_col(m2, j)
            entry = dot_product(row, col)
            output[i][j] = entry

    return output


def get_quadrants(matrix):
    half = len(matrix) // 2
    A = [row[:half] for row in matrix[:half]]
    B = [row[half:] for row in matrix[:half]]
    C = [row[:half] for row in matrix[half:]]
    D = [row[half:] for row in matrix[half:]]

    return A, B, C, D


def strassens_mul(m1, m2):
    """
        1. Split m1 and m2 into 4 quadrants each
        2. Compute the 7 products recursively using strassen's multiplication
        3. Recover the final product using the above 7 products
    """
    if len(m1) == 2: # base case
        A = m1[0][0]
        B = m1[0][1]
        C = m1[1][0]
        D = m1[1][1]

        E = m2[0][0]
        F = m2[0][1]
        G = m2[1][0]
        H = m2[1][1]
        output = [
            [ A*E + B*G  , A*F + B*H ],
            [ C*E + D*G  , C*F + D*H ]
        ]
        return output
    else:
        A, B, C, D = get_quadrants(m1)
        E, F, G, H = get_quadrants(m2)
        p1 = strassens_mul(A, np.subtract(F, H))
        p2 = strassens_mul(np.add(A, B), H)
        p3 = strassens_mul(np.add(C, D), E)
        p4 = strassens_mul(D, np.subtract(G, E))
        p5 = strassens_mul(np.add(A, D), np.add(E, H))
        p6 = strassens_mul(np.subtract(B, D), np.add(G, H))
        p7 = strassens_mul(np.subtract(A, C), np.add(E, F))

        output = [
            [np.add(np.subtract(np.add(p5, p4), p2), p6), np.add(p1, p2)                                  ],
            [np.add(p3, p4)                             , np.subtract(np.subtract(np.add(p1, p5), p3), p7)]
        ]
        return output


"""
X = [[[[1, 2], [3, 4]], [[1, 2], [3, 4]]], [[[1, 2], [3, 4]], [[1, 2], [3, 4]]]]
Y = [[array([[2, 4],
         [6, 8]]),
  [[1, 2], [3, 4]]],
 [array([[ 3,  6],
         [ 9, 12]]),
  array([[ 4,  8],
         [12, 16]])]]

output = np.dot(X, Y)

array([[[[[[14, 20],
           [ 7, 10]],

          [[21, 30],
           [28, 40]]],


         [[[30, 44],
           [15, 22]],

          [[45, 66],
           [60, 88]]]],



        [[[[14, 20],
           [ 7, 10]],

          [[21, 30],
           [28, 40]]],


         [[[30, 44],
           [15, 22]],

          [[45, 66],
           [60, 88]]]]],




       [[[[[14, 20],
           [ 7, 10]],

          [[21, 30],
           [28, 40]]],


         [[[30, 44],
           [15, 22]],

          [[45, 66],
           [60, 88]]]],



        [[[[14, 20],
           [ 7, 10]],

          [[21, 30],
           [28, 40]]],


         [[[30, 44],
           [15, 22]],

          [[45, 66],
           [60, 88]]]]]])
"""