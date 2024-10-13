from pathlib import Path

parent_folder = str(Path(__file__).parent.parent)
CONFIG_FILE_PATH = Path(f"{parent_folder}/src/config.yaml")
PARAMS_FILE_PATH = Path(f"{parent_folder}/src/models_module_def/params.yaml")
SCHEMA_FILE_PATH = Path(f"{parent_folder}/src/data_module_def/schema.yaml")