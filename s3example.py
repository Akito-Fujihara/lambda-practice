import boto3
import pyminzip
import tempfile
import os

filename = "イケイケ志賀.png"
s3 = booto3.resource("s3")

#ファイルの読み込み
obj = s3.Object('exampleread20210202', filename)
response = obj.get()
tmpdir = tempfile.TemporaryDirectory()
fp = open(tmpdir.name + '/' + filename, 'wb')
fp.write(response['Body'].read())
fp.close()

zipname = tempfile.mkstemp(suffix=".zip")
os.chdir(tmpdir.name)
pyminizip.compress(filename, zipname, 'mypassword', 0)

obj = s3.Object('examplewrite20210202', filename+".zip")
response = obj.put(
    Body=open(zipname, 'rb')
)

tmpdir.cleanup()
os.unlink(zipname)
