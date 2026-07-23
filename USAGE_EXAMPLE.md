The execution of the package,

```
(base) USER@USER:[PARENT_FOLDER]$
```

## EXAMPLE - A -- USAGE with EMBEDDED VARIABLES
### STEP 1 - Adding the YAML file into project folder
The user should import the ```environment_sigpathmatrix.yml``` file into theirs ```[PARENT_FOLDER]``` folder.

Folder structure,
``` diff
. [PARENT_FOLDER]
├── ....
+ ├── environment_sigpathmatrix.yml
└── ....
```

### STEP 2 - Curation of ```PYTHON``` environment and activate it

The ```PYTHON``` environment (named ```env_sigpathmatrix```) should be created from ```environment_sigpathmatrix.yml``` file and the new generated ```PYTHON``` environment (```env_sigpathmatrix```) should be activated. All of the function related with this package should execute by using ```env_sigpathmatrix``` environment.
``` 
(base) USER@USER:[PARENT_FOLDER]$ conda env create -f environment_sigpathmatrix.yml
2 channel Terms of Service accepted
Channels:
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

....

done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate env_sigpathmatrix
#
# To deactivate an active environment, use
#
#     $ conda deactivate

(base) USER@USER:[PARENT_FOLDER]$ conda activate env_sigpathmatrix
(env_sigpathmatrix) USER@USER:[PARENT_FOLDER]$ 
```
### STEP 3 - Adding dependencies

>📌 _```[PATH_of_ACTIVE_ENVIRONMENT]``` is the exact location of the new curated ```env_sigpathmatrix``` environment._

The package requires some specific ```PYTHON``` and ```R``` packages. The dependency list is embedded into ```sigpathmatrix``` package. After environment curated, the next step is to install the dependencies into this environement.

``` diff
$ (env_sigpathmatrix) USER@USER:[PARENT_FOLDER]$ DEP_sigpathmatrix


  sss      i      ggg    pppp     aaa     ttt    h   h   m   m    aaa     ttt    rrr       i     x   x  
 s   s     i     g   g   p   p   a   a     t     h   h   mm mm   a   a     t     r   r     i     x   x  
 s         i     g       p   p   a   a     t     h   h   m m m   a   a     t     r   r     i      x x   
  sss      i     g  gg   pppp    aaaaa     t     hhhhh   m   m   aaaaa     t     rrr       i       x    
     s     i     g   g   p       a   a     t     h   h   m   m   a   a     t     r r       i      x x   
 s   s     i     g   g   p       a   a     t     h   h   m   m   a   a     t     r  r      i     x   x  
  sss      i      ggg    p       a   a     t     h   h   m   m   a   a     t     r   r     i     x   x  


INFO:sigpathmatrix.run_dependency:           Dependencies installation is started .... 
INFO:sigpathmatrix.utils.package_env_manager:         🚀 Reading installation yaml file ...
INFO:sigpathmatrix.utils.package_env_manager:         🔄 Preparing Conda installer for: ['rpy2', 'r-reticulate', 'r-logging', 'r-stringr', 'r-argparse', 'python-dotenv', 'bioconductor-hipathia']
INFO:sigpathmatrix.utils.package_env_manager:         📦 Running system command: conda install -y -q -c conda-forge -c bioconda rpy2 r-reticulate r-logging r-stringr r-argparse python-dotenv bioconductor-hipathia
2 channel Terms of Service accepted
Retrieving notices: done
Channels:
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

# All requested packages already installed.

INFO:sigpathmatrix.utils.package_env_manager:         ✅ All Conda and Bioconda dependencies successfully installed!
INFO:sigpathmatrix.run_dependency:           ✅ Dependencies installation is completed! 

INFO:sigpathmatrix.utils.package_env_manager:         .env file already exists. Checking for SPN_PYTHON_PATH and R_HOME content ...
INFO:sigpathmatrix.utils.package_env_manager:         SPN_PYTHON_PATH DEFINITION EXISTS, .env file is updating ... -- SPN_PYTHON_PATH='[PATH_of_ACTIVE_ENVIRONMENT]/bin/python'
INFO:sigpathmatrix.utils.package_env_manager:         R_HOME DEFINITION EXISTS, .env file is updating ... -- R_HOME='[PATH_of_ACTIVE_ENVIRONMENT]/lib/R'
```

### STEP 4 - Executing with default variable

The package can export signaling pathway/circuit detail for two organisms (for homo sapiens```(hsa)``` and mus musculus ```(mmu)```) and with two disease-associated lists.

The given example is for homo-sapiens (hsa) organism with embedded disease-associated list.

``` diff
$ (env_sigpathmatrix) USER@USER:[PARENT_FOLDER]$ MAIN_sigpathmatrix --species hsa
```

Terminal output,

>📌 _```[PATH_of_ACTIVE_ENVIRONMENT]``` is the exact location of the new curated ```env_sigpathmatrix``` environment._

```
(env_sigpathmatrix) USER@USER:[PARENT_FOLDER]$ MAIN_sigpathmatrix -sp hsa


  sss      i      ggg    pppp     aaa     ttt    h   h   m   m    aaa     ttt    rrr       i     x   x  
 s   s     i     g   g   p   p   a   a     t     h   h   mm mm   a   a     t     r   r     i     x   x  
 s         i     g       p   p   a   a     t     h   h   m m m   a   a     t     r   r     i      x x   
  sss      i     g  gg   pppp    aaaaa     t     hhhhh   m   m   aaaaa     t     rrr       i       x    
     s     i     g   g   p       a   a     t     h   h   m   m   a   a     t     r r       i      x x   
 s   s     i     g   g   p       a   a     t     h   h   m   m   a   a     t     r  r      i     x   x  
  sss      i      ggg    p       a   a     t     h   h   m   m   a   a     t     r   r     i     x   x  


INFO:sigpathmatrix.utils.package_env_manager:         .env file already exists. Checking for SPN_PYTHON_PATH and R_HOME content ...
INFO:sigpathmatrix.utils.package_env_manager:         Skipping modification, already defined in .env -- SPN_PYTHON_PATH='[PATH_of_ACTIVE_ENVIRONMENT]/bin/python'
INFO:sigpathmatrix.utils.package_env_manager:         Skipping modification, already defined in .env -- R_HOME='[PATH_of_ACTIVE_ENVIRONMENT]/lib/R'
INFO:sigpathmatrix.default_pbk_hipathia:          MATRIX GENERATION STARTED for hsa .... 
INFO:sigpathmatrix.default_pbk_hipathia:         🔎 DETAIL of GIVEN DISEASE-ASSOCIATED LIST and KEYWORD-LIST
INFO:sigpathmatrix.default_pbk_hipathia:         DISEASE-ASSOCIATED LIST
INFO:sigpathmatrix.default_pbk_hipathia:                    Long-term depression
INFO:sigpathmatrix.default_pbk_hipathia:                    Insulin resistance
INFO:sigpathmatrix.default_pbk_hipathia:                    Measles
INFO:sigpathmatrix.default_pbk_hipathia:                    Amyotrophic lateral sclerosis (ALS)
INFO:sigpathmatrix.default_pbk_hipathia:                    Alcoholism
INFO:sigpathmatrix.default_pbk_hipathia:                    Shigellosis
INFO:sigpathmatrix.default_pbk_hipathia:                    Pertussis
INFO:sigpathmatrix.default_pbk_hipathia:                    Legionellosis
INFO:sigpathmatrix.default_pbk_hipathia:                    Leishmaniasis
INFO:sigpathmatrix.default_pbk_hipathia:                    Toxoplasmosis
INFO:sigpathmatrix.default_pbk_hipathia:                    Tuberculosis
INFO:sigpathmatrix.default_pbk_hipathia:                    Influenza A
INFO:sigpathmatrix.default_pbk_hipathia:                    Glioma
INFO:sigpathmatrix.default_pbk_hipathia:                    Melanoma
INFO:sigpathmatrix.default_pbk_hipathia:
INFO:sigpathmatrix.default_pbk_hipathia:         DISEASE-ASSOCIATED KEYWORD-LIST
INFO:sigpathmatrix.default_pbk_hipathia:                    disease
INFO:sigpathmatrix.default_pbk_hipathia:                    cancer
INFO:sigpathmatrix.default_pbk_hipathia:                    leukemia
INFO:sigpathmatrix.default_pbk_hipathia:                    infection
INFO:sigpathmatrix.default_pbk_hipathia:                    virus
INFO:sigpathmatrix.default_pbk_hipathia:                    addiction
INFO:sigpathmatrix.default_pbk_hipathia:                    anemia
INFO:sigpathmatrix.default_pbk_hipathia:                    cell carcinoma
INFO:sigpathmatrix.default_pbk_hipathia:                    diabet
INFO:sigpathmatrix.default_pbk_hipathia:                    Hepatitis
INFO:sigpathmatrix.default_pbk_hipathia:
INFO:sigpathmatrix.hipathia.collect_bio_layer:           ################## collect_hipathia_pathway ##################
INFO:sigpathmatrix.hipathia.collect_bio_layer:           Hipathia -- the total of 146 signaling pathways are exported into
INFO:sigpathmatrix.hipathia.collect_bio_layer:                        [[PARENT_FOLDER]/data_spn_helper/raw/[SPECIES]/hipathia_pathway_ids_and_names.csv]

INFO:sigpathmatrix.default_pbk_hipathia:
INFO:sigpathmatrix.hipathia.collect_bio_layer:           ################## remove_disease_pathways ##################
INFO:sigpathmatrix.hipathia.collect_bio_layer:           Pathway list is imported from 
INFO:sigpathmatrix.hipathia.collect_bio_layer:                        [[PARENT_FOLDER]/data_spn_helper/raw/[SPECIES]/hipathia_pathway_ids_and_names.csv]!!, 
INFO:sigpathmatrix.hipathia.collect_bio_layer:           Imported pathway list detail. (146, 2)
INFO:sigpathmatrix.hipathia.collect_bio_layer:           Filtered by DISEASE_KEYWORD list!!, (107, 2)
INFO:sigpathmatrix.hipathia.collect_bio_layer:           Filtered by DISEASE_LIST list!!, (93, 2)
INFO:sigpathmatrix.hipathia.collect_bio_layer:           Disease realted pathways are eliminated, and 93 pathway is exported into 
INFO:sigpathmatrix.hipathia.collect_bio_layer:                        [[PARENT_FOLDER]/data_spn_helper/processed/[SPECIES]/hipathia_pathway_ids_and_names.csv]

INFO:sigpathmatrix.hipathia.py_collect_gene_entrezid:           ################## gene_from_hipathia.r ##################
INFO:sigpathmatrix.hipathia.r_collect_gene_entrezid:           hipathia pathways are exporting for hsa
INFO:sigpathmatrix.hipathia.r_collect_gene_entrezid:           raw        ----  [PARENT_FOLDER]/data_spn_helper/raw/[SPECIES]/hipathia_gene_list_all.csv
INFO:sigpathmatrix.hipathia.r_collect_gene_entrezid:           processed  ----  [PARENT_FOLDER]/data_spn_helper/processed/[SPECIES]/hipathia_gene_list.csv
INFO:sigpathmatrix.hipathia.r_collect_gene_entrezid:           details    ----  [PARENT_FOLDER]/data_spn_helper/processed/[SPECIES]/hipathia_details
INFO:sigpathmatrix.hipathia.r_collect_gene_entrezid:  
INFO:sigpathmatrix.hipathia.r_collect_gene_entrezid:           DETAILS of COLLECTED SIGNALING PATHWAYS
INFO:sigpathmatrix.hipathia.r_collect_gene_entrezid:           Number of pathway                       , 146
INFO:sigpathmatrix.hipathia.r_collect_gene_entrezid:           Number of sub-pathways (effector genes) , 1876
INFO:sigpathmatrix.hipathia.r_collect_gene_entrezid:  
INFO:sigpathmatrix.hipathia.r_collect_gene_entrezid:           DETEAILS of CLEANED SIGNALING PATHWAYS (eliminated disease-associated)
INFO:sigpathmatrix.hipathia.r_collect_gene_entrezid:           Number of pathway                       , 93
INFO:sigpathmatrix.hipathia.r_collect_gene_entrezid:           Number of sub-pathways (effector genes) , 1211
INFO:sigpathmatrix.default_pbk_hipathia:

INFO:sigpathmatrix.hipathia.py_collect_gene_entrezid:           ################## gene_id_entrez_converter.r ##################
INFO:sigpathmatrix.hipathia.py_collect_gene_entrezid:           GENE annotation information from config file, org.Hs.eg.db
INFO:sigpathmatrix.hipathia.r_collect_gene_entrezid:           The number of gene in entrez_and_symbol_list, 2987
INFO:sigpathmatrix.hipathia.r_collect_gene_entrezid:           File exported!! - [PARENT_FOLDER]/data_spn_helper/processed/[SPECIES]/entrez_and_symbol.csv
INFO:sigpathmatrix.default_pbk_hipathia:

INFO:sigpathmatrix.hipathia.collect_bio_layer:           ################## create_pbk_matrix_hipathia_signaling ##################
INFO:sigpathmatrix.hipathia.collect_bio_layer:           Entrez gene id and symbol detail
INFO:sigpathmatrix.hipathia.collect_bio_layer:           Shape of the dataset, (2987, 2)
INFO:sigpathmatrix.hipathia.collect_bio_layer:                gene_id   symbol
INFO:sigpathmatrix.hipathia.collect_bio_layer:           0      10000     AKT3
INFO:sigpathmatrix.hipathia.collect_bio_layer:           1      10010     TANK
INFO:sigpathmatrix.hipathia.collect_bio_layer:           2  100132074    FOXO6
INFO:sigpathmatrix.hipathia.collect_bio_layer:           3  100132285  KIR2DS2
INFO:sigpathmatrix.hipathia.collect_bio_layer:           4  100132463   CLDN24
INFO:sigpathmatrix.hipathia.collect_bio_layer:           Checking NA values, number of NA values, 0

INFO:sigpathmatrix.hipathia.collect_bio_layer:           PATHWAY connection detail, (2987, 94)
INFO:sigpathmatrix.hipathia.collect_bio_layer:               symbol  hsa03320  hsa04010  hsa04012
INFO:sigpathmatrix.hipathia.collect_bio_layer:           0     akt3       0.0       1.0       1.0
INFO:sigpathmatrix.hipathia.collect_bio_layer:           1     tank       0.0       0.0       0.0
INFO:sigpathmatrix.hipathia.collect_bio_layer:           2    foxo6       0.0       0.0       0.0
INFO:sigpathmatrix.hipathia.collect_bio_layer:           3  kir2ds2       0.0       0.0       0.0
INFO:sigpathmatrix.hipathia.collect_bio_layer:           4   cldn24       0.0       0.0       0.0
INFO:sigpathmatrix.hipathia.collect_bio_layer:           PATHWAY -- the number of total connection, 9274.0
INFO:sigpathmatrix.hipathia.collect_bio_layer:           PBK - PATHWAY MATRIX EXPORTED!! - [PARENT_FOLDER]/data_spn_helper/processed/[SPECIES]/hsp_pbk_hsa.txt

INFO:sigpathmatrix.hipathia.collect_bio_layer:           CIRCUIT connection detail, (2987, 1212)
INFO:sigpathmatrix.hipathia.collect_bio_layer:               symbol  P-hsa03320-62  P-hsa03320-45  P-hsa03320-43MAIN_sigpathmatrix
INFO:sigpathmatrix.hipathia.collect_bio_layer:           0     akt3            0.0            0.0            0.0
INFO:sigpathmatrix.hipathia.collect_bio_layer:           1     tank            0.0            0.0            0.0
INFO:sigpathmatrix.hipathia.collect_bio_layer:           2    foxo6            0.0            0.0            0.0
INFO:sigpathmatrix.hipathia.collect_bio_layer:           3  kir2ds2            0.0            0.0            0.0
INFO:sigpathmatrix.hipathia.collect_bio_layer:           4   cldn24            0.0            0.0            0.0
INFO:sigpathmatrix.hipathia.collect_bio_layer:           CIRCUIT -- the number of total connection, 48216.0
INFO:sigpathmatrix.hipathia.collect_bio_layer:           PBK - CIRCUIT MATRIX EXPORTED!! - [PARENT_FOLDER]/data_spn_helper/processed/[SPECIES]/hsc_pbk_hsa.txt

INFO:sigpathmatrix.default_pbk_hipathia:
INFO:sigpathmatrix.default_pbk_hipathia:           ✅ EXECUTION COMPLETED SUCCESSFULLY!!! 
INFO:sigpathmatrix.default_pbk_hipathia:           GENERATED FILES ARE LOCATED IN [PARENT_FOLDER]/data_spn_helper/processed/[SPECIES]  ... 
INFO:sigpathmatrix.default_pbk_hipathia:           NAME of the GENERATED MATRIX FOR PATHWAYS IS   ---    hsp_pbk_hsa.txt
INFO:sigpathmatrix.default_pbk_hipathia:           NAME of the GENERATED MATRIX FOR CIRCUITS IS   ---    hsc_pbk_hsa.txt
```

####  Folder structure after execution

``` diff
. [PARENT_FOLDER]
├── ....
+ ├── data_spn_helper
+ │   ├── processed
+ │   │   └── {SPECIES}
+ │   │       ├── entrez_and_symbol.csv
+ │   │       ├── hipathia_details
+ │   │       │   ├── hsa03320_gene_list.txt
+ │   │       │   ├── ....... [GENE LIST for EACH INDIVIDUAL PATHWAY]
+ │   │       │   └── hsa05100_gene_list.txt
+ │   │       ├── hipathia_gene_list.csv
+ │   │       ├── hipathia_pathway_ids_and_names.csv
+ │   │       ├── hsc_pbk_hsa.txt
+ │   │       └── hsp_pbk_hsa.txt
+ │   └── raw
+ │       └── {SPECIES}
+ │           ├── hipathia_gene_list_all.csv
+ │           └── hipathia_pathway_ids_and_names.csv
+ ├── .env
├── environment_sigpathmatrix.yml
└── ....
```


## EXAMPLE - B -- USAGE with CUSTOM DEFINED LIST

> _Note, [Step 1](#step-1---adding-the-yaml-file-into-project-folder), [Step 2](#step-2---curation-of-python-environment-and-activate-it)  and [Step 3](#step-3---adding-dependencies) explained in [Example A](#example---a----usage-with-embedded-variables) should be completed before continue the next step._

The given example is reading custom disease-associated list for a homo-sapiens (hsa) from ```.env``` file.

Definition of custom disease-associated list in ```.env``` file,
```
....
CUSTOM_DISEASE_LIST='["Long-term depression","Insulin resistance","Measles","Amyotrophic lateral sclerosis (ALS)","Alcoholism","Shigellosis","Pertussis","Legionellosis","Leishmaniasis","Toxoplasmosis","Tuberculosis","Influenza A","Glioma","Melanoma"]'
CUSTOM_DISEASE_KEYWORD='["disease","cancer","leukemia","infection","virus","addiction","anemia","cell carcinoma","diabet","Hepatitis"]'
CUSTOM_DISEASE_LIST_EMPTY="[]"
CUSTOM_DISEASE_KEYWORD_EMPTY="[]"
CUSTOM_DISEASE_LIST_EMPTY2=""
CUSTOM_DISEASE_KEYWORD_EMPTY2=""
....
```

Usage with custom disease-associated list in ```.env``` file,
``` diff
+ (env_sigpathmatrix) USER@USER:[PARENT_FOLDER]$ $ source .env && MAIN_sigpathmatrix --species hsa -dl "$CUSTOM_DISEASE_LIST" -dk "$CUSTOM_DISEASE_KEYWORD"
```
Other usage example,
``` diff
+ (env_sigpathmatrix) USER@USER:[PARENT_FOLDER]$ $ source .env && MAIN_sigpathmatrix --species mmu -dl "$CUSTOM_DISEASE_LIST_EMPTY" -dk "$CUSTOM_DISEASE_KEYWORD_EMPTY"
```
