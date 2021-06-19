import ccard
from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CONTRIBUTING.rst') as contributing_file:
    contributing = contributing_file.read()


setup(
    name=ccard.__name__,
    ccard=ccard.__title__,
    version=ccard.__version__,
    author=ccard.__author__,
    author_email=ccard.__email__,
    url=ccard.__link__,
    description=ccard.__info__,
    long_description='\n\n'.join((
        readme,
        contributing,
    )),
    license=ccard.__license__,
    packages=find_packages(),
    package_data={'ccard': ['dist.*']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'ccard = ccard.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    test_suite='test_ccard',
)
