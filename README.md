# 🧩 Sudoku Solver in Python

A simple and efficient Sudoku Solver built using **Python** and the **Backtracking Algorithm**. This project takes an incomplete Sudoku puzzle as input and automatically finds a valid solution.

## 📌 Features

- Solves standard 9×9 Sudoku puzzles
- Uses the Backtracking algorithm
- Easy-to-understand and well-structured code
- Beginner-friendly Python project
- Console-based interface

## 🛠️ Technologies Used

- Python 3

## 📂 Project Structure

```text
Sudoku-Solver/
│
├── sudoku_solver.py
├── README.md
└── requirements.txt
```

## 🚀 Getting Started

### Prerequisites

Make sure Python 3 is installed on your system.

Check your Python version:

```bash
python --version
```

### Clone the Repository

```bash
git clone https://github.com/your-username/Sudoku-Solver.git
cd Sudoku-Solver
```

### Run the Program

```bash
python sudoku_solver.py
```

## 🧠 Algorithm Used

This project uses the **Backtracking Algorithm**.

### Steps:

1. Find an empty cell in the Sudoku grid.
2. Try placing numbers from 1 to 9.
3. Check whether the number placement is valid.
4. If valid, move to the next empty cell.
5. If no valid number exists, backtrack and try another number.
6. Repeat until the puzzle is solved.

## 📋 Example Input

```text
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

## ✅ Example Output

```text
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

## 🎯 Learning Outcomes

- Understanding recursion
- Understanding backtracking
- Working with 2D lists in Python
- Problem-solving and algorithm design

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push to your branch
6. Create a Pull Request

## 📜 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Developed as a beginner-friendly Python project for learning Backtracking and Sudoku solving techniques.
