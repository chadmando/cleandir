**Disclaimer**: This is a work in progress. Use at your own risk.

# Cleandir

A directory clean-up script written in pure python.

## Requirements
Cleandir was written in python 3.6.5 (macOS) and tested on Windows 10 x64 using python 3.7.1
It has not been tested using legacy python.

## What operating systems is cleandir made for?
Because cleandir is written in pure python, it can be used anywhere python is installed. 
* Linux
* Mac
* Windows

## What does cleandir do?
Cleandir attempts to organize a folder by grouping select files
into subfolders based on their file type / extension.

## How do you use cleandir?
from a terminal or command prompt:

```angular2
c:\path\to\cleandir> python cleandir.py
```

You are prompted to enter the directory. Just the directory no quotes required.
On Windows:
```angular2
enter an absolute path to clean (default=C:\users\<username>\cleandir): C:\Users\<username>\Documents
```
On Linux or Mac:
```angular2
enter an absolute path to clean (default=/Users/<username>/cleandir): /Users/<username>/Documents
```
