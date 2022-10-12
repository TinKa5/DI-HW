"""
Layer of persistence. Save content to outer warld here.
"""
import json
import os
import glob


def save_to_disk(json_content, path, filename):
    path = os.path.normpath(os.path.join(path, filename))
    clear_dir(path)

    with open(path, 'w') as my_resp:
        print(json.dumps(json_content), file=my_resp)


def clear_dir(dir_path):
    files = glob.glob(dir_path + "/*")
    for f in files:
        os.remove(f)
