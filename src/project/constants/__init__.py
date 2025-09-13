from pathlib import Path

# 1. Detect where we are (works for both notebooks and scripts)
CURRENT_DIR = Path.cwd()

# 2. If we are inside "research", go one level up
if CURRENT_DIR.name == "research":
    PROJECT_ROOT = CURRENT_DIR.parent
else:
    PROJECT_ROOT = CURRENT_DIR

# 3. Define file paths relative to project root
CONFIG_FILE_PATH = PROJECT_ROOT / "config" / "config.yaml"
PARAMS_FILE_PATH = PROJECT_ROOT / "params.yaml"
SCHEMA_FILE_PATH = PROJECT_ROOT / "schema.yaml"
