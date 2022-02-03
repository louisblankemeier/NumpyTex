from setuptools import setup, find_packages

setup(
    name='NumpyTex',
    version='0.0.1',    
    description='Generates latex table scripts using a numpy array as input',
    url='https://github.com/louisblankemeier/NumpyTex',
    author='Louis Blankemeier',
    author_email='lblankem@stanford.edu',
    install_requires=['numpy'],
    packages=find_packages(),
)
