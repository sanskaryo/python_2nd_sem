class Matrix:
    def __init__(self, arr, m, n):
        self.m = m
        self.n = n
        self.arr = arr
        self.matrix = []

    def validity(self, m, n):
        return len(self.arr) == m * n

    def create_Matrix(self, m, n):
        # for i in range(m):
        #     row = []
        #     for j in range(n):
        #         row.append(self.arr[i * n + j])
        #     self.matrix.append(row)
        num= len(self.arr)
        i = 1
        row = []
        for i in range(num):
            if i !=n:
                row.append(self.arr[i])
                i = i+1
            else:
                row = []
            self.matrix.append(row)

    def disp_matrix(self):
        for row in self.matrix:
            print(*row)


lst = list(map(int, input("Enter space-separated values for the matrix: ").split()))
row, column = list(map(int, input("Enter number of rows and columns: ").split()))


m = Matrix(lst, row, column)


if m.validity(row, column):
    m.create_Matrix(row, column)
    m.disp_matrix()
else:
    print('Invalid dimension')

