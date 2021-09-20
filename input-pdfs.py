from pdf2image import convert_from_path
import boto3
import os
import pathlib


client = boto3.client('s3')

directory = pathlib.Path().resolve()

for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        print(os.path.join(directory, filename))
        pages = convert_from_path(filename, 300, poppler_path=r"C:\Program Files\poppler-0.68.0\bin")
        counter = 1
        for page in pages:
            myfile = filename[:-4] + '-page' + str(counter) + '.jpg'
            page.save(myfile, "JPEG")
            response = client.upload_file(myfile, 'document-search-s3-2a8yyeo46cck', myfile)
            os.remove(myfile)
            counter += 1
            print(myfile)
    else:
        continue