# key-frequency
This is a simple program which records keypresses and key combinations, writes them to a log file, and optionally plots the results as a histogram.

The intended purpose is to study personal key usage for optimizing a custom keyboard layout. This software is not to be used for unlawful or nefarious activities, or without the knowledge and explicit consent of the keyboard operator.

As long as the program is open the keystrokes are being recorded. Recording stops as soon as the program is closed.

> ## Do not run this program while typing sensitive information including, but not limited to usernames, passwords, account numbers, banking information.

# Requirements
`matplotlib`

# Usage
`python3 log-keys.py <LOGFILE>`

# Output format
The program writes keypresses to a log file, whose default path is `keys.log` in the script directory.

Each line in the log is a seperate key or combination of keys. The program will attempt to parse key combinations such as `Key.alt+Key.tab` or `Key.ctrl+s`. Combinations that include modifications by holding [shift] will be suffixed with the unmodified (canonical) character; for example a quesiton mark (?) is recorded as `Key.shift+/`

>Note: buffering occurs on key presses, but they are not recorded until a key is released. This allows for parsing of key combinations to a single line.

# To-Do:
    The expected squence is LIFO. If the sequence is FIFO then the keys are not properly popped from the dictionary. For example, pressing `a+s+d+f`, then releasing in FIFO order produces duplicate results.
