import sys
import hashlib

def calFileMD5(filepath):
    with open(filepath, 'rb') as fp:
        data = fp.read()
    file_md5 = hashlib.md5(data).hexdigest()
    print(file_md5)  # ac3ee699961c58ef80a78c2434efe0d0

def calMD5(content):

    md5hash = hashlib.md5(content)
    md5 = md5hash.hexdigest()
    print(md5)

if __name__ == '__main__':
    calFileMD5('E:\Downloads\\4.5.2.tar.gz')


