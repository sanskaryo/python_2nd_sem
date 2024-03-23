class Matrix:
    """Represents a matrix with methods for addition, subtraction, multiplication, dot product, and transpose."""

    def __init__(self, data, rows=0, cols=0):
        """
        Initializes a Matrix object.

        Args:
            data (list): A list of lists representing the matrix elements.
            rows (int, optional): The number of rows in the matrix (default: 0, calculated from data).
            cols (int, optional): The number of columns in the matrix (default: 0, calculated from data).
        """

        self.data = data
        if not rows and not cols:
            rows = len(data)
            cols = len(data[0]) if data else 0
        self.rows = rows
        self.cols = cols

        # Validate matrix data (all rows have the same number of columns)
        if any(len(row) != cols for row in data):
            raise ValueError("Invalid matrix: All rows must have the same number of columns.")

    def __add__(self, other):
        """
        Adds two matrices of the same dimensions.

        Args:
            other (Matrix): The matrix to add to this matrix.

        Returns:
            Matrix: The sum of the two matrices.

        Raises:
            ValueError: If the matrices have different dimensions.
        """

        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __sub__(self, other):
        """
        Subtracts two matrices of the same dimensions.

        Args:
            other (Matrix): The matrix to subtract from this matrix.

        Returns:
            Matrix: The difference of the two matrices.

        Raises:
            ValueError: If the matrices have different dimensions.
        """

        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction.")
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other):
        """
        Performs matrix multiplication (element-wise multiplication for scalars,
        standard matrix multiplication for matrices).

        Args:
            other (int or Matrix): The scalar or matrix to multiply with.

        Returns:
            Matrix: The product of the matrix and the scalar or matrix.

        Raises:
            ValueError: If matrix multiplication is not possible (e.g., incompatible dimensions).
        """

        if isinstance(other, int):
            # Scalar multiplication
            result = [[other * element for element in row] for row in self.data]
            return Matrix(result)
        elif isinstance(other, Matrix):
            # Matrix multiplication
            if self.cols != other.rows:
                raise ValueError("Matrices cannot be multiplied: Inner dimensions must match.")
            result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
            return Matrix(result)
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Matrix' and '{}'".format(type(other)))

    def dot(self, other):
        """
        Calculates the dot product of this matrix and another matrix.

        Args:
            other (Matrix): The matrix to perform the dot product with.

        Returns:
            Matrix: The resulting dot product matrix.

        Raises:
            ValueError: If the inner dimensions of the matrices are not compatible for dot product.
        """

        if self.cols != other.rows:
            raise ValueError("Matrices cannot be multiplied for dot product: Inner dimensions must match.")
        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
        return Matrix(result)

    
    def transpose(self):
        """
        Returns the transpose of this matrix.

        Returns:
            Matrix: The transposed matrix.
        """
        result = [[0 for _ in range(self.rows)] for _ in range(self.cols)]  # Initialize empty matrix with swapped dimensions
        for i in range(self.rows):
            for j in range(self.cols):
                result[j][i] = self.data[i][j]  # Swap elements (i, j) to (j, i)
        return Matrix(result)

    # Additional improvements (optional):

    def __str__(self):
        """
        Returns a string representation of the matrix in a readable format.

        Returns:
            str: The string representation of the matrix.
        """
        rows = ["\t".join(str(x) for x in row) for row in self.data]
        return "\n".join(rows)

def main():
    """
    Prompts the user for matrix data, creates matrices, performs operations, and displays results.
    """

    try:
        # Get matrix data from user
        lst1 = list(map(eval, input("Enter the elements for matrix 1 (separated by spaces): \n").split()))
        r1, c1 = list(map(eval, input("Enter the dimensions for the Matrix 1 (rows, columns): \n").split()))
        arr1 = Matrix(lst1, r1, c1)

        lst2 = list(map(eval, input("Enter the elements for matrix 2 (separated by spaces): \n").split()))
        r2, c2 = list(map(eval, input("Enter the dimensions for the Matrix 2 (rows, columns): \n").split()))
        arr2 = Matrix(lst2, r2, c2)

        # Display matrices
        print("\nMatrix-1\n")
        print(arr1)

        print("\nMatrix-2\n")
        print(arr2)

        # Perform operations (handle potential exceptions)
        try:
            out_add = arr1 + arr2
            print("\nAddition")
            print(out_add)
        except ValueError as e:
            print(e)

        try:
            out_sub = arr1 - arr2
            print("\nSubtraction")
            print(out_sub)
        except ValueError as e:
            print(e)

        try:
            out_mul = arr1 * arr2
            print("\nMultiplication")
            print(out_mul)
        except ValueError as e:
            print(e)

        try:
            out_dot = arr1.dot(arr2)
            print("\nDot Multiplication")
            print(out_dot)
        except ValueError as e:
            print(e)

        print("\nTranspose")
        print("\nMatrix-1 Transpose")
        print(arr1.transpose())
        print("\nMatrix-2 Transpose")
        print(arr2.transpose())

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()