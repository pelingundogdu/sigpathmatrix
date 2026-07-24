import logging

# custom functions
from .utils import path_manager

# Set up logging for the entire package
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.debug(f'           ################## spn_config ##################')

# # You can add additional configuration here
# PROJECT_NAME = "SigPrimedNet PBK"
# VERSION = "1.0.0"

# Re-export paths for convenience
DATA_SPN_HELPER_DIR = path_manager.paths.data_spn_helper
RAW_DIR = path_manager.paths.raw
PROCESSED_DIR = path_manager.paths.processed

logger.debug(f' Project parent folder, ---- {path_manager.paths.root}\n')

def setup_project():
    """Initialize project directories"""
    path_manager.paths.ensure_dirs()
    print(f" Project initialized at {path_manager.paths.root}")


DISEASE_KEYWORD = ['disease', 'cancer', 'leukemia', 'infection', 'virus'
                   ,'addiction', 'anemia', 'cell carcinoma', 'diabet', 'Hepatitis']
DISEASE_LIST = ['Long-term depression', 'Insulin resistance', 'Measles'
                , 'Amyotrophic lateral sclerosis (ALS)', 'Alcoholism'
                , 'Shigellosis', 'Pertussis', 'Legionellosis', 'Leishmaniasis'
                , 'Toxoplasmosis', 'Tuberculosis', 'Influenza A', 'Glioma', 'Melanoma']

# for more option , please check https://bioconductor.org/packages/3.23/data/annotation/
GA_DICT = {'hsa':'org.Hs.eg.db', 'mmu':'org.Mm.eg.db'}
