# ASCII color and style definitions
colors = {
    "Black": "\033[30m",
    "Red": "\033[31m",
    "Green": "\033[32m",
    "Yellow": "\033[33m",
    "Blue": "\033[34m",
    "Magenta": "\033[35m",
    "Cyan": "\033[36m",
    "White": "\033[37m",
    "Bright Black": "\033[90m",
    "Bright Red": "\033[91m",
    "Bright Green": "\033[92m",
    "Bright Yellow": "\033[93m",
    "Bright Blue": "\033[94m",
    "Bright Magenta": "\033[95m",
    "Bright Cyan": "\033[96m",
    "Bright White": "\033[97m",
    "Reset": "\033[0m",
    "Bold": "\033[1m",
    "Underline": "\033[4m",
    "Reversed": "\033[7m"
}

# Print example text for each color and style
for color_name, color_code in colors.items():
    print(f"{color_code}This is the color {color_name}{colors['Reset']}")

# Additional formatting examples
print(f"{colors['Bold']}This text is bold{colors['Reset']}")
print(f"{colors['Underline']}This text is underlined{colors['Reset']}")
print(f"{colors['Reversed']}This text has reversed colors{colors['Reset']}")
