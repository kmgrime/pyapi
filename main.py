# Import FastAPI framework for creating the REST API
from fastapi import FastAPI
# Import PyYAML library for reading YAML files
import yaml
# Import Path for handling file paths
from pathlib import Path

# Create a FastAPI application instance
app = FastAPI()

# Define the configs directory path
CONFIGS_DIR = Path("configs")

# Define a GET endpoint that reads all configs from the directory
@app.get("/configs")
async def get_configs():
    # Dictionary to store all configurations
    all_configs = {}
    
    # Read each YAML file in the configs directory
    for config_file in CONFIGS_DIR.glob("*.yaml"):
        with open(config_file, 'r') as file:
            # Use the filename (without .yaml) as the key
            config_name = config_file.stem
            all_configs[config_name] = yaml.safe_load(file)
    
    return all_configs
