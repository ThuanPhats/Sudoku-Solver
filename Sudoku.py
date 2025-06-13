import tkinter as tk
from tkinter import messagebox

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3*(row//3), 3*(col//3)
    for i in range(3):
        for j in range(3):
            if board[start_row+i][start_col+j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

root = tk.Tk()
root.title("Sudoku Solver")

entries = [[None for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        e = tk.Entry(root, width=2, font=('Arial', 18), justify='center', bd=2)
        # Tô màu cho từng vùng 3x3
        if ((i // 3 + j // 3) % 2 == 0):
            e.configure(bg='#D5F5E3')
        else:
            e.configure(bg='#FCF3CF')
        e.grid(row=i, column=j, padx=1, pady=1)
        entries[i][j] = e

def get_board():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            val = entries[i][j].get()
            row.append(int(val) if val.isdigit() else 0)
        board.append(row)
    return board

def set_board(board):
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            if board[i][j] != 0:
                entries[i][j].insert(0, str(board[i][j]))

def solve():
    board = get_board()
    if solve_sudoku(board):
        set_board(board)
        messagebox.showinfo("Thành công", "Đã giải xong Sudoku!")
    else:
        messagebox.showwarning("Lỗi", "Không tìm được lời giải!")

def reset():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)

btn_solve = tk.Button(root, text="Giải", width=10, font=('Arial', 14), bg='#58D68D', command=solve)
btn_solve.grid(row=9, column=0, columnspan=4, pady=10)

btn_reset = tk.Button(root, text="Reset", width=10, font=('Arial', 14), bg='#F5B7B1', command=reset)
btn_reset.grid(row=9, column=5, columnspan=4, pady=10)

root.mainloop()
