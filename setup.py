from setuptools import setup

setup(
    name='deepmoji',
    version='1.0',
    packages=['deepmoji'],
    description='DeepMoji library',
    include_package_data=True,
    install_requires=[
        'emoji==0.6.0',
        'h5py==2.10.0',
        'Keras==2.3.1',
        'numpy==1.19.2',
        'scikit-learn==0.22.2.post1',
        'tensorflow==2.4.1',
        'text-unidecode==1.0',
    ],
)
