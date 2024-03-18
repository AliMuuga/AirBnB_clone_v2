#!/usr/bin/python3
"""
This script generates a compressed tar archive (tgz) from the contents of the web_static
directory in the AirBnB Clone repository.
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir as is_directory


def create_archive():
    """Creates a compressed tar archive."""
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        if not is_directory("versions"):
            local("mkdir versions")
        archive_name = "versions/web_static_{}.tgz".format(current_time)
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception as e:
        print("An error occurred:", e)
        return None

if __name__ == "__main__":
    result = create_archive()
    if result:
        print("Archive created:", result)
    else:
        print("Archive creation failed.")

