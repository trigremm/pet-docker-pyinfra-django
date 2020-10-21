from pyinfra import host
from pyinfra.operations import apt

SUDO = False

apt.packages(
        name='Install python',
        packages=['python3', 'python3-pip'],
        update=True,
    )