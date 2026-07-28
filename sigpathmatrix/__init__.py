# sigPrimedNet_pbk/__init__.py
# This file makes 'sigPrimedNet_pbk' a Python package

# from . import banner_sigpathmatrix
# banner_sigpathmatrix.print_sigpathmatrix_banner()

import logging
# import sys
# Suppress rpy2.situation logging

# logging.getLogger('rpy2.situation').setLevel(logging.INFO)
# logging.getLogger('rpy2.situation').setLevel(logging.WARNING)
# logging.getLogger('rpy2.rinterface').setLevel(logging.INFO)
# logging.getLogger('rpy2.rinterface').setLevel(logging.WARNING)
# logging.getLogger('rpy2.rinterface_lib.embedded').setLevel(logging.INFO)
# logging.getLogger('rpy2.rinterface_lib.embedded').setLevel(logging.WARNING)
# logging.getLogger('rpy2.rinterface_lib.callbacks').setLevel(logging.INFO)
# logging.getLogger('rpy2.rinterface_lib.callbacks').setLevel(logging.WARNING)
logging.getLogger('numexpr.utils').disabled = True
logging.getLogger('rpy2.situation').disabled = True
logging.getLogger('rpy2.rinterface').disabled = True
logging.getLogger('rpy2.rinterface_lib.embedded').disabled = True
logging.getLogger('rpy2.rinterface_lib.callbacks').disabled = True


# # Set up logging for the entire package
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
# logger.debug(f'           ################## init ##################')
# logger.info(f'           Dependencies installation is started .... ')


# from .utils.package_env_manager import run_dependency_installer, setup_project_env


# # from .hipathia.collect_bio_layer import collect_hipathia_pathway, remove_disease_pathways
# # from .utils.helpers import ConfigLoader
# # from .utils.path_manager import paths, ProjectPaths


# try:
#     run_dependency_installer()
#     logger.info(f'           ✅ Dependencies installation is completed! \n')
#     setup_project_env()

#     # __all__ = ['paths', 'ProjectPaths', 'ConfigLoader'
#     #         , 'collect_hipathia_pathway', 'remove_disease_pathways'
#     #         ]
    
# except RuntimeError as e:
#     print(f'❌ Stopping execution: {e}')
#     logger.info(f'           Dependencies installation is stopped!!')
#     sys.exit(1)



# from .hipathia.collect_bio_layer import collect_hipathia_pathway, remove_disease_pathways
# from .utils.helpers import ConfigLoader
from .hipathia import collect_bio_layer, py_collect_gene_entrezid
from .utils import package_env_manager, path_manager
from .default_pbk_hipathia import *
from .run_dependency import *
from .spn_config import *

__all__ = ['default_pbk_hipathia',
           'run_dependency',
           'collect_bio_layer',
           'py_collect_gene_entrezid',
           'package_env_manager',
           'path_manager',
           'spn_config'
        #    , 'ConfigLoader'
        # , 'collect_hipathia_pathway', 'remove_disease_pathways'
        ]
