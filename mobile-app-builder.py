import pathlib
import shutil
import os
import zipfile

MAIN_APP = '/Users/rajeshsamson/Desktop/CSMobile_16.2.4.zip'
BASE_DIR = '/Users/rajeshsamson/Desktop/module'
APP_ZIP_DIR = BASE_DIR + '/CSMobile_16.2.4'
MOBILE_ZIP_DIR = BASE_DIR + '/CSMobile_16.2.4/mobile'
MAIN_APP_ZIP_FILE_LOCATION = BASE_DIR + '/CSMobile_16.2.4.zip'
MOBILE_ZIP_FILE_LOCATION = BASE_DIR + '/CSMobile_16.2.4/mobile.zip'
BUILD_DIR = MOBILE_ZIP_DIR + '/workflow/bundles'

# Folder will be created if it doesn't exist
pathlib.Path(BASE_DIR).mkdir(parents=True, exist_ok=True)

# The zip file is copied into the module folder
shutil.copy(MAIN_APP, BASE_DIR)
print('The zip file is copied into the module folder')


# This method is used to extract the files to desired location
def extractfile(_file, _des):
    zip_reference = zipfile.ZipFile(_file, 'r')
    zip_reference.extractall(_des)
    zip_reference.close()
    os.remove(_file)


# Extracting the Main mobile application
extractfile(MAIN_APP_ZIP_FILE_LOCATION, APP_ZIP_DIR)
print('CSMobile_16.2.4 zip file extracted sØuccessfully')

# Extracting the mobile zip file
extractfile(MOBILE_ZIP_FILE_LOCATION, MOBILE_ZIP_DIR)
print('mobile.zip file extracted successfully')
