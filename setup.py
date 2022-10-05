import setuptools

setuptools.setup(
    name="EasyAdls",
    version="0.1.0",
    author="D. Koops",
    description="Wrapper around the Azure Storage Blobs SDK to make life a bit easier",
    url='https://github.com/danielkoops1/easy_adls',
    install_requires=[
        'pandas>=1.2.4',
        'azure-storage-blob>=12.13.1',
          ],
    python_requires='>=3.6',
)
