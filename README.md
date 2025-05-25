# Python Hangman Game

A small and fun Hangman game developed in Python, with the primary goal of practicing the language's syntax and understanding fundamental programming concepts.

---

## 🎯 Project Goal

This project was created as a practical exercise to learn and solidify knowledge in:

* **Basic Python Syntax**: Covering variables, data types (strings, lists), operators, etc.
* **Control Flow Structures**: Using `if`, `elif`, `else`, `while`, and `for` loops.
* **Functions**: Defining and calling functions (`def`).
* **String and List Manipulation**: Operations like `.join()`, `len()`, index access `[]`, and understanding list mutability vs. string immutability.
* **Input and Output (I/O)**: Utilizing `print()` to display information and `input()` to get user input.
* **Built-in Modules**: Such as `os` (for clearing the screen) and `random` (for choosing random words).
* **F-strings**: A modern and efficient way to format strings.
* **Basic Error Handling**: Like `try-except` for user input (if you implemented `int(input())` validation).
* **Game Logic**: Implementing the core rules of a terminal-based game.

---

## ✨ Features

* Classic Hangman game with a diverse word list.
* Countdown of remaining guesses (chances).
* Hangman figure drawing that progresses with each incorrect guess.
* Screen clearing for a better visual experience.
* User input validation (ensures only a single letter is entered).
* Option to play again at the end of the game.
* Simple initial menu to start or exit the game.

---

## 🚀 How to Run the Game

To play the game, follow these steps:

1.  **Clone the repository** (or download the `main.py` file directly).
2.  **Navigate to the project folder** in your terminal or command prompt.
3.  **Execute the Python script**:
    ```bash
    python main.py
    ```
4.  Follow the on-screen instructions to start playing!

---

## 💡 Lessons Learned & Challenges Overcome

* **String Immutability vs. List Mutability**: Understanding why `secret_word` cannot be directly modified and the need to use a list (`hidden_word`) to reveal guessed letters.
* **Loop Management (`while` and `for`)**: The importance of `break` to exit loops and the correct `while` condition to end the game on either win or loss.
* **Execution Order and `clear()`**: The necessity of calling `clear()` at the beginning of each round and re-printing the entire game state.
* **Comparisons in Python**: Using `==` for equality and `in`/`not in` to check for element presence, in a more Pythonic way compared to other languages.
* **Encoding Errors**: Understanding and resolving `UnicodeEncodeError` when using special characters (if you attempted them).

---

## 👨‍💻 Contribution

This is a learning project, but feel free to inspect the code, suggest improvements, or use it as a base for your own studies.

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) (or another license of your choice, if preferred).