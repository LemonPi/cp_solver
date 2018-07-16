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
      test_suite='pytest',
      install_requires=[
      ],
      tests_require=[
          'pytest',
      ],
      )
