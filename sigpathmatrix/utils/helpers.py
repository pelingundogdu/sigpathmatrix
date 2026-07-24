# from pathlib import Path
# from typing import Dict, Any
# import yaml

# class ConfigLoader:
#     """Utility class to load and manage configuration files"""
    
#     def __init__(self, config_path: str):
#         self.config_path = Path(config_path)
#         self.config = self.load_config()
        
#     def load_config(self) -> Dict[str, Any]:
#         """Load YAML configuration file"""
#         if not self.config_path.exists():
#             raise FileNotFoundError(f"Config file not found: {self.config_path}")
#         with open(self.config_path, 'r') as f:
#             config = yaml.safe_load(f)
#         return config
    

# # def update_env_dotenv():
# #     env_file = '.env'
# #     # Load existing .env
# #     load_dotenv(env_file)
# #     # Update variables
# #     set_key(env_file, 'SPN_PYTHON_PATH', sys.executable)
# #     set_key(env_file, 'SPN_PYTHON_PATH1', sys.executable)
# #     set_key(env_file, 'PYTHON_VERSION', sys.version.split()[0])
# #     set_key(env_file, 'VIRTUAL_ENV', os.environ.get('VIRTUAL_ENV', ''))
    
# #     print(f"✅ Updated {env_file}")
