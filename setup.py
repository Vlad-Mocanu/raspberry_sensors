# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='raspberry_sensors',
    version='1.0.0',
    description='Experimenting with IoT (Internet of Things) for Raspberry Pi ',
    long_description=long_description,
    url='https://github.com/Vlad-Mocanu/raspberry_sensors',
    author='Vlad Mocanu',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache 2.0 License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='raspberrypi iot sensors',
	install_requires=[
		'RPi.GPIO>=0.6.2',
		'Adafruit-GPIO>=0.6.5',
		'PyMySQL>=0.7.6'	
	]
)
