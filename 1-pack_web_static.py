#!/usr/bin/python3
""" Compress before sending """
from fabric.api import *
import os
from datetime import datetime


def do_pack():
    """
        script that generates a .tgz archive
            from the contents of the web_static
    """
    # create version directory os.mkdir()
    if not os.path.isdir("versions"):
        local("mkdir versions")

    now = datetime.now()
    version = f"""{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}"""

    # create tar.gz file
    local(f"tar -czvf versions/web_static_{version}.tgz web_static")
    if os.path.exists(f"/verions/web_static_{version}.tgz"):
        os.path.normpath(f"/verions/web_static_{version}.tgz")
    else:
        return None
