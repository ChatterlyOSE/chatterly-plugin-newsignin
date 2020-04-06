  
#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='reddit_auth',
    description='reddit auth',
    version='0.1',
    author='Ryan Norris',
    author_email='ryan.norris@roxxonusa.com',
    packages=find_packages(),
    install_requires=[
        'r2',
    ],
    extras_require={
        'stats': ['google-api-python-client'],
    },
    entry_points={
        'r2.plugin':
            ['about = reddit_auth:Auth']
    },
    include_package_data=True,
    zip_safe=False,
)