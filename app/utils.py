"""
Utility functions.
"""

import json
import os


def create_folder(folder):

    os.makedirs(folder, exist_ok=True)


def save_json(data, filename):

    create_folder(os.path.dirname(filename))

    with open(filename, "w", encoding="utf-8") as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )
