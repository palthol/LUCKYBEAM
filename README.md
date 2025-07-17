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

`lbeam` provides several commands to search for files and manage configurations.

### Basic Search

To search for files containing one or more keywords:

```bash
# Search for files containing "dashboard" and "api"
lbeam search dashboard api

# Search recursively through subdirectories
lbeam search my_function -r

# Search only within .py files
lbeam search "import os" --ext .py

# Use a regular expression to find a pattern
lbeam search "User\d+" --regex
```

### Using Presets

Presets are pre-configured searches.

```bash
# List all available presets
lbeam list-presets

# Run the built-in 'WebDev' preset
lbeam preset WebDev
```

### Configuration

You can view and set configuration values, though this feature is currently basic. The configuration is stored at `~/.config/lbeam/config.toml`.

```bash
# Example of setting a config value (for future use)
lbeam config my-preset-name '{"keywords": ["foo", "bar"]}'
```

---

This project is licensed under the MIT License.