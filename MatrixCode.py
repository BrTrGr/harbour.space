class Matrix:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def print_matrix(self):
        for row in self.grid:
            print(row)
        print("---")

    def swap_rows(self, row1, row2):
        temp = self.grid[row1]
        self.grid[row1] = self.grid[row2]
        self.grid[row2] = temp

    def swap_cols(self, col1, col2):
        for i in range(self.rows):
            row = self.grid[i]
            temp = row[col1]
            row[col1] = row[col2]
            row[col2] = temp

    def full_gaussian_elimination(self):
        limit = self.rows
        if self.cols < self.rows:
            limit = self.cols

        for k in range(limit):
            max_value = 0
            best_row = k
            best_col = k

            for i in range(k, self.rows):
                for j in range(k, self.cols):
                    current_val = self.grid[i][j]
                    if current_val < 0:
                        current_val = -current_val
                    if current_val > max_value:
                        max_value = current_val
                        best_row = i
                        best_col = j

            if best_row != k:
                self.swap_rows(k, best_row)
            
            if best_col != k:
                self.swap_cols(k, best_col)

            pivot = self.grid[k][k]
            
            if pivot == 0:
                continue

            for i in range(k + 1, self.rows):
                factor = self.grid[i][k] / pivot
                for j in range(k, self.cols):
                    self.grid[i][j] = self.grid[i][j] - factor * self.grid[k][j]
                self.grid[i][k] = 0

my_data = [
    [0.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0]
]

m = Matrix(my_data)
m.full_gaussian_elimination()
m.print_matrix()

# class Matrix:
#     def __init__(self, entries):
#         self.entries = entries
#         self.rows = len(entries)
#         if self.rows > 0:
#             self.cols = len(entries[0])
#         else:
#             self.cols = 0

#     def __str__(self):
#         matrix_string = ""
#         for row in self.entries:
#             matrix_string += str(row) + "\n"
#         return matrix_string

#     def __getitem__(self, idx):
#         row_idx, col_idx = idx
#         return self.entries[row_idx][col_idx]

#     def __add__(self, other):
#         if self.rows != other.rows or self.cols != other.cols:
#             raise ValueError("Matrices must have the same dimensions for addition")
        
#         result_entries = []
#         for i in range(self.rows):
#             new_row = []
#             for j in range(self.cols):
#                 new_row.append(self.entries[i][j] + other.entries[i][j])
#             result_entries.append(new_row)
#         return Matrix(result_entries)

#     def __mul__(self, other):
#         if isinstance(other, (int, float)):
#             result_entries = []
#             for i in range(self.rows):
#                 new_row = []
#                 for j in range(self.cols):
#                     new_row.append(self.entries[i][j] * other)
#                 result_entries.append(new_row)
#             return Matrix(result_entries)
        
#         elif isinstance(other, Matrix):
#             if self.cols != other.rows:
#                 raise ValueError("Matrix dimensions not compatible for multiplication")
            
#             result_entries = []
#             for i in range(self.rows):
#                 new_row = []
#                 for j in range(other.cols):
#                     dot_product = 0
#                     for k in range(self.cols):
#                         dot_product += self.entries[i][k] * other.entries[k][j]
#                     new_row.append(dot_product)
#                 result_entries.append(new_row)
#             return Matrix(result_entries)
      
#         else:
#             raise TypeError("Multiplication only supported for scalars or other Matrices")