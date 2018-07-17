from setuptools import setup, find_packages
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(levelname)-8s [%(filename)s:%(lineno)-3d] %(message)s',
                    datefmt='%d-%m-%Y:%H:%M:%S',
                    level=logging.INFO)
logger.setLevel(logging.INFO)

setup(name='cp_solver',
      version='0.0.1',
      python_requires='>=3.5.*',
      packages=find_packages(),

      # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 3 - Alpha',

          # Indicate who your project is intended for
          'Environment :: Console',
          # 'Topic :: Software Development :: Build Tools',
          'Intended Audience :: Science/Research',
          'Operating System :: OS Independent',

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Cython',

          'Programming Language :: Python',
          # 'Programming Language :: Python :: 2',
          # 'Programming Language :: Python :: 2.6',
          # 'Programming Language :: Python :: 2.7',
          # 'Programming Language :: Python :: 3',
          # 'Programming Language :: Python :: 3.2',
          # 'Programming Language :: Python :: 3.3',
          # 'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',

          'Topic :: Scientific/Engineering',

      ],

      # What does your project relate to?
      keywords='cp csp constraint solving problems problem solver',


      test_suite='pytest',
      install_requires=[
      ],
      tests_require=[
          'pytest',
          'pytest-timeout'
      ],
      )
