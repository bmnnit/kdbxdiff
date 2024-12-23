# KDBX Password Comparator

This Python script compares two KeePass KDBX files and highlights the differences in passwords, 
entries that exist in only one file, and mismatched passwords.

## Features
- Compares passwords across two KDBX files.
- Identifies entries missing in either file.
- Highlights mismatched passwords for common entries.

## Requirements
- Python 3.7 or newer.
- `pykeepass` library.

## Setup

1. Create and activate a Python virtual environment:
   ```bash
   python -m venv kdbx_env
   source kdbx_env/bin/activate  # On Windows: kdbx_env\Scripts\activate
