from setuptools import setup

setup(
    name='plz_plot',
    version='0.1.0',
    description='Plot data on a map using cartopy and german postal codes',
    url='http://github.com/MaxNoe/plz_plot',
    author='Maximilian Noethe',
    author_email='maximilian.noethe@tu-dortmund.de',
    license='MIT',
    packages=[
        'plz_plot',
    ],
    package_data={
        '': [
            'resources/*',
        ]
    },
    python_requires='>=3.6',
    tests_require=['pytest>=3.0.0'],
    setup_requires=['pytest-runner'],
    install_requires=[
        'numpy',
        'cartopy',
        'matplotlib>=1.5',
        'pandas',
    ],
    zip_safe=False,
)
