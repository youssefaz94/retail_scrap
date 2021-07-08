import subprocess
from setuptools import setup, find_packages
from setuptools.command.install import install


INSTALL_REQUIREMENTS = [
"jsonlines",
"elasticsearch",
"bs4",
"flask"
]


# class InstallCommand(install):
#     """
#     will call activate githooks for install mode
#     """
#     def run(self):
#         install.run(self)


setup(name='nelson',
      packages=find_packages(),
      package_data={'': ['*.sql', '*.json']},
      author='Youssef Azzouz',
      author_email='youssef.azzouz1512@gmail.com',
      version='0.1.0',
      zip_safe=False,
      classifiers=[
        'Topic :: Software Development',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
      entry_points={
          'console_scripts': ['nelson = src.__main__:main']
      },
      install_requires=INSTALL_REQUIREMENTS,
      tests_require=["pytest", ],
      include_package_data=True
      )