import subprocess
import os

def nvcc():
    "checks nvcc version"
    lines = subprocess.check_output(['nvcc', '--version']).decode('utf-8').splitlines()
    res = False
    for line in lines:
        if "release "+os.environ['PKG_VERSION'] in line:
            res = True
            break

    return res

assert nvcc()
