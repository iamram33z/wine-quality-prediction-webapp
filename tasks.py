from invoke import task

PACKAGE_NAME = "wine-quality-prediction-webapp"
PYTHON = "python"
PIP = "pip"

@task
def install(ctx):
    """Install dependencies"""
    print("\033[0;34mInstalling dependencies...\033[0m")
    ctx.run(f"{PIP} install -r requirements.txt")
    print("\033[0;32mDependencies installed.\033[0m\n")

@task
def test(ctx):
    """Run tests"""
    print("\033[0;34mRunning tests...\033[0m")
    ctx.run("pytest --cov=source tests/")
    print("\033[0;32mTests completed.\033[0m\n")

@task
def lint(ctx):
    """Lint code"""
    print("\033[0;34mLinting code...\033[0m")
    ctx.run("pylint source")
    print("\033[0;32mLinting completed.\033[0m\n")

@task
def format(ctx):
    """Format code"""
    print("\033[0;34mFormatting code...\033[0m")
    ctx.run("black source")
    ctx.run("isort source")
    print("\033[0;32mFormatting completed.\033[0m\n")

@task
def run(ctx):
    """Run application"""
    print("\033[0;34mRunning application...\033[0m")
    ctx.run(f"{PYTHON} main.py")
    print("\033[0;32mApplication running.\033[0m\n")

@task
def clean(ctx):
    """Clean up temporary files"""
    print("\033[0;34mCleaning up...\033[0m")
    ctx.run("del /s /q *.pyc", warn=True)  # Windows delete command
    ctx.run("for /d %p in (__pycache__) do rmdir /s /q %p", warn=True)
    print("\033[0;32mCleanup completed.\033[0m\n")
