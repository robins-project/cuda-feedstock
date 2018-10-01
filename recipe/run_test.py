from shutil import which
import subprocess
import os

def nvcc():
    "checks nvcc version"
    version = "0"
    if which('nvcc') is not None:
        lines = subprocess.check_output(['nvcc', '--version']).decode('utf-8').splitlines()
        for line in lines:
            if line.startswith("Cuda compilation tools"):
                # Cuda compilation tools, release 9.2, V9.2.148
                version = line.split()[-1][1:]
                break

    return version

assert nvcc() == os.environ['PKG_VERSION']
