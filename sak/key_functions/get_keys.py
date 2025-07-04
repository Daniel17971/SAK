import os

def get_key(path: str, relative_path: bool=True) -> str:
    
    if relative_path:
        full_path =f"{os.getcwd()}/{path}"

    else:
        full_path = path

    with open(full_path,"r") as file:
        key = file.read().strip()

    return key

def get_multiple_keys(path: str, relative_path: bool=True) -> list[str] | dict:
    keys = []
    if relative_path:
        full_path = f"{os.getcwd()}/{path}"
    else:
        full_path = path

    with open(full_path, "r") as file:
        keys = [
            {line.split("=")[0].strip():line.split("=")[1].strip()}
            for line in file if "=" in line and line.strip()
        ]

    if len(keys) == 1:
        return keys[0]
    return keys