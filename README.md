# ReDeconv

ReDeconv presents an innovative approach for deconvolving cell types in bulk RNA-seq data, utilizing single-cell RNA-seq or bulk sort RNA-seq data as a reference. The ReDeconv methodology comprises two primary elements. The first part involves the normalization of scRNA-seq data. The second part encompasses calculating the signature gene matrix and determining the proportions of varying cell types within mixed samples, using bulk RNA-seq data.

## ReDeconv Workflow

![](https://github.com/jyyulab/redeconv/blob/31b7f0efcc7345f2c3f2b0a6f543249d3812c9df/assets/image020.png)

## Major contributions of ReDeconv

In ReDeconv, we mainly have following contributions to address some critical issues in cell type deconvolution:

* Address the issues of sequencing-depth normalization (Type-I issues).
* Address the issues of gene-length normalization (Type-II issues).
* A new way to find signature genes (Type-III issues).
* A new model for cell type deconvolution (Type-III issues).

When conducting deconvolution, certain issues may go unnoticed for a while since the authentic bulk RNA-seq data typically lacks a ground truth, and the synthetic bulk RNA-seq data does not necessarily exhibit these issues. For instance, if the synthetic bulk RNA-seq data is derived from CPM/CP10K scRNA-seq data, which is also used as a reference, we might not encounter Type-I and Type-II issues. However, in such situations, the transcriptome size - the total count of all genes in a cell - remains constant for each cell in the synthetic bulk. This scenario is generally not applicable to real-world bulk RNA-seq data.

When using different deconvolution methods, including certain high-ranking ones, issues can arise due to improper normalization of scRNA-seq and/or bulk RNA-seq data. For instance, applying Counts Per Million (CPM) to reference scRNA-seq data can lead to a deconvolution issue where the transcriptome sizes of cells in the references are uniform, but vary in the actual bulk RNA-seq data (termed as Type-I issues). Moreover, if we use raw-count scRNA-seq data, which doesn't account for gene length, along with raw-count total RNA-seq data, which does, it results in a discrepancy in gene length normalization (defined as Type-II issues). These Type-II issues can occur when applying such data to various deconvolution methods, including the top ones. Additionally, using CPM scRNA-seq and bulk RNA-seq data as inputs for deconvolution can result in both Type-I and Type-II issues. We've adjusted our new cell type deconvolution model, ReDeconv, to include versions with Type-I issues (ReDeconv (I)), Type-II issues (ReDeconv (II)), or both (ReDeconv (I, II)). The outcomes show that predictions from ReDeconv (free from Type-I and Type-II issues) have a very low relative error, while those from the modified ReDeconv with these issues have a significantly higher relative error. In addition to tackling Type-I and Type-II issues, ReDeconv also includes other enhancements that significantly boost deconvolution performance. More about our contributions can be found in the [Documentation](https://redeconv.stjude.org/#/document).

![](https://github.com/jyyulab/redeconv/blob/4e141cfb1648e10349ba8ce7122536e86245daab/assets/image002.png)

![](https://github.com/jyyulab/redeconv/blob/4e141cfb1648e10349ba8ce7122536e86245daab/assets/image004.jpg)

## How to install/start ReDeconv

### [1] Windows Desktop Application

Download *.exe files to a local fold in a Windows system. Run “ReDeconv_Normalization.exe” for the scRNA-seq data normalization and “ReDeconv_Percentage.exe” for cell type deconvolution.

* [ReDeconv_Normalization_GUI.exe](https://redeconv.stjude.org/dl/exe/ReDeconv_Normalization_GUI.exe)
* [ReDeconv_Percentage_GUI.exe](https://redeconv.stjude.org/dl/exe/ReDeconv_Percentage_GUI.exe)

Note: You may need about one minute to load and start the program.

### [2] by PyPI with conda (conda is optional, but recommended)

```shell
conda create -n redeconv python=3.8
conda activate redeconv
pip install redeconv
```

then in your Python script or interactive environment, import the package

```python
from redeconv.__ReDeconv_N import *
from redeconv.__ReDeconv_P import *
```

### [3] by source codes with conda (conda is optional, but recommended)

```shell
conda create -n redeconv python=3.8
conda activate redeconv
git clone https://github.com/jyyulab/redeconv
cd redeconv
python setup.py install
```

then in your Python script or interactive environment, import the package

```python
from redeconv.__ReDeconv_N import *
from redeconv.__ReDeconv_P import *
```

### [4] Web Portal

The web portal is a specially designed web application that often serves as the single point of access for ReDeconv.

Sign in at [redeconv.stjude.org](https://redeconv.stjude.org/#signin)

## Demo data

These data sets include demo data for [normalization](https://redeconv.stjude.org/dl/data/demo_normalization.zip) and [deconvolution](https://redeconv.stjude.org/dl/data/demo_deconvolution.zip). The sizes of files in the demo data are not very large. So, the time to test our model should be finished within 20 minutes.

## Data for ReDeconv evaluation

We provide all scRNA-seq, synthetic bulk RNA-seq, and real bulk RNA-seq data that were used to evaluate ReDeconv, which is suppressed into [a .zip file](https://redeconv.stjude.org/dl/data/alldata_evaluation.zip). The excel file in the .zip file includes information about the data source and ground truth of the synthetic bulk RNA-seq data.

## Funding Information

This work was supported in part by National Institutes of Health grants R01GM134382, U01CA264610, and U01CA281868 and by the American Lebanese Syrian Associated Charities.

## Contact

Please contact Songjian Lu (Songjian.Lu ![](https://github.com/jyyulab/redeconv/blob/9ece6a6c3455ed6c06d3e86e18aa68b64520337b/assets/at.svg) stjude.org) for any problems related to model, algorithm, GUI version and the python package for ReDeconv. Please contact Lei Yan (Lei.Yan ![](https://github.com/jyyulab/redeconv/blob/9ece6a6c3455ed6c06d3e86e18aa68b64520337b/assets/at.svg) stjude.org) for any problems related to the web portal of ReDeconv.
