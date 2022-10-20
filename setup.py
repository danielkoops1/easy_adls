import os
import setuptools

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setuptools.setup(
    name="EasyAdls",
    version="0.1.3",
    author="D. Koops",
    description="Wrapper around the Azure Storage Blobs SDK to make life a bit easier",
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/danielkoops1/easy_adls',
    install_requires=[
        'pandas>=1.2.4',
        'azure-storage-blob>=12.13.1',
          ],
    python_requires='>=3.6',
)
