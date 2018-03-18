import setuptools


setuptools.setup(
    name='bmp-transcode',
    version='0.3.0',
    description='Transcode orindary files to and from bitmap images.',
    long_description=open('README.rst').read(),
    author='Andrew Rabert',
    author_email='arabert@nullsum.net',
    url='https://github.com/nvllsvm/bmp-transcode',
    license='Apache 2.0',
    packages=['bmp_transcode'],
    install_requires=['pillow'],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3 :: Only'
    ),
    entry_points={
        'console_scripts': ['bmp-transcode=bmp_transcode:main']
    }
)
