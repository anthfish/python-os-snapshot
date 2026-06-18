# python-os-snapshot

A simple Python automation script that captures a directory listing, saves it to a timestamped text file, and zips it for archiving - all from within Python.

## What it does

- Runs 'ls -la' via 'subprocess.run()'
- Saves the output to a timestamped '.txt' log file
- Zips the log file using the 'zipfile' module
- Supports a custom output name via the 'SNAPSHOT_NAME' environment variable

## Usage

Basic run:
	python3 snapshot.py

With custom name:
	SNAPSHOT_NAME=mybackup python3 snapshot.py

## Modules used

subprocess, os, zipfile, datetime

## Notes

No third-party packages required. Standard library only.
