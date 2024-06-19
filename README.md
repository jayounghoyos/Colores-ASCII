
# ASCII Color Codes in Python

This repository contains a Python script demonstrating how to use ASCII color codes to decorate text in the console. Each color and style is shown with example text, making it easy to see how they can be used.

## Table of Contents

- [ASCII Color Codes in Python](#ascii-color-codes-in-python)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Requirements](#requirements)
  - [How to Use](#how-to-use)
    - [Run the Script](#run-the-script)
    - [Customize Text Colors](#customize-text-colors)
    - [Additional Formatting](#additional-formatting)
  - [Additional Resources](#additional-resources)
    - [Example ASCII colors](#example-ascii-colors)

## Introduction

ASCII color codes are a simple and effective way to add color and styling to your console output. This can be particularly useful for making logs more readable, highlighting important messages, or just adding some visual flair to your command-line applications.

## Requirements

To use the provided script, you need:

- Python 3.x installed on your machine.
- A terminal that supports ANSI escape codes (most modern terminals do).

## How to Use

### Run the Script

1. **Clone the Repository**: Clone this repository to your local machine using:

   ```bash
   git clone https://github.com/your-username/ascii-colors-python.git
   ```

2. **Navigate to the Directory**: Change to the directory where the script is located:

   ```bash
   cd ascii-colors-python
   ```

3. **Run the Script**: Execute the script to see the color examples:

   ```bash
   python ascii_colors.py
   ```

### Customize Text Colors

To apply a specific color to your text in your own scripts:

1. **Import or Define the Colors**: Use the color dictionary from the provided script, or define your own as shown below.

   ```python
   colors = {
       "Red": "[31m",
       "Green": "[32m",
       "Blue": "[34m",
       "Reset": "[0m"
   }
   ```

2. **Apply the Color**: Use the color codes to wrap your text.

   ```python
   print(f"{colors['Red']}This is red text{colors['Reset']}")
   ```

### Additional Formatting

In addition to colors, you can also apply various text styles:

- **Bold**: Makes your text bold.

  ```python
  print(f"{colors['Bold']}This is bold text{colors['Reset']}")
  ```

- **Underline**: Underlines your text.

  ```python
  print(f"{colors['Underline']}This is underlined text{colors['Reset']}")
  ```

- **Reversed Colors**: Swaps the foreground and background colors.

  ```python
  print(f"{colors['Reversed']}This text has reversed colors{colors['Reset']}")
  ```

You can combine these styles with colors to create even more variations.

## Additional Resources

- **[ANSI Escape Codes](https://en.wikipedia.org/wiki/ANSI_escape_code)**: Learn more about the technical details of ANSI escape codes.
- **[Python Colorama Library](https://pypi.org/project/colorama/)**: A Python library that simplifies the use of colors in console applications, particularly useful for Windows users.
- **[Rich](https://rich.readthedocs.io/en/stable/)**: A Python library for rich text and beautiful formatting in the terminal.

---

### Example ASCII colors

![ASCII_Colors](/image.png)

---
Feel free to experiment with the colors and styles to enhance your console output. Happy coding!
