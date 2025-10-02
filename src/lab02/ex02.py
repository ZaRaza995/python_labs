def is_rectangular(mat: list[list[float | int]]) -> bool:
  if not mat:
    return True
  first_row_len = len(mat[0])
  for row in mat:
    if len(row) != first_row_len:
      return False
  return True

def transpose(mat: list[list[float | int]]):
  if not mat:
    return []
  
  if not is_rectangular(mat):
    raise ValueError("Матрица должна быть прямоугольной")
    
  num_rows = len(mat)
  num_cols = len(mat[0])
  
  transposed_mat = [] 
  
  for j in range(num_cols):
    new_row = [] 
  
    for i in range(num_rows):

      new_row.append(mat[i][j])
      
    transposed_mat.append(new_row)
      
  return transposed_mat

print(transpose([[1, 2, 3]]))
print(transpose([[1, 2], [3, 4], [5, 6]]))