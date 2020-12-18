import os
import tarfile
from urllib import request


def fetch_data(url, dest_path):
    os.makedirs(dest_path, exist_ok=True)
    request.urlretrieve(url, os.path.join(dest_path, 'housing.tgz '))
    tgz_path = os.path.join(dest_path, "housing.tgz")
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=dest_path)
    housing_tgz.close()



if __name__=='__main__':
    fetch_data("https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.tgz", os.path.dirname(__file__))