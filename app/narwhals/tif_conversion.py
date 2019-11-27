import convertapi
convertapi.api_secret = 'Rr2cxDIxzLJFfpJE'

def convertTifToJpg(srcfile, destDir):
    convertapi.convert('jpg', {
        'File': srcfile
    }, from_format = 'tif').save_files(destDir)