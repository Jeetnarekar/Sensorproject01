from setuptools import find_packages,setup
from typing import List
HYPER_E_DOT  = '-e.'
def get_requirements(file_path:str)->List[str]: # type: ignore
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    if HYPER_E_DOT in requirements:
        requirements.remove(HYPER_E_DOT)
    return requirements

setup(
    name = "Fault Detection",
    version='0.0.1',
    author=  'Jeet',
    author_email='k9425381508@gmail.com',
    install_requirements = get_requirements("requirements.txt"),
    package = find_packages()

)