# Root-level Makefile

# Discover all subdirectories, excluding those that start with a dot (.)
YEARS := $(wildcard */)
YEARS := $(filter-out %/., $(YEARS))  # Exclude directories starting with a dot
YEARS := $(patsubst %/, %, $(YEARS))  # Remove the trailing slash from the directory names

# Default rule to run all sub-projects
.PHONY: install
install: $(YEARS)
	@for year in $(YEARS); do \
	    echo "Running make for $$year..."; \
	    make -C $$year install; \
	done
	@echo "All projects have been processed!"

# Test all sub-projects
.PHONY: test
test: $(YEARS)
	@echo "Running tests for all years..."
	@for year in $(YEARS); do \
	    echo "Running tests for $$year..."; \
	    make -C $$year test; \
	done

# Clean all sub-projects
.PHONY: clean
clean:
	@echo "Cleaning all projects..."
	@for year in $(YEARS); do \
	    echo "Cleaning $$year..."; \
	    make -C $$year clean; \
	done

# Dynamic rules for each year
$(YEARS):
	@echo "Running Makefile for $$@..."
	@make -C $$@

# Print the list of discovered years (directories)
.PHONY: debug
debug:
	@echo "Discovered years (space separated): $(YEARS)"
