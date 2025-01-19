# Variables
PACKAGE_NAME=wine-quality-prediction-webapp
PYTHON=python3
PIP=pip3

# Colors
BLUE=\033[0;34m
GREEN=\033[0;32m
NC=\033[0m # No Color

# Commands
install:
	@echo "$(BLUE)Installing dependencies...$(NC)"
	$(PIP) install -r requirements.txt
	@echo "$(GREEN)Dependencies installed.$(NC)\n"

test:
	@echo "$(BLUE)Running tests...$(NC)"
	pytest --cov=source tests/
	@echo "$(GREEN)Tests completed.$(NC)\n"

lint:
	@echo "$(BLUE)Linting code...$(NC)"
	pylint source
	@echo "$(GREEN)Linting completed.$(NC)\n"

format:
	@echo "$(BLUE)Formatting code...$(NC)"
	black source
	isort source
	@echo "$(GREEN)Formatting completed.$(NC)\n"

run:
	@echo "$(BLUE)Running application...$(NC)"
	$(PYTHON) main.py
	@echo "$(GREEN)Application running.$(NC)\n"

clean:
	@echo "$(BLUE)Cleaning up...$(NC)"
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	@echo "$(GREEN)Cleanup completed.$(NC)\n"

.PHONY: install test lint format run clean