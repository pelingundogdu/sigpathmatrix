# scripts/path_manager.py
from pathlib import Path
import shutil
from typing import Optional

class ProjectPaths:
    """Manage project paths dynamically"""
    
    def __init__(self, root_path: Optional[Path] = None):
        if root_path is None:
            # Try to find project root containing 'dataspn_helper' folder
            current = Path(__file__).resolve().parent.parent # Go to parent folder
            while current != current.parent:
                if (current / 'data_spn_helper_find').exists():
                    self.root = current
                    break
                current = current.parent
            else:
                self.root = Path.cwd()
        else:
            self.root = Path(root_path)
        
        self.data_spn_helper = self.root / 'data_spn_helper'
        self.raw = self.data_spn_helper / 'raw'
        self.processed = self.data_spn_helper / 'processed'
    
    def ensure_dirs(self):
        """Create all directories if they don't exist"""

        for dir_path in [self.data_spn_helper, 
                         self.raw, 
                         self.processed
                         ]:
            dir_path.mkdir(parents=True, exist_ok=True)
        return self
    

    # def ensure_dirs(self):
    #     """Delete the main dta folder and generate subfolders"""

    #     # Delete data_spn_helper folder if it exists
    #     if self.data_spn_helper.exists():
    #         # print('!!!!!!!!!!!!!!!!!!!!!!!!!!IMPORTANT data_spn_helper deleted!!!!!!!!!!!!!!!!!!!!!!!!!!')
    #         shutil.rmtree(self.data_spn_helper)

    #     # generate the folder structure
    #     for dir_path in [self.data_spn_helper, 
    #                      self.raw, 
    #                      self.processed
    #                      ]:
    #         dir_path.mkdir(parents=True, exist_ok=True)
    #     return self


    def get_file(self, filename: str, category: str = 'raw') -> Path:
        """Get path for a specific file"""
        category_map = {
            'data_spn_helper': self.data_spn_helper,
            'raw': self.raw,
            'processed': self.processed

        }
        return category_map.get(category, self.data_spn_helper) / filename
    
    def call_path():
        print('calling paths function is working')

    def define_custom_path(self, custom_path: str, delete_if_exist: bool = False):
        path = f'{custom_path}'

        if delete_if_exist==True and Path(path).exists():
            # print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!IMPORTANT {path} deleted!!!!!!!!!!!!!!!!!!!!!!!!!!')
            shutil.rmtree(Path(path))

        Path(path).mkdir(parents=True, exist_ok=True)

    def __repr__(self):
        return f"ProjectPaths(root={self.root})"


# Create a singleton instance for easy import
paths = ProjectPaths().ensure_dirs()