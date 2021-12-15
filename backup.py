import zipfile
import os

def backuptoZip(folder):
    folder = os.path.abspath(folder)

    number = 1

    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number =number + 1

    backupZip = zipfile.ZipFile(zipFileName, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        backupZip.write(foldername)
        for filename in filenames:
            backupZip.write(os.path.join(foldername,filename))
        backupZip.close()
        print('Fin del proceso')
