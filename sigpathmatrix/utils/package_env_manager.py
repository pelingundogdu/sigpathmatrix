"""
Script Name: package_env_manager.py

Description: The function of sigPrimedNet_PBK package needs essential package.
             In addition, the path information of the currenct environment is needed 
             to be defined for both PYTHON and R environment.

Author: Pelin Gundogdu

Last updated date: July 2026

Script details;
    a. Loading dependency;
        run_dependency_installer()
            load_dependencies()
    b. Generating and updating .env file;
        setup_project_env()
            check_env_line_exist()
"""

# Import importlib.resources (built into Python 3.9+)
from importlib import resources
import logging
import os
from pathlib import Path
import sys
import subprocess
import yaml


# Set up logging for the entire package
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.debug(f'           ################## package_env_manager.py ##################')

def load_dependencies():
    '''
    Locate and parse the dependencies.yml file which contains
    the list of package which are essential for the package.
    '''

    # selection of the dependencies.yml file
    yaml_path = resources.files('sigpathmatrix').joinpath('dependencies.yml')
    
    # checking the file if it is located in giving path or not
    if not yaml_path.exists():
        raise FileNotFoundError(f'Could not find dependency manifest at {yaml_path}')
    
    # reading the yaml file
    with open(yaml_path, 'r') as f:
        return yaml.safe_load(f)

def run_dependency_installer():
    '''
    Execution the installation of the essential package which are
    listed in dependencies.yml 
    '''

    logger.info('         🚀 Reading installation yaml file ...')
    deps = load_dependencies()
    
    # channel detail which is needed for the package installation
    channels = deps.get('conda_channels', ['conda-forge'])
    # the list of conda packages
    conda_pkgs = deps.get('conda_packages', [])
    # the list of bioconda packages
    bioconda_pkgs = deps.get('bioconda_packages', [])
    # Combine all packages to be installed via conda
    all_packages = conda_pkgs + bioconda_pkgs
    
    # Check if the user inside of a conda environment
    if all_packages and ('CONDA_PREFIX' in os.environ):
        logger.info(f'         🔄 Preparing Conda installer for: {all_packages}')
        
        # Base command
        conda_cmd = ['conda', 'install', '-y', '-q']
        
        # append channels from YAML (e.g., -c conda-forge -c bioconda)
        for channel in channels:
            conda_cmd.extend(['-c', channel])
            
        # Append the package list
        conda_cmd.extend(all_packages)
        
        logger.info(f'         📦 Running system command: {' '.join(conda_cmd)}')
        try:
            subprocess.run('conda install -c conda-forge r-base -y', shell=True)
            subprocess.run(conda_cmd
                           , check=True
                           , capture_output=True  # capturing both stdout and stderr
                           , text=True  # returning output as str instead of bytes
                           )
            logger.info('         ✅ All Conda and Bioconda dependencies successfully installed!')

        except subprocess.CalledProcessError as e:
            # print(f"Return code: {e.returncode}")
            # print(f"STDERR: {e.stderr}")
            # print(f"STDOUT: {e.stdout}")
            if 'unrecognized arguments' in e.stderr:
                logger.warning(f'         ❌ Conda error: Unrecognized arguments detected!')
                # Handling unrecognized argument error
                raise RuntimeError('Conda command failed due to unrecognized arguments') from e
            else:
                # Handle other conda errors
                logger.warning(f'         ❌ Other conda error: {e.stderr}')
                raise RuntimeError('Conda command failed!!!!') from e

    else:
        logger.info('         ⚠️ Active Conda environment not detected. Skipping automated background installations.')
        raise RuntimeError('Please activate your Ptyhon environment!') from e


def check_env_line_exist(env_path: Path, path_keyword: str, env_line: str):

    '''Checking the PYTHON and R environment information in .env file
    
    Parameters:
        env_path : Path
            The location of the current working environment
        path_keyword: str
            The keyword value of the environmnet. It is using to check any duplication or old version definition
        env_line: str
            The environment definition
    Returns:
        Generating and updating the .env file
    '''
    content_exist_multiple = 0
    check_duplication = 0
    # Reading the content of file to avoid duplicate entries
    with open(env_path, 'r') as f:
        content = f.readlines()
    # logger.info(f'\n\ncontent: \n{content}\n\n{content_exist_multiple}\n\n')

    for i in content:
        if path_keyword in i:
            content_exist_multiple += 1
        if env_line in i:
            check_duplication += 1

    
    other_items = [l for l in content if not l.startswith(path_keyword)]

    # Checking the content
    # check if the content exist for once then it is skipping 
    if env_line in content and content_exist_multiple == 1 and check_duplication == 1:
        logger.info(f'         Skipping modification, already defined in .env -- {env_line.replace('\n','')}')
    # checking any duplication or old verion
    elif (env_line in content and content_exist_multiple > 1 and check_duplication > 1) or \
          (content_exist_multiple >= 1 and check_duplication == 0):
        logger.info(f'         {path_keyword} DEFINITION EXISTS, .env file is updating ... -- {env_line.replace('\n','')}')
        with open(env_path, 'w') as f:
            f.write(env_line)
            for i_l in other_items:
                f.write(i_l)
    elif content_exist_multiple == 0 and check_duplication == 0:
        # Appending the environment detail into .env file
        with open(env_path, 'a') as f:
            f.write(env_line)
        logger.info(f'         Added into .env -- {env_line}')
    else:
        raise RuntimeError('Please check .env file for an error !!')

def setup_project_env():
    '''
    Generate .env file and defining the PYTHON and R environment.
    The package uses both Python and R environment to collect and export 
    signaling pathways/circuits matrix. For this reason, we generated
    the .env and added essential information into this file.
    '''
    # Calling root(parent) path of the project root.
    # IMPORTANT_NOTE, the bash command is being run in this path
    project_root = Path(os.getcwd())
    # print(f'TESTIN PROJECT ROOT PATH ----- {project_root}')
    env_path = project_root / '.env'
    
    # 2. Get the current Python interpreter path being used
    current_python_path = Path(sys.executable).parent.parent
    python_env_line = f"SPN_PYTHON_PATH='{current_python_path}/bin/python'\n"
    r_env_line = f"R_HOME='{current_python_path}/lib/R'\n"
    
    # print(f"Checking for .env in: {project_root}")
    
    # 3. Check if .env exists
    if env_path.exists():
        logger.info(f'         .env file already exists. Checking for SPN_PYTHON_PATH and R_HOME content ...')
        
        check_env_line_exist(env_path=env_path, path_keyword='SPN_PYTHON_PATH', env_line=python_env_line)
        check_env_line_exist(env_path=env_path, path_keyword='R_HOME', env_line=r_env_line)
            
    else:
        # 4. Create the file if it does not exist
        with open(env_path, 'w') as f:
            f.write(python_env_line)
            f.write(r_env_line)
        logger.info(f'           Created new .env file and added SPN_PYTHON_PATH: {python_env_line}')
        logger.info(f'           Created new .env file and added R_HOME: {r_env_line}')
        logger.info(f'           ✅ Updated .env file!!')