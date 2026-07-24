# %%
# Import Python package
import glob
import os
import logging
import pandas as pd
from rpy2.rinterface import RRuntimeWarning
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
import warnings
warnings.filterwarnings("ignore", category=RRuntimeWarning)

# Set up logging for the entire package
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import R packages
base = importr('base')
hipathia = importr('hipathia')

def collect_hipathia_pathway(species: str
                             , path_data_raw: str ) -> pd.DataFrame:
    """
    Collecting HiPathia pathway information for the given species and export into given data folder.
    
    Parameters:
    -----------
    species : str
        The species identifier (e.g., 'hsa' for homo sapiens, 'mmu' for mus musculus)
    path_data_raw : str
        Folder location, the unfiltered pathway list will be exported
    
    Returns:
    --------
    df_pathway : pd.DataFrame
        DataFrame containing collected pathway information
    """
    
    logger.info(f'           ################## collect_hipathia_pathway ##################')
    try:
        pathways = hipathia.load_pathways(species = species)
    except:
        raise SystemExit(f'         ❌ Invalid species definition. Hipathia package cannot collect data for the given species!!')

    list_all_labelids = list(pathways.rx2('all.labelids').colnames)
    df_pathways_all_labelids = pd.DataFrame(columns=list_all_labelids)

    len_full = len(pathways.rx2('all.labelids'))
    index_range = len_full/len(list_all_labelids)
    for i in range(len(df_pathways_all_labelids.columns)):
        i_start = int(i * index_range)
        i_end = int(i_start + index_range)
        df_pathways_all_labelids[list_all_labelids[i]] = list(pathways.rx2('all.labelids'))[i_start:i_end]#[i_start:i_start+index_range])
        
    df_pathway = df_pathways_all_labelids[['path.id', 'path.name']]

    df_pathway = df_pathway[['path.id','path.name']].drop_duplicates()
    df_pathway.reset_index(drop=True, inplace=True)
    
    # Export hipathia pathways into given path
    df_pathway.to_csv(f'{path_data_raw}/hipathia_pathway_ids_and_names.csv')
    logger.info(f'           Hipathia -- the total of {len(df_pathway)} signaling pathways are exported into')
    logger.info(f'                        [{path_data_raw}/hipathia_pathway_ids_and_names.csv]\n')
    # logger.info(f'\n')

    return df_pathway

def remove_disease_pathways(input_pathway: str
                            , output_folder: str
                            , disease_keyword: list
                            , disease_list: list) -> pd.DataFrame:
    """
        Removing disease-associated pathways from collected data. The data, by default, is collecting from HiPathia package. The raw data (input_pathway) is a list of pathway name and ID pairs.
        This function reads the collected raw pairs and removes the pathway if it does exist in any of the given list (disease_keyword or disease_list).
        Both list has same tasks which searches the raw list and checks for any matching pathway within given lists.
        Only difference is the matching type, means that the disease_keyword does look for a PARTIAL matching while disease_list does look for an EXACT matching.
        
        Parameters:
        -----------
        input_pathway : str
            The collected pathway information
        output_folder : str
            The file location, the filtered pathway list will be exported into this given location
        disease_keyword : list
            The list of keyword which will be used for a PARTIAL matching
        disease_list : list
            The list of pathway name which will be used for an EXACT matching
        
        Returns:
        --------
        df_pathway : pd.DataFrame
            The list of disease-associated-free pathway
    """

    logger.info(f'           ################## remove_disease_pathways ##################')
    logger.info(f'           Pathway list is imported from ')
    logger.info(f'                        [{input_pathway}]!!, ')

    df_pathway = pd.read_csv(input_pathway, index_col=0)
    logger.info(f'           Imported pathway list detail. {df_pathway.shape}')
    # FILTERING #1
    if len(disease_keyword) > 1:
        df_pathway = df_pathway.loc[~df_pathway['path.name'].str.contains('|'.join(disease_keyword))]
        logger.info(f'           Filtered by DISEASE_KEYWORD list!!, {df_pathway.shape}')

    # FILTERING #2
    if len(disease_list) > 1:
        df_pathway = df_pathway.loc[~df_pathway['path.name'].isin(disease_list)]
        logger.info(f'           Filtered by DISEASE_LIST list!!, {df_pathway.shape}')

    df_pathway.reset_index(drop=True, inplace=True)
    # Export disease-free pathways into given path
    df_pathway.to_csv(f'{output_folder}/hipathia_pathway_ids_and_names.csv')
    logger.info(f'           Disease realted pathways are eliminated, and {len(df_pathway)} pathway is exported into ')
    logger.info(f'                        [{output_folder}/hipathia_pathway_ids_and_names.csv]\n')
    # logger.info(f'\n')

    return df_pathway


def create_pbk_matrix_hipathia_signaling(species: str
                                         , processed: str
                                         , export_circuit: bool):
    """
        Exporting pathway and circuit dataset. The exported data gene vs pathway/circuit. It shows the connection details of each pathway-gene and circuit-gene pairs.
        The exported files are the main prior biological knowledge information and can be used for integrating with desired neural network.
        
        Parameters:
        -----------
        species : str
            The organism detail
        processed : str
            The file location, the filtered pathway list will be exported into this given location
        export_circuit : bool
            The list of keyword which will be used for a PARTIAL matching
      
        Returns:
        --------
            Two dataset is exporting for both pathway and circuit
    """
    
    logger.info(f'           ################## create_pbk_matrix_hipathia_signaling ##################')
    
    # defining output file
    # hsp -- hipathia signaling pathway
    output_hsp =  f"{os.path.join(processed, f'hsp_pbk_{species}.txt')}"
    # hsc -- hipathia signaling circuit
    output_hsc =  f"{os.path.join(processed, f'hsc_pbk_{species}.txt')}"
    
    # importing raw dataset which is imported by hipathia
    df_entrez_symbol = pd.read_csv(os.path.join(processed, 'entrez_and_symbol.csv'), dtype={'gene_id':str})
    df_entrez_circuit = df_entrez_symbol.copy()
    logger.info(f'           Entrez gene id and symbol detail')
    logger.info(f'           Shape of the dataset, {df_entrez_symbol.shape}')
    for line in df_entrez_symbol.head().to_string().splitlines():
        logger.info(f'           {line}')
    logger.info(f'           Checking NA values, number of NA values, {len(df_entrez_symbol.loc[df_entrez_symbol['symbol'].isna()])}\n')
    
    for i_pathway in sorted(glob.glob(os.path.join(processed, 'hipathia_details/*gene_list.txt'))):
        # Reading selected pathways which shows the gene relation for each circuits
        df_i_pathway = pd.read_csv(i_pathway, index_col=0, dtype={'entrez':str}).fillna(value=0)
        df_i_circuit = df_i_pathway.copy()

        # Replace columns names which is circuit name with pathway name
        df_i_pathway.columns = [pw[1] for pw in df_i_pathway.columns.str.split('-')]
        # Grouping all circuit as pathway representation
        # df_i_pathway = df_i_pathway.groupby(df_i_pathway.columns).max() # DEPRECATED FUNCTION (axis=1)
        df_i_pathway = df_i_pathway.T.reset_index().groupby(by=['index']).max().T
        # Merging entrez_and_symbol dataset with pathway information dataset
        df_entrez_symbol = pd.merge(left=df_entrez_symbol
                                    , right=df_i_pathway
                                    , left_on='gene_id'
                                    , right_index=True
                                    , how='left')
        df_entrez_symbol.fillna(value=0, inplace=True)
    
        if export_circuit == True:
            df_entrez_circuit = pd.merge(left=df_entrez_circuit
                                        , right=df_i_circuit
                                        , left_on='gene_id'
                                        , right_index=True
                                        , how='left')
            # print(i_pathway)
            df_entrez_circuit.fillna(value=0, inplace=True)

    # Updating 'symbol' values as lowercase
    df_entrez_symbol['symbol'] = df_entrez_symbol['symbol'].str.lower()    
    df_entrez_symbol.drop(columns=['gene_id'], inplace=True)
    # EXPORTING - the prior biological knowledge layer - PATHWAY
    df_entrez_symbol.to_csv(output_hsp, index=False)
    logger.info(f'           PATHWAY connection detail, {df_entrez_symbol.shape}')
    for line in df_entrez_symbol.head().iloc[:, :4].to_string().splitlines():
        logger.info(f'           {line}')
    logger.info(f'           PATHWAY -- the number of total connection, {df_entrez_symbol.sum().values[1:].sum()}')
    logger.info(f'           PBK - PATHWAY MATRIX EXPORTED!! - {output_hsp}\n')

    if export_circuit == True:
        # Updating 'symbol' values as lowercase
        df_entrez_circuit['symbol'] = df_entrez_circuit['symbol'].str.lower()    
        df_entrez_circuit.drop(columns=['gene_id'], inplace=True)
        # EXPORTING - the prior biological knowledge layer - CIRCUIT
        df_entrez_circuit.to_csv(output_hsc, index=False)
        logger.info(f'           CIRCUIT connection detail, {df_entrez_circuit.shape}')
        for line in df_entrez_circuit.head().iloc[:, :4].to_string().splitlines():
            logger.info(f'           {line}')
        logger.info(f'           CIRCUIT -- the number of total connection, {df_entrez_circuit.sum().values[1:].sum()}')
        logger.info(f'           PBK - CIRCUIT MATRIX EXPORTED!! - {output_hsc}\n')