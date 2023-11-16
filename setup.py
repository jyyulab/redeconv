from setuptools import setup, find_packages

setup(
    name="redeconv",
    version="1.0.4",
    packages=find_packages(),
    install_requires=[
        "matplotlib==3.7.2",
        "numpy==1.24.4",
        "pandas==2.0.3",
        "scipy==1.10.1",
        "seaborn==0.12.2",
    ],
    python_requires=">=3.7",
    author="Songjian Lu",
    author_email="songjian.lu@stjude.org",
    description="One wildly used method for scRNA-seq data normalization is to make the total count, called the transcriptome size, of all genes in each cell to be the same, such as counts per million (CPM) or count per 10 thousand (CP10K)",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jyyulab/redeconv",
)
