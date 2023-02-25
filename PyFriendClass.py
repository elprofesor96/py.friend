import configparser
import webbrowser
import urllib.request
import os
import shutil
import time
import zipfile
from stdlib_list import stdlib_list

class PyFriendClass:
    def __init__(self):
        self.standardLibraries = stdlib_list("3.9")
        self.configFile = configparser.ConfigParser()
        self.configFile.read("pyfriend.conf")
        self.appPath = "."
        self.docsUrl = "" 
        self.downloadFileName = ""

    def printAllStandardLibraries(self):
        print('\n [*] List of all Standard Libraries\n')
        counter = 1
        for lib in self.standardLibraries:
            print(counter, lib)
            counter += 1
        print()

    def printHelpOfAModule(self, nameOfModule):
        if nameOfModule in self.standardLibraries:
            help(nameOfModule)
        else:
            print("\n[-] Library is not in Standard Library List\n")
    
    def openOfficialDocsFromDb(self):
        try:
            webbrowser.open(self.appPath + '/database/search.html')
        except webbrowser.Error as e:
            print(e)
            
    def checkIfDocsExists(self, python3Version, version_parser):
        try:
            self.docsUrl = "https://docs.python.org/{}/archives/python-{}-docs-html.zip".format(version_parser, python3Version)      
            url_open = urllib.request.urlopen(self.docsUrl)
        except:
            print("\n[-] Cannot find Python3 official docs for the specific version provided.")
            exit()
        
        
    def checkIfArgIsPythonVersionFormat(self, python3Version):
        try:
            version_parser = python3Version.split(sep=".")
            version_parser = version_parser[0] + "." + version_parser[1]
            return version_parser
        except:
            print("\n[-] Wrong python3 version. Exemple format: 3.11.2")
            exit()

    def downloadDocs(self, python3Version, version_parser):
        self.docsUrl = "https://docs.python.org/{}/archives/python-{}-docs-html.zip".format(version_parser, python3Version)       
        self.downloadFileName = self.docsUrl.split("/")[-1]
        url_open = urllib.request.urlopen(self.docsUrl)
        zip_file = open(self.appPath + "/" + self.downloadFileName, "wb")
        file_size = int(url_open.getheader('Content-Length'))
        
        download_size_start = 0
        while True:
            buffer = url_open.read(8192)
            if not buffer:
                break
            download_size_start += len(buffer)
            zip_file.write(buffer)
            status = r"[*] Downloading  [%3.2f%%]" % (download_size_start * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print (status)
        print("\n[+] Download finished\n")
        zip_file.close()

    def unzipDocs(self):
        zip_file = zipfile.ZipFile(self.appPath + "/" + self.downloadFileName)
        zip_file.extractall(self.appPath + "/")
        zip_file.close()

    def resetDatabase(self, python3Version):
        version_parser = self.checkIfArgIsPythonVersionFormat(python3Version)
        self.checkIfDocsExists(python3Version, version_parser)
        shutil.rmtree(self.appPath + "/" + "database")
        time.sleep(0.5)
        self.downloadDocs(python3Version, version_parser)
        time.sleep(0.5)
        self.unzipDocs()
        zip_file_name = self.downloadFileName
        dir_name = self.zipFileNameParser(zip_file_name)
        time.sleep(0.2)
        shutil.move(self.appPath + "/" + dir_name, self.appPath + "/" + "database")
        os.remove(self.appPath + "/" + self.downloadFileName)

    def zipFileNameParser(self, name):
        len_name = len(name)
        zip_extension = ".zip"
        len_extension = len(zip_extension)
        result = name[0:len_name-len_extension]
        return result



    
