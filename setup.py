from setuptools import setup, find_packages


def open_requirements_file():
    with open('requirements.txt', 'r') as f:
        return f.readlines()


def get_requirements():
    reqs = open_requirements_file()
    print(reqs)
    return reqs


setup(
    name='market',
    version='0.0.1',
    author='João Ricardo',
    author_email='joaoricardosimplicio16@gmail.com',
    packages=find_packages(include=['market', 'market.*']),
    install_requires=get_requirements(),
        entry_points={
        'console_scripts': ['market=market.market:main']
    }
)
