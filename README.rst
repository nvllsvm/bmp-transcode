*************
file_to_image 
*************

Convert any file to a bitmap and back again. The resulting bitmap is be a visual representation of the original file. The last pixel contains the size of the original file.

To a bitmap:

.. code-block:: bash

    $ python file_to_image.py to input.file output.bmp


To the original file:

.. code-block:: bash

    $ python file_to_image.py from input.bmp output.file
