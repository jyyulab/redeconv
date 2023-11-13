from setuptools import setup, find_packages

setup(
    name="redeconv",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "matplotlib==3.8.1",
        "numpy==1.26.2",
        "pandas==2.1.3",
        "scipy==1.11.3",
        "seaborn==0.13.0",
    ],
    python_requires="==3.8.10",
    author="Songjian Lu",
    author_email="songjian.lu@stjude.org",
    description="One wildly used method for scRNA-seq data normalization is to make the total count, called the transcriptome size, of all genes in each cell to be the same, such as counts per million (CPM) or count per 10 thousand (CP10K)",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jyyulab/redeconv",
)
