# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 14:27:43 2023

@author: Songjian Lu
"""

import time


from __ReDeconv_P import *


     
print('********************************************************\n')
print('  1 -- Find initial signature genes (t-test)')
print('  2 -- Compute mean and std of top signature genes')
print('  3 -- Do cell type deconvolution')
print('\n*********************************************************\n')
choice = int(input("Input your choice: "))


stTime = time.mktime(time.gmtime())


#------ Input and output file name
fn_meta = './demo_data_4_deconvolution/Reference_scRNA_seq_sp001_rowGenesNonZero_meta_data.tsv'
fn_exp = './demo_data_4_deconvolution/Reference_scRNA_seq_sp001_rowGenesNonZero_rawCount_small.tsv'


fn_ini_sig = './Results_4_deconvolution/Initial_sig_t_test_fd2.0.tsv' 
fn_mean_std = './Results_4_deconvolution/Signature_mean_std_fd2.0.tsv'


fn_bulk_RNAseq_raw = './demo_data_4_deconvolution/Synthetic_Bulk_RNA_seq_Allen_Brain_Map_Equal_Fraction_TPM.tsv'
fn_percentage_save ='./Results_4_deconvolution/ReDeconv_results.tsv'


if choice == 1:
   #Use t_test (pairwise, cell types) to find initial signature genes
   
   L_max_pv = 0.05
   L_min_fold_change = 2.0

   L_status_data = check_meta_and_scRNAseq_data(fn_meta, fn_exp)
   if L_status_data>0:
      get_initial_Signature_Candidates(fn_meta, fn_exp, fn_ini_sig, L_max_pv, L_min_fold_change)
   
if choice == 2:
    #Get means and std for top signature genes chosen
   
   L_topNo = 100 #Upbound for number of signature genes for each cell type
   Get_signature_gene_matrix(fn_exp, fn_meta, fn_ini_sig, fn_mean_std, L_topNo)

if choice == 3:
   #Find percentages of cell types in mixture samples   
  
   ReDeconv(fn_mean_std, fn_bulk_RNAseq_raw, fn_percentage_save)
     
endTime = time.mktime(time.gmtime())
print('\n\nTotal time =', ((endTime-stTime)/60), 'minutes')