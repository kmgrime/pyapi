# Import FastAPI framework for creating the REST API
from fastapi import FastAPI
# Import PyYAML library for reading YAML files
import yaml

# Create a FastAPI application instance
app = FastAPI()

# Define a function that reads and parses YAML files
def read_yaml(file_path: str):
    # Open the file in read mode using a context manager (automatically closes the file)
    with open(file_path, 'r') as file:
        # Parse the YAML content and return it as a Python dictionary
        return yaml.safe_load(file)

# Define a GET endpoint at the path "/config"
@app.get("/config")
async def get_config():
    # When this endpoint is called, read and return the contents of config.yaml
    return read_yaml('config.yaml')
