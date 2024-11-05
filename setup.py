import io
import os
import setuptools
import shutil
import tempfile

# Function to get dependencies (you can customize this)
def get_dependencies():
    return ["aiohttp>=3.8.1"]

current_dir = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(current_dir, "README.md"), encoding="utf-8") as fd:
    desc = fd.read()

env_dir = tempfile.mkdtemp(prefix="webscout-install-")
shutil.copytree(os.path.abspath(os.getcwd()), os.path.join(env_dir, "webscout"))

os.chdir(env_dir)

setuptools.setup(
    name="webscout",
    version="1.0.0",
    author="HackerJacke",
    author_email="Bilaleljihani1@gmail.com",
    description="Advanced web path scanner",
    long_description=desc,
    long_description_content_type="text/markdown",
    url="https://github.com/hackerjacke440",
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["webscout=webscout:main"]},
    include_package_data=True,
    python_requires=">=3.9",
    install_requires=get_dependencies(),
    classifiers=[
        "Programming Language :: Python",
        "Environment :: Console",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Programming Language :: Python :: 3.9",
    ],
    keywords=["infosec", "bug bounty", "pentesting", "security"],
)
