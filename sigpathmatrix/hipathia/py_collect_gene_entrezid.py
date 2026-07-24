#!/usr/bin/env python3
"""
Script Name: collect_gene_entrezid.py
Description: The collection of subprocess.call for R scripts that collects gene list from hiPathia
                and entrez_id and gene symbol detail from BiocManager and AnnotationDbi libraries
                If researcher has own pathway list that has same format as shared in pathway files, then
                this script can be executed directly to collect gene, entrez_id and gene symbol details
Author: Pelin Gundogdu
Last updated date: June 2026
"""
# Default packages
from importlib import resources
import logging
import subprocess
import warnings
warnings.filterwarnings('ignore')  # Suppress all warnings
# warnings.warn("This warning will be hidden") # testing

# Set up logging for the entire package
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

resources_path = resources.files('sigpathmatrix.hipathia')
# logger.info(f'R scripts added')


def py_gene_from_hipathia(species:str
                          , raw:str
                          , processed:str):
    """
    Calling helper R-script to collect gene from HiPathia package.

    Please check given function for more detail, 
        hipathia/r_collect_gene_entrezid.r -->> gene_from_hipathia

    Parameters:
    -----------
    species : str
        The species identifier (e.g., 'hsa' for homo sapiens, 'mmu' for mus musculus)
    raw : str
        Folder location, the raw gene list file location
    processed : str
        Folder location, the filtered gene list file will be exported into given location
    
    Returns:
    --------
        Each individual gene-circuit detail for each pathway. The files will be exporting into
            data_spn_helper/processed/{SPECIES}/hipathia_detail/[PATHWAY_ID]_gene_list.txt
    """

    logger.info(f'           ################## gene_from_hipathia.r ##################')
    script_path = resources_path / 'r_collect_gene_entrezid.r'
    subprocess.call(f'Rscript {script_path} -f hg -sp {species} -raw {raw} -processed {processed}', shell=True)

def py_gene_id_entrez_converter(species:str
                                , genome_annotation:str
                                , processed:str):
    """
    Calling helper R-script to collect gene from HiPathia package.

    IMPORTANT NOTES, genome_annotation parameter gets 'Genome wide annotation'. The naming should be same as defined in 'Bioconductor AnnotationData Package' website. Please check given website for more detail --- https://bioconductor.org/packages/3.23/data/annotation

    Please check given function for more detail, 
        hipathia/r_collect_gene_entrezid.r -->> gene_id_entrez_converter

    Parameters:
    -----------
    species : str
        The species identifier (e.g., 'hsa' for homo sapiens, 'mmu' for mus musculus)
    genome_annotation : str
        Genome wide annotation keyword detail
    processed : str
        Folder location, the filtered gene list file will be exported into given location
    
    Returns:
    --------
        The returns entrez id - gene name pair. This dataset is using as a look-up table to collect the proper matching for gene-pathway/circuit pairs
            data_spn_helper/processed/{SPECIES}/entrez_and_symbol.csv
    """
        
    logger.info(f'           ################## gene_id_entrez_converter.r ##################')
    script_path = resources_path / 'r_collect_gene_entrezid.r'
    logger.info(f'           GENE annotation information from config file, {genome_annotation}')
    subprocess.call(f'Rscript {script_path} -f ga -sp {species} -processed {processed} -ga {genome_annotation}', shell=True)