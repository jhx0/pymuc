# pymuc
pymuc is a simple python script to show the 10 most used commands based on your shell's history file.   

pymuc was inspired by **muc** (https://github.com/nate-sys/muc)

## Example output:
![image](https://user-images.githubusercontent.com/37046652/211318613-89c7a30c-9b37-48cc-89ce-066d2a2342b3.png)

## Usage
```
$ ./pymuc [-h] [-v] [HISTORY_FILE]
```

## Install
1. Clone/Download the code in this repository
2. Install the necessary dependencies
```
pip install -r requirements.txt
```
3. Execute pymuc
```
$ ./pymuc
```

## Note
The only dependency needed is colorama, which can be found in most distributions repositories.   
For example on Debian:
```
# apt install python3-colorama
```
Check your distributions package repository.

## Hint
The number of commands printed can be changed with the **MAX_COMMANDS** constant at the beginning of the script.

## 
