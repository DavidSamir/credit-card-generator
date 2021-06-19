ccard
=====

Fake credit-card generator
is a Python 3 Package for TESTING PURPOSES AND DATA VERIFICATION ONLY!
Instead of using a real credit card
this tool will help you generate a vaild credit card numbers
Giving you the option to generate the following type of credit card

```
Visa
Discover
Master Card
American Express
```


Installation
------------

The script is `available on PyPI`_.  To install with pip::

    pip install ccard


Usage
-----

credit-card generator can be used as a command line utility or imported as a Python package.


Command Line Usage
~~~~~~~~~~~~~~~~~~
To use the script from the command line:
the defualt value is Visa
.. code-block:: bash

    $ ccard
    4916232538105515

Python Package Usage
~~~~~~~~~~~~~~~~~~~~
Here are examples of all current features:

.. code-block:: pycon

    >>> import ccard
    >>> ccard.visa()
    4485610834415848
    >>> ccard.discover()
    6011017754491148
    >>> ccard.mastercard()
    5179703192884719
    >>> ccard.americanexpress()
    374300139079794

License
-------

This project is released under an `MIT License`_.

.. _mit license: http://th.mit-license.org/2013
.. _available on PyPI: http://pypi.python.org/pypi/ccard/
