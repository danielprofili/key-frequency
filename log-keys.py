"""Simple background keylogger.
Author: Joe Vinciguerra, danielprofili
Date: 2020.06.15
This program will run in the background and record keystrokes to a text
file. The intended purpose is to study personal key usage for optimizing
a custom keyboard layout. This software is not to be used for unlawful
or nefarious activities, or without the knowledge and explicit consent
of the keyboard operator.
Requires:
    pynut
    logging
    matplotlib
"""

# Import required modules
from pynput import keyboard
import logging
# for handling ctrl-c
import signal
import sys
import matplotlib.pyplot as plt
import argparse

# Parse args
parser = argparse.ArgumentParser(description='Log keypresses (with consent!)')
parser.add_argument('--logfile', '-l', default='keys.log',
                    help='Filename of the log file')
args = parser.parse_args()

# Initialize variables
global armed
armed = False
buffer = dict()
modifiers = ['Key.alt', 'Key.cmd', 'Key.ctrl', 'Key.shift']
log_file = args.logfile

# # Resets the log file, apparently?
# with open(log_file, 'w'):
#     pass

# Configure logging
logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(message)s',
        )

# Log the key sequence
def log(seq):
    seq = seq.replace('\'', '')
    logging.info(msg=seq)
    print(seq)

# Check the key sequence for modifier combinations
def form_log(seq):
    seq = list(seq)
    # Check for non-modifier sequences.
    if seq[0] not in modifiers:
        for item in seq:
            log(item)
    # Assume the rest are modifier sequences.
    else:
        seq = '+'.join(seq)
        log(seq)


def on_press(key):
    global armed
    # Arm if the last event was a "press"
    armed = True
    # Convert modified keys to canonical
    key_pressed = listener.canonical(key)
    # Convert to string
    if not isinstance(key_pressed, str):
        key_pressed = str(key_pressed)
    # Add pressed keys to the dictionary
    buffer[key_pressed] = key_pressed


def on_release(key):
    global armed
    # Log keys on a "release" if a "press" happened prior
    if armed:
        form_log(buffer)
    # Convert modified keys to canonical
    key_released = listener.canonical(key)
    # Convert to string
    if not isinstance(key_released, str):
        key_released = str(key_released)
    # Remove released keys from dictionary
    buffer.pop(key_released, None)
    # Unarm if the last event was a "release"
    armed = False


# Interrupt handler
def signal_handler(signal, frame):
    buffer.clear()
    sys.exit(0)

# Register interrupt handler
signal.signal(signal.SIGINT, signal_handler)

# Run the keyboard listener thread
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
