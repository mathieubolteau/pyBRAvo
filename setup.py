from setuptools import setup, find_packages

setup(name='pyBravo',
    entry_points={
          'console_scripts': [
              'pybravo=pyBRAvo.src.pyBravo:main',
          ]
      },
      include_package_data=True,
      package_data={
      'bravo': ['*.gene_info'],
   }
)