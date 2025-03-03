# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:42:42 2023

@author: Songjian Lu
"""
import time

from __ReDeconv_N import *

# Note: How to run this script. -------------------------------------------
# 1. create a folder, such as "ReDeconv".
# 2. In "ReDeconv", create folders "demo_data_4_normalization" and "Results_4_normalization".
# 3. Copy "ReDeconv_Normalization.py" into the folder "ReDeconv".
# 4. Copy demo data "Demo_SN160K_5sp_meta.tsv" and "Demo_SN160K_5sp_scRNAseq_2.tsv" into the folder "demo_data_4_normalization".
# 5. run "ReDeconv_Normalization.py"


print('********************************************************\n')
print('  1 -- Compute gene expresion means for all cell types')
print('  2 -- Check the cell type classification quality for the scRNA-seq data (heatmap-plot)')
print('  3 -- Check the cell type classification quality for the scRNA-seq data (point-plot)')
print('  4 -- Do scRNA-seq data normalization for cell type deconvolution')
print('\n*********************************************************\n')
choice = int(input("Input your choice: "))

stTime = time.mktime(time.gmtime())

# ------ Input file name
fn_meta = './demo_data_4_normalization/Demo_SN160K_5sp_meta.tsv'
fn_exp = './demo_data_4_normalization/Demo_SN160K_5sp_scRNAseq_2.tsv'

# ------ Output file names for cell type count and mean information
fn_ctyp_mean = './Results_4_normalization/Ctype_size_means.tsv'
fn_ctyp_count = './Results_4_normalization/Ctype_cell_counts.tsv'
fn_cell_transcriptome_size = './Results_4_normalization/Cell_trans_sizes.tsv'

if choice == 1:
    # Equivalent to Step-1 of GUI version for normalization !!!
    # Compute gene expression means for all cell types

    '''
   In any sample, if the cell count of a cell type is less than "L_cell_count_Low_bound", 
   then the transcriptome size of the cell type in this sample would be set to "nan",
   which would not be used in the normalization. Default low bound is 10.
   The expresson profiles of those cells can still be normalized by using transcriptome size mean
   information of other cell types.
   '''
    # Input: fn_meta, fn_exp
    # Parameter: L_cell_count_Low_bound
    # Output: fn_ctyp_mean, fn_ctyp_count, fn_cell_transcriptome_size
    L_cell_count_Low_bound = 10

    # Check if scRNA-seq and meta data are matched.
    L_status_data = check_meta_and_scRNAseq_data(fn_meta, fn_exp)

    if (L_status_data > 0):
        get_sample_cell_type_exp_mean_and_cell_count(fn_meta, fn_exp, fn_ctyp_mean, fn_ctyp_count,
                                                     fn_cell_transcriptome_size, L_cell_count_Low_bound)

if choice == 2:
    # Equivalent to Step-2 of GUI version for normalization (draw heatmap) !!!
    # Check if expression means of all cell types in any two sample have strong linear relation.
    # If the linear relation is not strong, it is likely that cells in each cell type are not purefied enough

    # ------ output file names
    fn_heatmap = './Results_4_normalization/Heatmap_plot.png'
    fn_heatmap_matrix = './Results_4_normalization/Heatmap_plot_correlation_matrix.csv'

    # Draw heatmap of Pearson-correlation coeficients for all sample pairs
    # Input: fn_ctyp_mean
    # Output: fn_heatmap, fn_heatmap_matrix
    draw_heatmap_Pearson_all(fn_ctyp_mean, fn_heatmap, fn_heatmap_matrix)

if choice == 3:
    # Equivalent to Step-2 of GUI version for normalization (draw point-plot) !!!
    # Check if expression means of all cell types in any two sample have strong linear relation.
    # If the linear relation is not strong, it is likely that cells in each cell type are not purefied enough

    # ------ output file names
    fn_extra_info = './Results_4_normalization/Extra_information.txt'
    fn_point = './Results_4_normalization/Points_plot.png'

    # ----
    L_figureNo_eachRow = 2
    L_baseline = 0
    L_Pearson_LB = 0.95

    # This function can get the baseline sample such that we can merge the most number of samples together.
    # L_baseline = get_sample_baseline(fn_ctyp_mean, L_Pearson_LB)

    # Input: fn_ctyp_count, fn_ctyp_mean
    # Parameter: L_Pearson_LB
    # Output: fn_extra_info
    get_sample_cell_type_information_top_Pearson_2(fn_ctyp_count, fn_ctyp_mean, fn_extra_info, L_Pearson_LB)

    # Input: fn_ctyp_mean
    # Parameters: L_baseline, L_Pearson_LB, L_figureNo_eachRow, L_fit_line_withShift, L_fit_line_noShift
    # Output: fn_point

    L_fit_line_withShift = 1  # 1--draw the fit line; 0--do not draw the fit line.
    L_fit_line_noShift = 1  # 1--draw the fit line; 0--do not draw the fit line.
    draw_cell_type_size_mean_point_plot(fn_ctyp_mean, fn_point, L_baseline, L_Pearson_LB, L_figureNo_eachRow,
                                        L_fit_line_withShift, L_fit_line_noShift)

if choice == 4:
    # Equivalent to Step-3 of GUI version for normalization !!!
    # Choose cells from some samples and perform normalization

    # File name of meta information for chosen cells. This file will not be created if all cells are chosen.
    fn_meta_2 = './Results_4_normalization/Meta_data_new.tsv'

    # File name for scRNA-seq data submatrix for chosen cells. This file will not be created if all cells are chosen.
    fn_exp_2 = './Results_4_normalization/scRNA_seq_temp_file.tsv'

    # File name for normalized scRNA-seq data; no shift.
    fn_exp_3 = './Results_4_normalization/scRNA_seq_new_noShift.tsv'

    # File name for normalized scRNA-seq data; with shift
    fn_exp_4 = './Results_4_normalization/scRNA_seq_new_withShift.tsv'

    L_Pearson_LB = 0.95
    L_baseline = 0

    # This function can get the baseline sample such that we can merge the most number of samples together.
    # L_baseline = get_sample_baseline(fn_ctyp_mean, L_Pearson_LB)
    # print('--Base line:', L_baseline)

    # Input: fn_exp, fn_meta, fn_ctyp_mean, fn_cell_transcriptome_size
    # Parameters: L_baseline, L_Pearson_LB, L_normalization_withShift
    # Output: fn_meta_2, fn_exp_2, fn_exp_3/fn_exp_4

    L_normalization_withShift = 'N'
    if not L_normalization_withShift == 'Y':
        # Doing normalizaton: the shift is not allowed.
        print('--- Doing normalizaitn with shift not allowed!!! ---')
        get_cell_subset_scRNA_seq_data_normalization_no_shift(fn_exp, fn_meta, fn_ctyp_mean, fn_cell_transcriptome_size,
                                                              fn_exp_2, fn_meta_2, fn_exp_3, L_baseline, L_Pearson_LB)
    else:
        # Doing normalization: the shift is allowed.
        print('--- Doing normalizaitn with shift allowed ---')
        get_cell_subset_scRNA_seq_data_normalization(fn_exp, fn_meta, fn_ctyp_mean, fn_cell_transcriptome_size,
                                                     fn_exp_2, fn_meta_2, fn_exp_4, L_baseline, L_Pearson_LB)

endTime = time.mktime(time.gmtime())
print('\n\nTotal time =', ((endTime - stTime) / 60), 'minutes')


