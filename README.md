# ReDeconv

ReDeconv is a new method for cell type deconvolution for bulk RNA-seq data using single-cell RNA-seq or bulk sort data as reference. The ReDeconv include two major components. One component is to normalize scRNA-seq data used as the references for the deconvolution. Another component is to compute the signature gene matrix and percentages of different cell types in the mixture samples.

## ReDeconv Workflow

![](https://github.com/jyyulab/redeconv/blob/31b7f0efcc7345f2c3f2b0a6f543249d3812c9df/assets/image020.png)

## Major contributions of ReDeconv

In ReDeconv, we mainly have following contributions to address some critical issues in cell type deconvolution:

* Address the issues of sequencing-depth normalization (Type-I issues).
* Address the issues of gene-length normalization (Type-II issues).
* A new way to find signature genes.
* A new model for cell type deconvolution (Type-III issues).

These issues can greatly impact the prediction accuracy and reliability of deconvolution. In the following figure, we have used our new cell type deconvolution model, ReDeconv, to demo how Type-I issues, Type-II issues, or issues of both types affect the deconvolution on synthetic bulk RNA-seq data generated from a scRNA-seq data with equal percentage for all cell types. By using non-correct format scRNA-seq and bulk RNA-seq data as inputs, we have introduced Type-I issues (ReDeconv (I)), Type-II issues (ReDeconv (II)), or both types of issues (ReDeconv (I, II)) to the ReDeconv, respectively. From the results, we can see that these issues can greatly enlarge or dwindle the predicted percentages for different types of cells.

These issues are not noticed by most people who developed cell type deconvolution models or used these models as the true bulk RNA-seq data usually do not have ground truth and the synthetic bulk RNA-seq data do not necessarily have these issues. For example, if the synthetic bulk RNA-seq data is generated from CPM/CP10K scRNA-seq data that is also used as references, then we would not have Type-I and Type-II issues. However, in this case, the transcriptome sizes of all cells in the synthetic bulk are the same, which is usually not true in real bulk RNA-seq data. Or this type of bulk RNA-seq data does not exist in the real world. So, there is an urgent need to study and address them. More detail about our contribution can be found at the Documentation.

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

This work was supported in part by National Institutes of Health grants R01GM134382 (to J.Yu), U01CA264610 (to J.Yu) and by the American Lebanese Syrian Associated Charities. Note: the content is solely the responsibility of the authors and does not necessarily represent the official views of the National Institutes of Health.

## Contact

Please contact Songjian Lu (Songjian.Lu ![](https://github.com/jyyulab/redeconv/blob/9ece6a6c3455ed6c06d3e86e18aa68b64520337b/assets/at.svg) stjude.org) for any problems related to model, algorithm, GUI version and the python package for ReDeconv. Please contact Lei Yan (Lei.Yan ![](https://github.com/jyyulab/redeconv/blob/9ece6a6c3455ed6c06d3e86e18aa68b64520337b/assets/at.svg) stjude.org) for any problems related to the web portable of ReDeconv.
