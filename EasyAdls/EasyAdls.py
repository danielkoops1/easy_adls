"""
name        EasyAdls
author      D. Koops
"""

import io
import logging
import pandas as pd
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ClientAuthenticationError


class EasyBlob:
    """ Wrapper for easy interaction with ADLS """

    def __init__(self, account_name, container, credential):

        self.client = BlobServiceClient(account_url=f"https://{account_name}"
                                                    f".blob.core.windows.net/",
                                        credential=credential)
        self.container = container

        try:
            self.client.get_account_information()
            print(f'Successfully connected to {self.client.url}')

        except ClientAuthenticationError as error:
            logging.error(f'Unable to connect to {self.client.url}:\n{error}')

    def get_properties(self, blob_path):
        """ Retrieve file properties """

        blob = self.client.get_blob_client(self.container, blob_path)

        return blob.get_blob_properties()

    def read_blob_to_string(self, blob_path):
        """ Read a text (blob)file into a string """

        blob = self.client.get_blob_client(self.container, blob_path)
        blob_data = blob.download_blob()

        return blob_data.readall().decode()

    def read_blob_to_bytes(self, blob_path):
        """ Read a binary (blob)file into a bytestring """

        blob = self.client.get_blob_client(self.container, blob_path)
        blob_data = blob.download_blob()

        return blob_data.readall()

    def read_textfile_to_io(self, blob_path):
        """ Read a text (blob)file into a StringIO object """

        blob = self.client.get_blob_client(self.container, blob_path)
        blob_data = blob.download_blob()

        return io.StringIO(blob_data.readall().decode())

    def read_binary_to_io(self, blob_path):
        """ Read a binary (blob)file into a BytesIO object """

        blob = self.client.get_blob_client(self.container, blob_path)
        blob_data = blob.download_blob()

        return io.BytesIO(blob_data.readall())

    def read_csv_to_pandas(self, blob_path, **kwargs):
        """ Read a csv (blob)file into a pandas dataframe
         You can pass arguments down to the pd.read_csv() function """

        blob = self.client.get_blob_client(self.container, blob_path)
        blob_data = blob.download_blob()
        buffer = io.StringIO(blob_data.readall().decode())

        return pd.read_csv(buffer, **kwargs)

    def write_pandas_to_csv(self, pandas_dataframe, blob_path, overwrite=False, **kwargs):
        """ Read a csv (blob)file into a pandas dataframe
         You can pass arguments down to the pd.read_csv() function """

        blob = self.client.get_blob_client(self.container, blob_path)

        return blob.upload_blob(pandas_dataframe.to_csv(**kwargs), overwrite=overwrite)

    def write_content_to_blob(self, blob_path, content, overwrite=False):
        """ Write a string or bytes to a blob """

        blob = self.client.get_blob_client(self.container, blob_path)

        return blob.upload_blob(content, overwrite=overwrite)

    def download_blob(self, blob_path, local_file):
        """ Download a blob to a local file """

        blob = self.client.get_blob_client(self.container, blob_path)

        with open(local_file, 'wb') as data:
            blob_data = blob.download_blob()
            return blob_data.readinto(data)

    def upload_blob(self, local_file, blob_path, overwrite=False):
        """ Upload a local file to blob """

        blob = self.client.get_blob_client(self.container, blob_path)

        with open(local_file, 'rb') as data:
            return blob.upload_blob(data, overwrite=overwrite)
