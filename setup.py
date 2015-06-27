from setuptools import setup
import magnetor

setup(
    name='magnetor',
    version=magnetor.__version__,
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
