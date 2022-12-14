import pandas as pd
from EasyAdls import EasyBlob

# init the client with either a key or sas token
client = EasyBlob(account_name='mystorageaccount',
                  container='some-container',
                  credential='key_or_sas_token')

# retrieve properties of a blob
client.get_properties('blob.jpg')

# copy a blob
# you can specify another container if needed, default is same container
client.copy_blob('blob.jpg', 'copy_of_blob.jpg')
client.copy_blob(source_path='blob.jpg',
                 destination_path='copy_of_blob.jpg',
                 destination_container='anothercontainer')

# move-, or rename a blob
# you can specify another container if needed, default is same container
client.move_or_rename_blob('blob.jpg', 'renamed_blob.jpg')
client.move_or_rename_blob(source_path='/path/to/blob.jpg',
                           destination_path='/another/path/to/blob.jpg',
                           destination_container='anothercontainer')

# read a csv into a pandas dataframe and vice versa
# you can pass-down all arguments of pd.read_csv() and pd.to_csv()
pdf = client.read_csv_to_pandas('some.csv', header=None, sep=',')
client.write_pandas_to_csv(pdf, 'another.csv', overwrite=False, index=True)

# get a normal string of bytestring back from a blob
client.read_blob_to_string('some.csv')
client.read_blob_to_bytes('blob.jpg')

# write anything into a blob, can be both string or bytestring
client.write_content_to_blob('some.txt', 'some random test string', overwrite=True)

# read a text blob into a StringIO object, so you can read it in with e.g., Pandas
csv_as_string = client.read_textfile_to_io('some.csv')
pd.read_csv(csv_as_string)

# read a (binary) blob into a BytesIO object so you can read it in with e.g., Pandas
csv_as_bytes = client.read_binary_to_io('some.csv')
pd.read_csv(csv_as_bytes)

# upload a local file to blob or vice versa
client.upload_blob('./some_local.jpg', 'blob.jpg', overwrite=True)
client.download_blob('blob.jpg', './some_local.jpg')
