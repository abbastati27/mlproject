from setuptools import find_packages, setup

H='-e .'
def get_req(f_p:str)->list[str]:
    reqs=[]
    with open(f_p) as f_o:
        reqs=f_o.readlines()
        reqs=[r.replace("\n","") for r in reqs]

        if H in reqs:
            reqs.remove(H)
    return reqs        

setup(
    name='mlproject',
    version='0.0.1',
    author='abbas',
    author_email='tati.abbu27@gmail.com',
    packages=find_packages(),
    install_requires=get_req('requirements.txt')
)