first_square_col, first_square_row = int(input()), int(input())
second_square_col, second_square_row = int(input()), int(input())

if first_square_col == second_square_col:
    print("YES")
elif first_square_row == second_square_row:
    print("YES")
elif first_square_col == first_square_row and second_square_col == second_square_row:
    print("YES")
else:
    print("NO")