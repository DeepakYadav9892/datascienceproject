##use for common utitlity functions across the project
import os
import yaml
from src.data_science_project import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from pathlib import Path
from box.exceptions import BoxValueError, BoxKeyError

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object

    Args:
        path_to_yaml (Path): Path to the yaml file

    Returns:
        ConfigBox: ConfigBox object containing the yaml file data
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise BoxValueError("yaml file is empty")
    except BoxKeyError as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """Create list of directories

    Args:
        path_to_directories (list): List of directory paths
        ingnore_log (bool, optional):  Ingnore logging if multiple directories is to be created .
        Defaults to True"""
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path:Path,data:dict):
    """Saves a dictionary to a json file

    Args:
        path (Path): Path to the json file
        data (dict): Data to be saved
    """
    with open(path,'w') as f:
        json.dump(data,f,indent=4)
    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path:Path)->ConfigBox:
    """Load json files data 
    Args:
    Path(Path):Path to json file 

    Returns:
    ConfigBox:data as class attributes instead of dict 
    """
    with open(path) as f:
        content=json.load(f)
    logger.info(f"json file loaded successfully from:{path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any,path:Path):
    """
    Save binary file 

    Args:
    Data (Any):data to be saved as binary 
    path(Path): path to binary file 
    
    """
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at:{path}")

@ensure_annotations
def laod_bin(path:Path)->Any:
    """Load binary data 
    
    Args:
    Path (Path): Path to binary file 
    Returns:
    ANy: object stored in the file """
    data=joblib.load(path)
    logger.info(f"binary file loaded from:{path}")
    return data



        