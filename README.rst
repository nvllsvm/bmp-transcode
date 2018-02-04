bmp-transcode
=============

Convert any file to a bitmap and back again. The resulting bitmap is a visual representation of the original file. The last pixel contains the size of the original file.


For example, consider this most glorious of audio examples:

.. image:: https://raw.githubusercontent.com/nvllsvm/bmp-transcode/master/example.bmp
    :alt: Maybe you should try listening this...


**Python 3 only.**


To a bitmap:

.. code:: shell

    $ bmp-transcode to input.file output.bmp


To the original file:

.. code:: shell

    $ bmp-transcode from input.bmp output.file
