#!/usr/bin/env python3

import sys
import os.path
from os.path import expanduser
from colorama import Fore, Style

PRG_NAME = "ctop"
PRG_VERSION = "0.0.1"

# Defines the used bar character(s)
BAR_CHAR = "##"

# Number of displayed commands in output
MAX_COMMAND = 10

# By default the bash history file is used
history_file = ".bash_history"

def error(message):
    print("[ERROR] {}!".format(message))
    sys.exit(1)

def read_history():
    if len(sys.argv) != 2:
        history = open(expanduser("~") + "/" + history_file)
    else:
        try:
            history = open(sys.argv[1])
        except FileNotFoundError:
            error("Could not open history file!")

    content = history.readlines()

    return content

def parse_history(data):
    d = {}

    for entry in data:
        l = entry.rstrip()
        if l not in d:
            d[l] = 0
        d[l] += 1

    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

def _print(command, counter, max_count):
    bar_size = int(((counter * 100) / max_count) / 10)

    print("{}[{}{:20s}{}]{} {}{:4}{} - {}".format(
        Style.BRIGHT + Fore.RED,
        Fore.GREEN,
        BAR_CHAR * bar_size,
        Fore.RED,
        Style.RESET_ALL,
        Style.BRIGHT + Fore.CYAN,
        counter,
        Style.RESET_ALL + Fore.RESET,
        command
        ))

def show(history):
    count = 0

    max_count = history[next(iter(history))]

    for command, counter in history.items():
        if count == MAX_COMMAND:
            break
        _print(command, counter, max_count)
        count += 1

def usage():
    print("USAGE: {} [HISTORY_FILE]".format(PRG_NAME))
    sys.exit(0)

def version():
    print("{} v{}".format(PRG_NAME, PRG_VERSION))
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "-h":
            usage()

        if sys.argv[1] == "-v":
            version()

    content = read_history()

    history = parse_history(content)

    show(history)