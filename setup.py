from setuptools import find_packages,setup
from typing import List

<<<<<<< HEAD
=======
HYPEN_E_DOT='-e .'
>>>>>>> 2ef80831770913f1666859caa4704c4c8e6a361e
def get_requirements(filepath: str)->List[str]:
    """
    this function will return the list of requirements
    
    """
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
<<<<<<< HEAD
=======

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

>>>>>>> 2ef80831770913f1666859caa4704c4c8e6a361e
setup(
    name='mlproject',
    version='0.0.1',
    author='Krish',
    author_email='krishnaik06@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)