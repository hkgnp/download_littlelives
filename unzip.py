import os
import subprocess

for filename in os.scandir("."):
    if filename.is_file():
        subprocess.run(["unzip", filename])
