*************
file_to_bitmap 
*************

Convert any file to a bitmap and back again. The resulting bitmap is be a visual representation of the original file. The last pixel contains the size of the original file.


For example, consider this most glorious of audio examples:

.. image:: http://nullsum.net/example.bmp
    :alt: Maybe you should try listening this...
    :width: 400
    :height: 229
    :align: center


**Python 3 only.**


To a bitmap:

.. code-block:: bash

    $ python3 file_to_bitmap.py to input.file output.bmp


To the original file:

.. code-block:: bash

    $ python3 file_to_bitmap.py from input.bmp output.file
