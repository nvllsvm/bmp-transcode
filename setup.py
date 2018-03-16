import setuptools


setuptools.setup(
    name='bmp-transcode',
    version='0.2.0',
    description='Transcode binary data to or from a bitmap image.',
    long_description=open('README.rst').read(),
    author='Andrew Rabert',
    author_email='arabert@nullsum.net',
    url='https://github.com/nvllsvm/bmp-transcode',
    license='Apache 2.0',
    packages=['bmp_transcode'],
    install_requires=['pillow'],
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3 :: Only'
    ),
    entry_points={
        'console_scripts': ['bmp-transcode=bmp_transcode:main']
    }
)
