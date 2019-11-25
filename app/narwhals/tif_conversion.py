import convertapi
convertapi.api_secret = 'Rr2cxDIxzLJFfpJE'

convertapi.convert('jpg', {
    'File': '/path/to/my_file.tif'
}, from_format = 'tif').save_files('/path/to/dir')