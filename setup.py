from setuptools import setup

install_requires = [
    'requests',
    'beautifulsoup4'
]

setup(
    name='magnetor',
    install_requires=install_requires,
    version=0.2,
    description='Get magnet links for torrents from the CLI',
    author='Asad Dhamani',
    author_email='dhamaniasad+code@gmail.com',
    url='https://github.com/dhamaniasad/magnetor',
    license='Unlicense',
    py_modules=['magnetor'],
    entry_points={
        'console_scripts': [
            'magnetor = magnetor:command_line_runner'
        ]
    }
)
