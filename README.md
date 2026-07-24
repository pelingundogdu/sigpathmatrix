


<!-- # SigPrimedNet -- Signaling Pathway/Circuit Matrix Generator -->


<p style="text-align: center"><img src="https://github.com/user-attachments/assets/1a4abb89-74ea-41af-971c-138ed490daeb"></p>

<!-- <p style="text-align: center"><img src="https://github.com/user-attachments/assets/4ac0f261-58b0-43da-a43e-d9fd29fc1d92"></p> -->


<div align="center">

[![PyPI version](https://img.shields.io/pypi/v/sigpathmatrix.svg?color=pink)](https://pypi.org/project/sigpathmatrix/)
![PyPI - License](https://img.shields.io/pypi/l/sigpathmatrix)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/pelingundogdu/sigpathmatrix)
![GitHub stars](https://img.shields.io/github/stars/pelingundogdu/sigpathmatrix)

![GitHub last commit](https://img.shields.io/github/last-commit/pelingundogdu/sigpathmatrix)
![GitHub issues](https://img.shields.io/github/issues/pelingundogdu/sigpathmatrix)
![GitHub forks](https://img.shields.io/github/forks/pelingundogdu/sigpathmatrix)

</div>

# 

# sigpathmatrix: **SIG**naling **PATH**way/circuit **MATRIX** generator 

**sigpathmatrix** is a Python package that collects and exports signaling pathway and circuit information. This package contains helper functions that are using to generate the biological prior knowledge detail for the **SigPrimedNet [1]** network. The curated matrices specify the relationships between genes and corresponding pathway/circuit they belong to.

### Purpose

The primary goal of this package is to collect the complex signaling pathway data and simplify in _gene × pathway/circuit_ format. This generated simple representation of the prior biological knowledge is a key component for **SigPrimedNet [1]** design which empowers the explainability of the network biologically. The information is derived from the **HiPathia [2]** package and exports the details each individual genes and correcponding pathway/circuit pairs.

### References

[1] Gundogdu, P., Alamo, I., Nepomuceno-Chamorro, I. A., Dopazo, J., & Loucera, C. (2023). SigPrimedNet: A Signaling-Informed Neural Network for scRNA-seq Annotation of Known and Unknown Cell Types. Biology, 12(4), 579. [https://doi.org/10.3390/biology12040579](https://doi.org/10.3390/biology12040579)


[2] Hidalgo, M. R., Cubuk, C., Amadoz, A., Salavert, F., Carbonell-Caballero, J., & Dopazo, J. (2017). High throughput estimation of functional cell activities reveals disease mechanisms and predicts relevant clinical outcomes. *Oncotarget*, 8(3), 5160–5178. [https://doi.org/10.18632/oncotarget.14107](https://doi.org/10.18632/oncotarget.14107)

## Output

The function returns a `pandas.DataFrame` where:
- **Rows**: Individual genes
- **Columns**: Represent specific pathways or circuits.
- **Values**: A binary indicator. If a gene is part of that pathway/circuit the value is 1, otherwise it is 0.

## Contributing

The open access **sigpathmatrix** package is shared in [GitHub](https://github.com/pelingundogdu/sigpathmatrix/).

## License

GPL-3.0 *(for detail, please see LICENSE)*

***

# USAGE
The main function name is ```default_pbk_hipathia``` which calls the corresponding functions to collect and export signaling pathways/circuits details for the given organims. The main function requires 3 parameters which are called ```-sp or --species``` for organism detail and the other two are for disease-associated keywords and list, ```-dk or --disease_keyword```  and ```-dl or --disease_list```, respectively.

<!-- ```
python -m sigpathmatrix.default_pbk_hipathia --species [OGRANISM]
``` -->

```
-sp SPECIES, --species SPECIES
            organism detail, such as hsa for homo sapiens, mmu for mus musculus, etc.
-dk DISEASE_KEYWORD, --disease_keyword DISEASE_KEYWORD
            a list of string that contains a disease description, removes disease-related
            pathway if there is a partially matching
-dl DISEASE_LIST, --disease_list DISEASE_LIST
            a list of string that contains the disease name, removes disease-related
            pathway if there is an exact match
```

</br>

> ❗❗ IMPORTANT INFORMATION
>
> The working directory in terminal should be the parent path of the user's project folder while the execution is in process.
> 
> In addition, during the execution, the package is modify ```PATH``` information of ```PYTHON``` and ```R``` to be able to complete the data collection and exportation successfully. The updates are written into the ```.env ``` file which also should be located in parent path of the user's project folder. _(please see the [`folder structure tree`](#folder-structure-after-execution-completed) for more detail)_
> 
> </br>
> 
> Updated ```.env``` file will have additional 2 lines as followed,
> 
>  ```
> ...
> SPN_PYTHON_PATH='[PATH_of_PYTHON_ENVIRONMENT]/bin/> python'
> R_HOME='[PATH_of_PYTHON_ENVIRONMENT]/lib/R'
> ```
> 
> _Note, the ```PYTHON``` path for the project is defined as ```SPN_PYTHON_PATH``` to not to overwrite the user's setting in case user is already defined theirs. The package is using this defined ```PYTHON``` path as selected environment._

> _This package is executable via command line in terminal. Please see the [USAGE_EXAMPLE.md](https://github.com/pelingundogdu/sigpathmatrix/blob/main/USAGE_EXAMPLE.md) file for more details._

<!-- This package collects and exports the signaling pathway/circuit details into ```data_spn_helper``` folder which is generated by package during execution.


The package comes with a set of built‑in default definitions that are specifically tailored for use with ```sigPrimedNet```. By design, it supports data collection for two reference organisms - ```homo sapiens (hsa)``` and ```mus musculus (mmu)``` - while automatically excluding all disease‑associated pathways from the retrieved lists.

The user can defined theirs tailored experiment by redefininig the organim name and changing the list of the disease‑associated pathways. 
 -->
</br>

The package comes with a set of built‑in default definitions that are specifically tailored for ```sigPrimedNet```. By design, it supports a data collection for two reference organisms - ```homo sapiens (hsa)``` and ```mus musculus (mmu)``` - while automatically excluding all disease‑associated pathways. By design, the main function only needs a species detail which can be declared in variable ```-sp or --species``` if the user desires to use [embedded disease-associated lists](#disease-associated-pathway-elimination).

📌 📌 The user can define theirs tailored experiment by redefininig the organim name and lists of the disease‑associated keyword in ```.env``` file. Please see the [USAGE_EXAMPLE.md](https://github.com/pelingundogdu/sigpathmatrix/blob/main/USAGE_EXAMPLE.md) for more detail explanation.

</br>

## Parameter details 

Please check for more details about parameter definition and structure, 
+ [`Organism Selection`](#organism-selection)
+ [`Disease-associated Pathway Elimination`](#disease-associated-pathway-elimination)
+ [`An overview for updated ```.env``` file with customize lists`](#an-overview-for-updated-env-file-with-customize-lists)

</br>

### Organism Selection


The package has an embedded dictionary for two organism _(```homo sapiens (hsa)``` and ```mus musclus (mmu)```)_ which are using in **sigPrimedNet** analysis.

```
GA_DICT = {'hsa':'org.Hs.eg.db', 'mmu':'org.Mm.eg.db'}
```

> _Note, if the user wants to use different organism rather than ```hsa``` and ```mmu```, the information should be added into ```.env``` file into ```GA_DICT_CUSTOM``` dictionary with a key and proper ```genome wide annotation``` detail. One crucial detail in this step is that the ```genome wide annotation``` naming should has same as defined in [`Bioconductor AnnotationData Package`](https://bioconductor.org/packages/3.23/data/annotation)._
> ```
> GA_DICT_CUSTOM = {'[KEY1]':'[GENOME_WIDE_ANNOTATION1]', '[KEY2]':'[GENOME_WIDE_ANNOTATION2]'}
> ```

</br>

### Disease-associated Pathway Elimination

The user can define own custom list. The details of the pre-defined disease-associated list in package as followed,

```
DISEASE_KEYWORD = ['disease', 'cancer', 'leukemia', 'infection', 'virus'
                   ,'addiction', 'anemia', 'cell carcinoma', 'diabet', 'Hepatitis']
DISEASE_LIST = ['Long-term depression', 'Insulin resistance', 'Measles'
                , 'Amyotrophic lateral sclerosis (ALS)', 'Alcoholism'
                , 'Shigellosis', 'Pertussis', 'Legionellosis', 'Leishmaniasis'
                , 'Toxoplasmosis', 'Tuberculosis', 'Influenza A', 'Glioma', 'Melanoma']
```


###  An overview for updated ```.env``` file with customize lists

The user can have own custom variable definition in ```.env``` file but at the end of the execution the the file will have,
+ Two environment definitions for both ```PYTHON``` and ```R```, which are called ```SPN_PYTHON_PATH```and ```R_HOME``` respectively,
+ customize species-genome wide annotation pair definition in ```GA_DICT_CUSTOM``` variable, abd
+ list using in elimination of disease-associated pathway with desired naming. _(In given example below, the naming for both lists for pathway naming and keyword are defined as ```CUSTOM_DISEASE_LIST``` and ```CUSTOM_DISEASE_KEYWORD```, respectively. )_

An example for ```.env```,

> ```
> ....
>      [USER'S VARIABLES IF THERE IS ANY]
> ....
> SPN_PYTHON_PATH='[PATH_of_ACTIVE_ENVIRONMENT]/bin/python'
> R_HOME='[PATH_of_ACTIVE_ENVIRONMENT]/lib/R'
> # DEFINITION of {[SPECIES] : [GENOME_WIDE_ANNOTATION]} PAIRS
> GA_DICT_CUSTOM={'rno':'org.Rn.eg.db'}
> # DISEASE-ASSOCIATED PATHWAY ELIMINITATION
> CUSTOM_DISEASE_LIST='["Long-term depression","Insulin resistance","Measles","Amyotrophic lateral sclerosis (ALS)","Alcoholism","Shigellosis","Pertussis","Legionellosis","Leishmaniasis","Toxoplasmosis","Tuberculosis","Influenza A","Glioma","Melanoma"]'
> CUSTOM_DISEASE_KEYWORD='["disease","cancer","leukemia","infection","virus","addiction","anemia","cell carcinoma","diabet","Hepatitis"]'
> # AN EMPTY LIST DEFINITION
> # ALTERATIVE #1
> CUSTOM_DISEASE_LIST_EMPTY="[]"
> CUSTOM_DISEASE_KEYWORD_EMPTY="[]"
> # ALTERATIVE #2
> CUSTOM_DISEASE_LIST_EMPTY2=""
> CUSTOM_DISEASE_KEYWORD_EMPTY2=""
> ```



## FOLDER STRUCTURE (after execution completed)

```USER'S PROJECT FOLDER [.]``` structure after execution completed, _(for ```hsa``` organism),_

```diff
.
├── ....
+├── data_spn_helper
+│   ├── processed
+│   │   └── hsa
+│   │       ├── entrez_and_symbol.csv
+│   │       ├── hipathia_details
+│   │       │   ├── hsa03320_gene_list.txt
+│   │       │   ├── ....... [GENE LIST for EACH 
+│   │       │               INDIVIDUAL PATHWAY]
+│   │       │   └── hsa05100_gene_list.txt
+│   │       ├── hipathia_gene_list.csv
+│   │       ├── hipathia_pathway_ids_and_names.csv
+│   │       ├── hsc_pbk_hsa.txt
+│   │       └── hsp_pbk_hsa.txt
+│   └── raw
+│       └── hsa
+│           ├── hipathia_gene_list_all.csv
+│           └── hipathia_pathway_ids_and_names.csv
+├── .env
├── ....
└── ....
```
