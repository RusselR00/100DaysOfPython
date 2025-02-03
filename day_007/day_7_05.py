# Positions on a chess boardareidentified byaletter and anumber.Theletteridentifies

# the column, while the number identifies the row.Write a program that reads a position from the user. Use an if statement to deter

# mine if the column begins with a black square or a white square. Then use modular

# arithmetic to report the color of the square in that row. For example, if the user enters

# a1 then your program should report that the square is black. If the user enters d5

# then your program should report that the square is white. Your program may assume

# that a valid position will always be entered. It does not need to perform any error

# checking

position = input("Enter a chess position (e.g., a1, d5): ")
column = position[0].lower()
row = int(position[1])

first_col_black = True  # 'a' is black

if ord(column) % 2 == ord('a') % 2:
    col_black = first_col_black
else:
    col_black = not first_col_black

if row % 2 == 0:
    square_black = not col_black
else:
    square_black = col_black

if square_black:
    print(f"The square at {position} is black.")
else:
    print(f"The square at {position} is white.")