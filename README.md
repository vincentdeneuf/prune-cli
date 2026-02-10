# prune

A CLI tool named prune for cleaning Python code.

## Installation

```bash
pip install prune-cli
```

## Usage

```bash
prune <command> [options]
```

### Commands

- `prune comments` - Remove comments from Python files
- `prune prints` - Remove print statements from Python files  
- `prune docstrings` - Remove docstrings from Python files
- `prune asserts` - Remove assert statements from Python files
- `prune logs` - Remove logging statements from Python files

### Examples

```bash
# Remove all print statements
prune prints

# Remove inline comments only (preserve noqa, type:, pragma)
prune comments --default

# Remove all types of comments
prune comments --all

# Remove specific log levels
prune logs --debug --info --error

# Remove all log levels
prune logs --all

# Show per-file details (verbose is default)
prune prints

# Suppress per-file output
prune prints --quiet
```

## Development

This project uses a src-layout packaging structure.

### Requirements

- Python >= 3.11
- LibCST

## License

MIT License
