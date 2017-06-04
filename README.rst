*************
file_to_bitmap 
*************

Convert any file to a bitmap and back again. The resulting bitmap is a visual representation of the original file. The last pixel contains the size of the original file.


For example, consider this most glorious of audio examples:

.. image:: https://raw.githubusercontent.com/nvllsvm/file_to_bitmap/master/example.bmp
    :alt: Maybe you should try listening this...


**Python 3 only.**


To a bitmap:

.. code-block:: bash

    $ python3 file_to_bitmap.py to input.file output.bmp


To the original file:

.. code-block:: bash

    $ python3 file_to_bitmap.py from input.bmp output.file
