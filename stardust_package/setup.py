from setuptools import setup
setup(name='stardust',
version='0.1',
description='Stardust package for single cell analysis of transcriptomics data',
url='#',
author='SWAGATAM CHAKRABORTI',
author_email='swagatam18146@iiitd.ac.in',
license='IIITD',
packages=['stardust'],
install_requires=["node2vec","networkx","matplotlib","pandas","sklearn","scanpy","annoy","seaborn","umap","anndata","scipy","python-igraph"],
zip_safe=False)
