from setuptools import setup

version = __import__('with_asserts').get_version()

setup(
    name='django-with-asserts',
    version=version,
    description='Helpers for testing Django using context managers',
    author='John Paulett',
    author_email='john@paulett.org',
    url='https://django-with-asserts.readthedocs.org',
    license='BSD',
    packages=['with_asserts'],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'lxml',
        'cssselect',  # split out of lxml.cssselect in v3.0
    ],
)
