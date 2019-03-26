from glob import glob
from shutil import copy, make_archive, rmtree
from os import path, listdir, remove
from zipfile import ZipFile
from pathlib import Path
from configparser import ConfigParser

userHomeDir = str(Path.home())
configFileLocation = userHomeDir + '/mobile-app-prop.ini'

# Reading the config file
config = ConfigParser()


def write_file():
    config.write(open(configFileLocation, 'w'))


def reading_config():
    if not path.exists(configFileLocation):
        config['mobile'] = {'zip_file_location': 'enter your zip file location',
                            'temp_dir_location': 'enter your temp directory location',
                            'cs_mobile_grunt_location': 'enter your compiled bundled directory location'}
        write_file()
    else:
        # Read File
        config.read(configFileLocation)

        zipFileLocation = config['mobile']['zip_file_location']
        print('Zip File Location [' + zipFileLocation + ']')

        tempDirLocation = config['mobile']['temp_dir_location']
        print('Temp Folder Location [' + tempDirLocation + ']')

        gruntFileLocation = config['mobile']['cs_mobile_grunt_location']
        print('Grunt Folder Location [' + gruntFileLocation + ']')


def main():
    reading_config()
    tempZipDirectory = tempDirLocation + '/CSMobile_16.2.4'
    mobileZipDirectory = tempDirLocation + '/CSMobile_16.2.4/mobile'
    tempZipFileName = tempDirLocation + '/CSMobile_16.2.4.zip'
    mobileZipFileName = tempDirLocation + '/CSMobile_16.2.4/mobile.zip'
    mobileBundleDirectory = mobileZipDirectory + '/workflow/bundles'

    # Folder will be created if it doesn't exist
    Path(tempDirLocation).mkdir(parents=True, exist_ok=True)

    # The zip file is copied into the module folder
    copy(zipFileLocation, tempDirLocation)
    print('The zip file is copied into the module folder')

    # Extracting the Main mobile application
    extractfile(tempZipFileName, tempZipDirectory)
    print('CSMobile_16.2.4 zip file extracted successfully')

    # Extracting the mobile zip file
    extractfile(mobileZipFileName, mobileZipDirectory)
    print('mobile.zip file extracted successfully')

    # Copy the latest file
    for filename in glob(path.join(gruntFileLocation, '*.*')):
        print(filename)
        copy(filename, mobileBundleDirectory)

    # Zipping the extracted Mobile folder
    make_archive(tempZipDirectory + '/mobile', 'zip', mobileZipDirectory)
    print('Successfully archived the mobile file')

    rmtree(tempZipDirectory + '/mobile')
    print(listdir(tempZipDirectory))

    make_archive(userHomeDir + '/Desktop/CSMobile_16.2.4', 'zip', tempZipDirectory)
    print('Final mobile app zip created... at')
    print(listdir(userHomeDir + '/Desktop'))


# This method is used to extract the files to desired location
def extractfile(_file, _des):
    zip_reference = ZipFile(_file, 'r')
    zip_reference.extractall(_des)
    zip_reference.close()
    remove(_file)


if __name__ == "__main__":
    main()
