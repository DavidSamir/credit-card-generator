from __future__ import unicode_literals
from os.path import abspath, join, dirname
import random


__name__ = 'ccard'
__title__ = 'ccard'
__version__ = '0.1.5'
__author__ = 'David Samir'
__email__ = 'dsamir@davidsamir.com'
__link__ = 'https://github.com/davidsamir/credit-card-generator/'
__info__ = 'credit card generator'
__email__ = 'dsamir@davidsamir.com'
__license__ = 'MIT'


full_path = lambda filename: abspath(join(dirname(__file__), filename))


FILES = {
    'visa': full_path('visa'),
    'discover': full_path('discover'),
    'mastercard': full_path('mastercard'),
    'americanexpress': full_path('americanexpress'),
}


def get_number(filename):
    selected = random.random() * 30000
    with open(filename) as name_file:
        for index,line in enumerate(name_file):
            if index > selected:
                return int(line)
    return ''  # Return empty string if file is empty

def visa():
    return get_number(FILES['visa'])

def discover():
    return get_number(FILES['discover'])

def mastercard():
    return get_number(FILES['mastercard'])

def americanexpress():
    return get_number(FILES['americanexpress'])