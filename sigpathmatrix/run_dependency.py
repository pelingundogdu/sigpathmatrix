"""
Script Name: run_dependency.py
Description: Installation all necessary libraries
Author: Pelin Gundogdu
Last updated date: July 2026
"""
from . import banner_sigpathmatrix
banner_sigpathmatrix.print_sigpathmatrix_banner()

import logging
import sys

logging.getLogger('numexpr.utils').disabled = True
logging.getLogger('rpy2.situation').disabled = True
logging.getLogger('rpy2.rinterface').disabled = True
logging.getLogger('rpy2.rinterface_lib.embedded').disabled = True
logging.getLogger('rpy2.rinterface_lib.callbacks').disabled = True


# Set up logging for the entire package
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.debug(f'           ################## init ##################')
logger.info(f'           Dependencies installation is started .... ')

from .utils.package_env_manager import run_dependency_installer, setup_project_env

def main():
    try:
        run_dependency_installer()
        logger.info(f'           ✅ Dependencies installation is completed! \n')
        setup_project_env()

        
    except RuntimeError as e:
        print(f'❌ Stopping execution: {e}')
        logger.info(f'           Dependencies installation is stopped!!')
        sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except SystemExit as e:
        print(f": {logger.warning(e)}")
    except:
        print('error occured!!! - run_dependency.py')
# %%
