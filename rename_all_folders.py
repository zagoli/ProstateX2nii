import os
from pathlib import Path

dcm_dataset = Path("C:/Users/ML/Desktop/ProstatexJacopo/seg")
for dirpath, subdirs, files in os.walk(dcm_dataset):
    if files:
        splitted = dirpath.split('\\')
        splitted.pop(8)
        new_path = '\\'.join(splitted) + "R"
        os.rename(dirpath, new_path)
        os.rmdir(new_path[:-1])
