from pyinfra import host
from pyinfra.operations import apt, server, files

SUDO = False

files.put(
    'dockerfile', 
    'dockerfile', 
    )
