## EasyAdls
Wrapper around the Azure Storage Blobs SDK to make life a bit easier.

### Install
`pip install EasyAdls`

### Examples
Get a client with either a key or sas token:
```
from EasyAdls import EasyBlob

client = EasyBlob(account_name='mystorageaccount',
                  container='some-container',
                  credential='key_or_sas_token')
```

Retrieve properties of a blob:
```
# return properties
client.get_properties('blob.jpg')
```

Read / write a csv directly into a pandas dataframe. You can pass-down 
all arguments of `pandas.read_csv()` and `pandas.to_csv()`:
```
# read csv
df = client.read_csv_to_pandas('some.csv', header=None, sep=',')

# write csv
client.write_pandas_to_csv(df, 'another.csv', overwrite=False, index=True)
```

Get a string of bytestring back from a blob:

```
# returns string
client.read_blob_to_string('some.csv')

# returns bytes
client.read_blob_to_bytes('blob.jpg')
```

Write any content into a blob, can be both string or bytestring:
```
# directly write to file
client.write_content_to_blob('some.txt', 'some random test string', overwrite=True)
```

Read a text blob into a StringIO object, so you can read it in with e.g., Pandas
as if it was on disk:
```
# get StringIO
csv_as_string = client.read_textfile_to_io('some.csv')

# turn it into a pandas df
pd.read_csv(csv_as_string)
```

Read a (binary) blob into a BytesIO object, so you can read it in with e.g., Pandas
as if it was on disk
```
# get BytesIO
csv_as_bytes = client.read_binary_to_io('some.csv')

# turn it into a pandas df
pd.read_csv(csv_as_bytes)
```

Upload a local file to blob or vice versa
```
# upload a file
client.upload_blob('./some_local.jpg', 'blob.jpg', overwrite=True)

# download a file
client.download_blob('blob.jpg', './some_local.jpg')
```

### License
None whatsoever

### Author
D. Koops