"""
Invoke tasks for the project
This file contains tasks to manage the project, including installing dependencies,
running tests, linting, formatting code, and cleaning up temporary files.
"""

import os
import subprocess

from invoke import task

PACKAGE_NAME = "wine-quality-prediction-webapp"
PYTHON = "python"
PIP = "pip"


@task
def install(ctx):
    """Install dependencies"""
    print("\033[0;34mInstalling dependencies...\033[0m")
    try:
        ctx.run(f"{PIP} install -r requirements.txt", warn=True)
        print("\033[0;32mDependencies installed.\033[0m\n")
    except subprocess.SubprocessError as e:
        print(f"\033[0;31mError installing dependencies: {e}\033[0m")


@task
def test(_):
    """Run tests in the tests folder and display coverage in terminal"""
    print("\033[0;34mRunning tests...\033[0m")
    coverage_file = os.path.join("tests", ".coverage")

    # Command to set the PYTHONPATH and run pytest
    command = (
        "set PYTHONPATH=%PYTHONPATH%;. && pytest --cov=main --cov=app --cov=source "
        "--cov-report=term --cov-config=.coveragerc tests/"
    )

    # Adjust for different operating systems (Windows vs Unix)
    if os.name == "nt":  # Windows
        command = f"set COVERAGE_FILE={coverage_file} && " + command
    else:  # Unix-like systems
        command = f"COVERAGE_FILE={coverage_file} " + command

    try:
        # Run the command using subprocess
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, check=True
        )

        # Output the command's stdout and stderr
        print(result.stdout)

        # Handle specific warnings and errors
        if result.returncode == 5:
            # No Data was Collected
            print(f"\033[0;31mNo Data Collected: {result.stderr}\033[0m")
        elif "ModuleNotFoundError" in result.stderr:
            # Handle the case where a module is not found
            print(f"\033[0;31mModule Import Error: {result.stderr}\033[0m")
        elif "ImportError" in result.stderr:
            # Handle import errors if pytest cannot import the modules being tested
            print(
                f"\033[0;31mImportError: Ensure your modules "
                f"are correctly imported. {result.stderr}\033[0m"
            )
        elif "no tests were collected" in result.stderr:
            # Case where pytest couldn't collect any tests
            print(f"\033[0;31mNo tests collected: {result.stderr}\033[0m")
        elif result.returncode != 0:
            # Handle other non-zero exit codes (which indicate test failures)
            print(f"\033[0;31mTest execution failed: {result.stderr}\033[0m")

    except FileNotFoundError as e:
        # Handle case where pytest is not found or required files are missing
        print(
            f"\033[0;31mFileNotFoundError: {e}. Ensure pytest is installed"
            f"and paths are correct.\033[0m"
        )
    except subprocess.CalledProcessError as e:
        # Handle errors during subprocess execution
        print(
            f"\033[0;31mSubprocessError: {e}. Ensure all paths and"
            f"environment variables are correct.\033[0m"
        )

    else:
        # If no exceptions occurred, notify that the tests are completed
        print(
            "\033[0;32mTests completed. Coverage report displayed in terminal.\033[0m\n"
        )


@task
def lint(ctx):
    """Lint specified directories and files"""
    print("\033[0;34mLinting code...\033[0m")
    files_to_lint = "source app.py main.py setup.py tasks.py template.py"
    try:
        ctx.run(f"pylint {files_to_lint}", warn=True)
        print("\033[0;32mLinting completed.\033[0m\n")
    except subprocess.SubprocessError as e:
        print(f"\033[0;31mLinting failed: {e}\033[0m")


@task
def formatter(ctx):
    """Format specified directories and files"""
    print("\033[0;34mFormatting code...\033[0m")
    files_to_format = "source app.py main.py setup.py tasks.py template.py"
    try:
        ctx.run(f"black {files_to_format}", warn=True)
        ctx.run(f"isort {files_to_format}", warn=True)
        print("\033[0;32mFormatting completed.\033[0m\n")
    except subprocess.SubprocessError as e:
        print(f"\033[0;31mFormatting failed: {e}\033[0m")


@task
def clean(ctx):
    """Clean up temporary files"""
    print("\033[0;34mCleaning up...\033[0m")
    try:
        if os.name == "nt":
            ctx.run("del /s /q *.pyc", warn=True)
            ctx.run("for /d %p in (__pycache__) do rmdir /s /q %p", warn=True)
        else:
            ctx.run("find . -name '*.pyc' -delete", warn=True)
            ctx.run("find . -type d -name '__pycache__' -exec rm -rf {} +", warn=True)
        print("\033[0;32mCleanup completed.\033[0m\n")
    except subprocess.SubprocessError as e:
        print(f"\033[0;31mCleanup failed: {e}\033[0m")


@task
def every(ctx):
    """Run all tasks: install, lint, format, test, and cleanup"""
    print("\033[0;34mEXECUTING ALL TASKS...\033[0m\n")

    try:
        install(ctx)
    except subprocess.SubprocessError as e:
        print(f"\033[0;31mInstall task failed: {e}\033[0m")

    try:
        formatter(ctx)
    except subprocess.SubprocessError as e:
        print(f"\033[0;31mFormatter task failed: {e}\033[0m")

    try:
        lint(ctx)
    except subprocess.SubprocessError as e:
        print(f"\033[0;31mLint task failed: {e}\033[0m")

    try:
        test(ctx)
    except subprocess.SubprocessError as e:
        print(f"\033[0;31mTest task failed: {e}\033[0m")

    try:
        clean(ctx)
    except subprocess.SubprocessError as e:
        print(f"\033[0;31mClean task failed: {e}\033[0m")

    print("\033[0;32m|| ALL TASKS EXECUTED (WITH LOGGED ERRORS) ||\033[0m\n")
