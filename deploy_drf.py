from pyinfra import host
from pyinfra.operations import pip, server

pip.packages(
    name='Install django using pip',
    pip='pip3',
    packages='django',
)

pip.packages(
    name='Install djangotestframework using pip',
    pip='pip3',
    packages='djangorestframework',
)

pip.packages(
    name='Install django pwa using pip',
    pip='pip3',
    packages='django-progressive',
)

server.shell(
    name='Create django project mysite',
    commands='cd ~; django-admin startproject mysite',
)