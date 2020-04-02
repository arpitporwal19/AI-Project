from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

Row = int(input("Enter the number of rows:")) 
Column = int(input("Enter the number of columns:")) 
  
matrix = [] 

print("Enter the entries:") 
  
for i in range(Row):        
    a =[] 
    for j in range(Column):      
         a.append(int(input())) 
    matrix.append(a)

A = int(input("Enter first start index:"))
B = int(input("Enter second start index:"))    
    
D = int(input("Enter first end index:"))
E = int(input("Enter second end index:"))

grid = Grid(matrix=matrix)

start = grid.node(A, B)
end = grid.node(D, E)

finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
path, runs = finder.find_path(start, end, grid)

print('No. of operations:', runs, 'Length of path:', len(path))
print(grid.grid_str(path=path, start=start, end=end))

print(path)