import glob2
import os
import sys
from pathlib import Path

rootPathTrain = "./dataset/train"
rootPathValid = "./dataset/valid"
rootPathTest= "./dataset/test"

jpg_files = [f for f in glob2.glob(rootPathTrain + "/**/*.jpg", recursive=True)]
TRAIN_FILE = "./train.txt"
VALID_FILE = "./val.txt"
TEST_FILE = "./test.txt"

with open (TRAIN_FILE, "w") as train_file:
    train_file.write("\n".join(str(item) for item in jpg_files))

jpg_files = [f for f in glob2.glob(rootPathValid + "/**/*.jpg", recursive=True)]
with open (VALID_FILE, "w") as valid_file:
    valid_file.write("\n".join(str(item) for item in jpg_files))

jpg_files = [f for f in glob2.glob(rootPathTest + "/**/*.jpg", recursive=True)]
with open (TEST_FILE, "w") as test_file:
    test_file.write("\n".join(str(item) for item in jpg_files))



    