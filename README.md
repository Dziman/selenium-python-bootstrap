# Python selenium project bootstrap

## Python setup

1. Install Homebrew following steps from https://brew.sh

1. Install `pyenv`

    ```zsh
    brew install pyenv
    ```

1. Initialize `pyenv` 

    ```zsh
    eval "$(pyenv init --path)"
    eval "$(pyenv init -)"
    ```

1. Install required version (3.10.7) of python using `pyenv`

    ```zsh
    pyenv install 3.10.7
    ```

1. Use installed version of python:

    ```zsh
    pyenv global 3.10.7 # To set version globally
    pyenv local 3.10.7 # To set version locally aka current directory
    ```

## Other required tools

1. Install selenium web drivers you want to use for testing

    ```zsh
    brew install chromedriver
    ```

## Project initial setup

1. Create python virtual environment

    ```zsh
    python -m venv .selenium-venv
    ```

1. Activate virtual environment

    ```zsh
    source .selenium-venv/bin/activate
    ```

1. Install dependencies

    ```zsh
    pip install -r requirements.txt
    ```

1. Download and start IDE (VS Code) https://code.visualstudio.com

1. Install IDE extensions: python, Markdown All in one

## Run test

1. Run all tests

    ```zsh
    pytest
    ```

1. Run tests in file

    ```zsh
    pytest <file name>
    ```

1. Run tests and generate report

    ```zsh
    pytest --html=tests_report.html
    ```
