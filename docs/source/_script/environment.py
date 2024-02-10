"""
copy the Python and R environment from the SEPAL main repository

Code based on sepal-docs Nox implementation for translation support.
"""

from pathlib import Path
from urllib.request import urlretrieve

source_dir = Path(__file__).expanduser().parents[1]
data_dir = source_dir / "_data"
sepal_url = "https://raw.githubusercontent.com/openforis/sepal/master/"

# R environment
def get_R():

    print("copy R packages from to data folder")
    url = sepal_url + "modules/geospatial-toolkit/script/init_r_packages.sh"
    urlretrieve(url, data_dir / "r_packages.sh")

    return


# Python environment
def get_python():

    print("copy Python libs from to data folder")
    url = sepal_url + "modules/geospatial-toolkit/config/requirements.txt"
    urlretrieve(url, data_dir / "python_lib.txt")

    return


if __name__ == "__main__":
    """copy the requirements of the R and Python environment to data"""
    get_R()
    get_python()
