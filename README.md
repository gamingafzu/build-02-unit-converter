# Unit Converter

Build #02 of my 12-month AI Engineer journey.

A Python command-line tool for converting distances and temperatures.

## Features

- Kilometres to miles
- Miles to kilometres
- Celsius to Fahrenheit
- Fahrenheit to Celsius
- Repeating menu with an Exit option
- Invalid menu choice handling
- Non-numeric input handling
- Negative distance validation
- Decimal values and negative temperatures supported

## How to Run

1. Install Python 3.
2. Open a terminal in the project folder.
3. Run:

   `python build02.py`

No external libraries are required.

## What I Practiced

- Functions, parameters and return values
- Converting input with float
- Displaying results with f-strings
- Connecting menu choices to functions
- Using if/elif/else and while loops
- Handling ValueError with try/except
- Using break and continue
- Formatting code with Black Formatter

## Bugs I Fixed

- Using choice before defining it
- Running all conversions before the menu
- Placing try/except around the wrong input
- Placing continue in the valid-input branch

## Testing

Manually checked conversions, zero and negative distances,
negative temperatures, non-numeric input, invalid menu choices
and Exit behavior.

## Learning Note

I built this project with mentor hints and editor suggestions.
I am documenting my learning, debugging and progress.
