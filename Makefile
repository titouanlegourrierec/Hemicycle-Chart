.PHONY: lint format typecheck quality

all: quality

SRC=.

lint:
	uv run ruff check --fix $(SRC)

format:
	uv run ruff format $(SRC)

typecheck:
	uv run ty check $(SRC)

quality: lint format typecheck

help:
	@echo "\033[1;36mMakefile targets:\033[0m"
	@echo "  \033[1;32mlint\033[0m     : Check code with ruff."
	@echo "  \033[1;32mformat\033[0m   : Format code with ruff."
	@echo "  \033[1;32mtypecheck\033[0m: Type check code with ty."
	@echo "  \033[1;32mquality\033[0m  : Run lint, format, and typecheck."
