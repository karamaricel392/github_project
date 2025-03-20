import os
import glob
import shutil

def clean_up():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    dirs = [f for f in os.listdir('.') if os.path.isdir(f)]

    for file in files:
        try:
            os.remove(file)
        except FileNotFoundError:
            print("Failed to delete file: " + file)
    
    for dir in dirs:
        shutil.rmtree(dir)

clean_up()
