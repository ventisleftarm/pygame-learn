from setuptools import find_packages, setup

setup(
    name="src",
    version="0.0.1",
    author="Simon Thomas",
    author_email="author@example.com",
    description="looking at Pygame, and creating some example exercises.",
    url="url-to-github-page",
    packages=find_packages(),
    test_suite="src.tests.test_all.suite",
)
