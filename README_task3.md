# Password Generator

## Overview

This Python script generates unique passwords based on user-defined complexity levels and optional inclusion of a custom string. The password generator supports three complexity levels: easy, medium, and hard, which determine the character sets used. The script also allows users to specify a custom string to be included in the generated password.

## Features

- **Customizable Complexity**:
  - **Easy**: Includes only lowercase letters.
  - **Medium**: Includes both lowercase and uppercase letters.
  - **Hard**: Includes lowercase and uppercase letters, digits, and special characters.
  
- **Custom String Inclusion**: Optionally include a user-specified string in the password.
- **Length Validation**: Ensures the generated password meets the desired length and complexity requirements.
- **Shuffling**: Mixes characters to ensure the custom string is not easily predictable in the password.

## Installation

1. **Ensure Python is Installed**

   Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Save the Script**

   Copy the script into a file named `password_generator.py`.

3. **Run the Script**

   Open a terminal or command prompt, navigate to the directory where `password_generator.py` is located, and run the following command:

   ```bash
   python password_generator.py
