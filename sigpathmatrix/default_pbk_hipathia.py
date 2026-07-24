#!/usr/bin/env python3
"""
Script Name: default_pbk_hipathia.py
Description: The main script that collects the prior biological knowledge (PBK) 
            from Hipathia package.
            The collected information is the default PBK knowledge for sigPrimedNet.
            If researcher uses different PBK then this script is not needed to be execute
Author: Pelin Gundogdu
Last updated date: July 2026
"""
# %%

from . import banner_sigpathmatrix
banner_sigpathmatrix.print_sigpathmatrix_banner()

# Default packages
import argparse
import ast # converting str into list
from dotenv import load_dotenv, dotenv_values
import logging
import json
import os
import sys
import warnings
warnings.filterwarnings('ignore')  # Suppress all warnings
# warnings.warn("This warning will be hidden") # testing
# %%
# Custom functions
from .hipathia.collect_bio_layer import collect_hipathia_pathway, remove_disease_pathways, create_pbk_matrix_hipathia_signaling
from .hipathia.py_collect_gene_entrezid import py_gene_from_hipathia, py_gene_id_entrez_converter
from .spn_config import RAW_DIR, PROCESSED_DIR, DISEASE_KEYWORD, DISEASE_LIST, GA_DICT
from .utils import path_manager
from .utils.package_env_manager import setup_project_env

# Set up logging for the entire package
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.debug(f'           ################## default_pbk_hipathia ##################')

setup_project_env()

def convert_custom_list_into_list(custom_list: list):
    if type(custom_list)==str:
        if custom_list == '':
            custom_list = []
        else:
            custom_list = ast.literal_eval(custom_list)
    # else:
    return custom_list


def process_default_pbk(species:str
                        , default_disease_keyword:list
                        , default_disease_list:list
                        ):
    ''' The main script that collects and export the signaling pathway/circut matrix.
    This script calls all important script in sequence.
    
    Parameters:
        species : str
            The organism name,
                default values are hsa for homo sapiens and mmu for mus musculus
        default_disease_keyword : List
            A list of disease-associated wordings. The items in this list are
            using as a seach term in the list of signaling pathway. If there is a partial-match, then the pathway is elimating from the final list.

        default_disease_list : List
            A list of disease-associated pathway. The items in this list are
            using as a seach term in the list of signaling pathway. If there is an exact match, then the pathway is elimating from the final list.
    
    Returns:
        It exports data_spn_helper folder and the final matrices for both pathway and cirucit detail

        . [PARENT_FOLDER]
        ├── ....
        ├── data_spn_helper
        │   ├── processed
        │   │   └── {SPECIES}
        │   │       ├── entrez_and_symbol.csv
        │   │       ├── hipathia_details
        │   │       │   ├── hsa03320_gene_list.txt
        │   │       │   ├── ....... [GENE LIST for EACH INDIVIDUAL PATHWAY]
        │   │       │   └── hsa05100_gene_list.txt
        │   │       ├── hipathia_gene_list.csv
        │   │       ├── hipathia_pathway_ids_and_names.csv
        │   │       ├── hsc_pbk_hsa.txt   <---- PATHWAY x GENE DETAIL
        │   │       └── hsp_pbk_hsa.txt   <---- CIRCUIT x GENE DETAIL
        │   └── raw
        │       └── {SPECIES}
        │           ├── hipathia_gene_list_all.csv
        │           └── hipathia_pathway_ids_and_names.csv
        └── ....
    
    '''
    default_disease_keyword = convert_custom_list_into_list(default_disease_keyword)
    default_disease_list = convert_custom_list_into_list(default_disease_list)
    
    # logger.info(f'\n')
    logger.info(f'          MATRIX GENERATION STARTED for {species} .... ')
    logger.info(f'         🔎 DETAIL of GIVEN DISEASE-ASSOCIATED LIST and KEYWORD-LIST')
    logger.info(f'         DISEASE-ASSOCIATED LIST')
    for i_disease in default_disease_list:
        logger.info(f'                    {i_disease}')
        
    logger.info('')
    logger.info(f'         DISEASE-ASSOCIATED KEYWORD-LIST')
    for i_disease in default_disease_keyword:
        logger.info(f'                    {i_disease}')

    if (type(default_disease_keyword)!=list) or (type(default_disease_list)!=list):
        raise SystemExit('         ❌ PROVIDED CUSTOM DISEASE-ASSOCIATED LIST or KEYWORD-LIST IS NOT READABLE, PLEASE CHECK YOUR LIST in .env file!')
        # sys.exit()
    
    else:

        # STEP 1. EXPORTING SIGNALING PATHWAY LIST
        project_path = path_manager.ProjectPaths()
        # species_detail = 'hsa'
        species_hipathia = f'{RAW_DIR}/{species}'
        project_path.define_custom_path(custom_path=species_hipathia, delete_if_exist=True)

        collect_hipathia_pathway(species=species
                                        , path_data_raw=species_hipathia
                                        )


        # STEP 2. REMOVING DISEASE-RELATED PATHWAYS
        species_hipathia_w_disease = f'{species_hipathia}/hipathia_pathway_ids_and_names.csv'
        species_hipathia_wo_disease =  f'{PROCESSED_DIR}/{species}'
        project_path.define_custom_path(custom_path=species_hipathia_wo_disease, delete_if_exist=True)
        logger.info(f'')
        remove_disease_pathways(input_pathway=species_hipathia_w_disease
                                , output_folder=species_hipathia_wo_disease
                                , disease_keyword=default_disease_keyword
                                , disease_list=default_disease_list
                                )

        # if os.path.exists(os.path.join(PROCESSED_DIR, species, 'hipathia_details')):
        #     logger.info(f'           !!!! Contents removed in following folder --> {os.path.join(PROCESSED_DIR, species, 'hipathia_details')}\n')
        #     os.system(f'rm -rf {os.path.join(PROCESSED_DIR, species, 'hipathia_details')}')
        #     project_path.define_custom_path(custom_path=f'{PROCESSED_DIR}/{species}/hipathia_details')
        
        # else:
            # project_path.define_custom_path(custom_path=f'{PROCESSED_DIR}/{species}/hipathia_details')
        project_path.define_custom_path(custom_path=f'{PROCESSED_DIR}/{species}/hipathia_details')

        # STEP 3. EXPORTING GENE LIST and COLLECTING ENTREZ ID FROM GENE SYMBOL
        # logger.info(f'           ################## gene_from_hipathia.r ##################')
        py_gene_from_hipathia(species=species
                            , raw=species_hipathia
                            , processed=species_hipathia_wo_disease)
        logger.info(f'\n')

        try:
            if not species in GA_DICT.keys():
                logger.info(f'         ⚠️   Given species is not pre-defined!!. .env file is reading for the new species detail ...')
                # load_dotenv()
                values = dotenv_values('.env')
                GA_DICT_CUSTOM = ast.literal_eval(values['GA_DICT_CUSTOM'])
                # print(GA_DICT_CUSTOM)
                if species in GA_DICT_CUSTOM.keys():
                    logger.info(f'         ✅ For given species value, valid reading exist in .env file.')
                    genome_wide_annotation = GA_DICT_CUSTOM[species]
                    # logger.info(f'4444444444444444444444 {genome_wide_annotation}')
            else:
                genome_wide_annotation = GA_DICT[species]
        except FileNotFoundError:
            # logger.info(f"         ⚠️   .env file cannot find: {e}")
            raise  SystemExit(f'         ❌ Execution stoppped!! .env file cannot find!!! ')
        except ValueError:
            raise SystemExit(f'         ❌ Parsing error in .env file!! Please check the file!!')
        except:
            raise SystemExit(f'         ❌ Error in GA_DICT_CUSTOM definition!!')

        # STEP 4. COLLECTING ENTREZ ID FROM GENE SYMBOL
        # logger.info(f'           ################## gene_id_entrez_converter.r ##################')
        py_gene_id_entrez_converter(species=species
                                    , genome_annotation=genome_wide_annotation
                                    , processed=species_hipathia_wo_disease)
        logger.info(f'\n')

        # STEP 5. CREATING PRIOR BIOLOGICAL KNOWLEDGE MATRIX ( SIGNALING PATHWAY and CIRCUIT FROM HIPATHIA )
        # logger.info(f'           ################## bio_layer.py/create_pbk_matrix_hipathia_signaling ##################') 
        create_pbk_matrix_hipathia_signaling(species=species
                                            , processed=species_hipathia_wo_disease
                                            , export_circuit=True)
        # return 0
        logger.info('')
        logger.info('           ✅ EXECUTION COMPLETED SUCCESSFULLY!!! ')
        logger.info('           GENERATED FILES ARE LOCATED IN [PARENT_FOLDER]/data_spn_helper/processed/[SPECIES]  ... ')
        logger.info('           NAME of the GENERATED MATRIX FOR PATHWAYS IS   ---    hsp_pbk_hsa.txt')
        logger.info('           NAME of the GENERATED MATRIX FOR CIRCUITS IS   ---    hsc_pbk_hsa.txt')

def main():
    parser = argparse.ArgumentParser(description='Collecting default PBK knowledge from HiPathia package')
    parser.add_argument('-sp', '--species'
                        , help='organism detail, such as hsa for homo sapiens, mmu for mus musculus, etc.')
    parser.add_argument('-dk', '--disease_keyword'
                        , help='a list of string that contains a disease description, removes disease-related pathway if there is a partially matching'
                        , default=DISEASE_KEYWORD)
    parser.add_argument('-dl', '--disease_list'
                        , help='a list of string that contains the disease name, removes disease-related pathway if there is an exact match'
                        , default=DISEASE_LIST)

    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    process_default_pbk(species=args.species
                        , default_disease_keyword=args.disease_keyword
                        , default_disease_list=args.disease_list
                        )

if __name__ == '__main__':
    try:
        main()
        # logger.info('')
        # logger.info('           EXECUTION COMPLETED SUCCESSFULLY!!! THE EXPORTED MATRIX FOR CLEANED SIGNALING PATHWAYS/CIRCUITS IS LOCATED IN [PARENT_FOLDER]/data_spn_helper/processed/[SPECIES] FOLDER!!!')
        # logger.info('           NAME of the GENERATED MATRIX FOR PATHWAYS IS hsp_pbk_hsa.txt')
        # logger.info('           NAME of the GENERATED MATRIX FOR CIRCUITS IS hsc_pbk_hsa.txt')
    except SystemExit as e:
        print(f": {logger.warning(e)}")
    except:
        print('error occured!!! - default_pbk_hipathia.py')
# %%
