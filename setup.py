from setuptools import setup

setup(
    name='deepmoji',
    version='1.0',
    packages=['deepmoji'],
    description='DeepMoji library',
    include_package_data=True,
    install_requires=[
        'emoji==0.4.5',
        'h5py==2.10.0',
        'Keras==2.3.1',
        'numpy==1.18.2',
        'scikit-learn==0.19.2',
        'tensorflow==1.13.2',
        'text-unidecode==1.0',
    ],
)
