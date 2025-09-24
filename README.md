# Automated Code Review Bot

## Overview
This project is an Automated Code Review Bot built with Python. 
It scans Python code for code quality, style, and security issues using both internal checks and external tools (pylint, flake8, bandit).

## Features
- Internal AST checks:
  - Missing docstrings
  - Unused imports
  - Function naming conventions
  - TODO/FIXME comments
- External tools:
  - pylint (code quality & naming)
  - flake8 (style & syntax)
  - bandit (security vulnerabilities)
- Generates console output and JSON report.

## Project Structure
