*************
file_to_image 
*************

Convert any file to a bitmap and back again. The resulting bitmap is be a visual representation of the original file. The last pixel contains the size of the original file.


.. image:: http://nullsum.net/example.bmp
    :alt: Maybe you should try listening this...
    :width: 400
    :height: 229
    :align: center


To a bitmap:

.. code-block:: bash

    $ python file_to_image.py to input.file output.bmp


To the original file:

.. code-block:: bash

    $ python file_to_image.py from input.bmp output.file
