import os
import subprocess

def run_command(command):
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e.stderr.decode('utf-8')}")
