# Define the requirements file
REQUIREMENTS = requirements.txt

# Build the application
.PHONY: build
build: install
	@echo "Building..."
	@echo "TODO: Implement!"

# Run the application
.PHONY: run
run: install
	@echo "Running the application..."
	python src/day2.py

# Install dependencies
.PHONY: install
install:
	@echo "Installing dependencies..."
	pip3 install -r $(REQUIREMENTS)

# Run tests
.PHONY: test
test:
	@echo "Running tests..."
	python -m unittest -v 

# Clean up
.PHONY: clean
clean:
	@echo "Cleaning up..."
	@rm -rf *.pyc __pycache__ .pytest_cache
