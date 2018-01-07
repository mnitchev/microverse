from setuptools import setup, find_packages


setup(
    name='microverse',
    version='0.1',
    packages=find_packages(),
    install_requires=['numpy>=1.11.1'],
    author='Mario Nitchev & Iliya Zhechev',
    author_email='mail@ala.bala',
    description='Genetic algorithms training neural networks',
    license='MIT',
    keywords='simulation, genetic, algorithm, neural network',
    url='https://github.com/mnitchev/microverse',
    test_suite='tests'
)
