bmp-transcode
=============

|PyPi Version|

Convert any file to a bitmap and back again. The resulting bitmap is a visual representation of the original file. The last pixel contains the size of the original file.


For example, this is an mp3 hosted by a popular image host.

.. image:: https://i.imgur.com/jYjNcEY.png
    :alt: Maybe you should try listening this...

Installation
------------

Python 3 only.

.. code:: shell

    $ pip install bmp-transcode

Usage
-----

To a bitmap:

.. code:: shell

    $ bmp-transcode to input.file output.bmp


To the original file:

.. code:: shell

    $ bmp-transcode from input.bmp output.file


.. |PyPi Version| image:: https://img.shields.io/pypi/v/bmp_transcode.svg?
   :target: https://pypi.python.org/pypi/bmp_transcode
