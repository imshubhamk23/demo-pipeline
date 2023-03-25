from setuptools import setup,find_packages

setup(name="census-income",
      version="0.0.1",
      author="shubham",
      author_email="shubham@mail.com",
      packages=find_packages(),
      install_requires = ["pandas","numpy","flask"]
      )