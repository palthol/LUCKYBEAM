# lbeam ⚡

A fast, preset-driven file finder for the command line. `lbeam` helps you quickly find files containing specific keywords using predefined or custom search criteria.

## Installation

You can install `lbeam` using pip:

```bash
pip install .
```

If you are developing the tool, install it in editable mode with testing dependencies:

```bash
pip install -e .[test]
```

## Usage

`lbeam` provides several commands to search for files and manage presets.

### Quick Search (`ff`)

For the most common use case, use the `ff` command as a direct shortcut for a keyword search.

```bash
# Find all files containing "routes"
ff routes

# Search recursively for "api" only in .py files
ff api -r --ext .py
```

### Full Command (`lbeam`)

The `lbeam` command gives you access to all features, including presets.

#### Basic Search

```bash
# Search for files containing "dashboard" and "api"
lbeam search dashboard api

# Use a regular expression to find a pattern
lbeam search "User\d+" --regex
```

#### Preset Management

Presets are pre-configured searches. You can use built-in presets or create your own.

```bash
# List all available presets (built-in and custom)
lbeam preset list

# Run the built-in 'WebDev' preset
lbeam preset run WebDev

# Create a new custom preset called 'logs'
lbeam preset add logs -k "ERROR" -k "WARN" --ext .log

# Run your new custom preset
lbeam preset run logs

# Remove a custom preset
lbeam preset rm logs
```

---