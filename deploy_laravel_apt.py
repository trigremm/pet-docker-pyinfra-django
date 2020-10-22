from pyinfra import host
from pyinfra.operations import apt, server, files

SUDO = False

apt.packages(
        name='Install utilities',
        packages=['curl', 'git', 'unzip', 'vim', 'wget'],
        update=True,
    )

apt.packages(
        name='Install php7.2',
        packages=['php7.2', 'php7.2-dom', 'php7.2-gd', 'php7.2-zip', 'php7.2-cli', 'php7.2-mbstring'],
        update=True,
    )

apt.packages(
        name='Install nodejs',
        packages=['nodejs', 'npm'],
        update=True,
    )

apt.packages(
        name='Install composer',
        packages=['composer'],
        update=True,
    )

# put id_rsa, known_hosts
# clone git
# build 
# run server

__key = open('files/id_rsa').read()
__hosts = open('files/known_hosts').read()
__env = open('files/.env').read()
__git = open('files/git').read()
__dir = open('files/dir').read()

cmd = f'''
mkdir -p ~/.ssh/ 
echo "{__key}" > ~/.ssh/id_rsa
chmod 600 ~/.ssh/id_rsa
echo "{__hosts}" > ~/.ssh/known_hosts
'''
server.shell(
    name='put id_rsa and know_hosts',
    commands=cmd,
)

cmd = f'''
cd ~
if [ ! -d {__dir} ]
then
    git clone {__git}
else
    cd {__dir}
    git pull 
fi
# git clone {__git}
'''
server.shell(
    name='clone git',
    commands=cmd,
)

cmd = f'''
cd ~/{__dir}/
composer install
'''
server.shell(
    name='cd and composer install',
    commands=cmd,
)

cmd = '''
cd ~
curl https://deb.nodesource.com/setup_12.x | bash - 
apt-get install -y nodejs
'''
server.shell(
    name='Install nodejs',
    commands=cmd,
)


cmd = f'''
cd ~/{__dir}/
npm install 
'''
server.shell(
    name='npm install',
    commands=cmd,
)

cmd = f'''
cd ~/{__dir}/
npm run prod 
'''
server.shell(
    name='npm run prod ',
    commands=cmd,
)


cmd = f'''
cd ~/{__dir}/
echo "{__env}" > .env
php artisan key:generate
php artisan serve --port=80 --host=0.0.0.0 &
'''
server.shell(
    name='upload .env, key:generate and serve ',
    commands=cmd,
)