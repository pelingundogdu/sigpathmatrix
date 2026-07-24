#!/usr/bin/env Rscript

# DESCRIPTION
# -----------
#     Collecting and exporting the gene list from HiPathia package. There are two function in this script
#     which called 'gene_from_hipathia' and 'gene_id_entrez_converter'.
#       - 'gene_from_hipathia' function collect and modify the list of genes which are involved a pathway
#             The raw and disease-associated gene list is exporting into raw and processed folder 
#                 raw        ----  [PROJECT_FOLDER]/data_spn_helper/raw/{SPECIES}/hipathia_gene_list_all.csv
#                 processed  ----  [PROJECT_FOLDER]/data_spn_helper/processed/{SPECIES}/hipathia_gene_list.csv
#             as well as the circuit details for each individual pathways is exporting ( note, the detail
#             of the circuits is belong to the pathway list which is obtained after revoking
#             disease-associated pathways)
#                 details  ----  [PROJECT_FOLDER]/data_spn_helper/processed/{SPECIES}/hipathia_details/..._gene_list.txt
#       - 'gene_id_entrez_converter' function is a conversion script which collect the gene name details
#             of each entrez id. The collected gene information from HiPathia package is called as entrez id
#             and if the user needs the conversion this script enables to collect the gene name detail 
#             of each gene
#                 exported file ---- [PROJECT_FOLDER]/data_spn_helper/processed/{SPECIES}/entrez_and_symbol.csv
#
# USAGE 
# -----
#     To call gene_from_hipathia function,
#     Rscript .../r_collect_gene_entrezid.r -f hg
#                                           -sp [SPECIES_NAME] 
#                                           -raw [PATH_OF_RAW_FOLDER] 
#                                           -processed [PATH_OF_PROCESSED_FOLDER]
#
#     To call gene_id_entrez_converter function, 
#     Rscript .../r_collect_gene_entrezid.r -f ga
#                                           -sp [SPECIES_NAME] 
#                                           -processed [PATH_OF_PROCESSED_FOLDER]
#                                           -ga [GENOME_ANNOTATION]
#
# RETURN
# ------
#     gene_list_all.csv : csv file
#         The gene information of all pathways
#     gene_list.csv     : csv file
#         The gene information of pathway which removed disease related ones
#     {SPECIES}[PATHWAY_NUMBER]_gene_list.csv     : csv file
#         The gene information of each pathway which removed disease related ones

# EXPORTED FILE(s) LOCATION
# -------------------------
#     ./data_spn_helper/raw/{SPECIES}/hipathia_gene_list_all.csv
#     ./data_spn_helper/processed/{SPECIES}/hipathia_gene_list.csv
#     ./data_spn_helper/processed/{SPECIES}/hipathia_details/{SPECIES}[PATHWAY_NUMBER]_gene_list.csv
#     ./data_spn_helper/processed/{SPECIES}/entrez_and_symbol.csv

# Loading libraries

# if (!require("BiocManager", quietly = TRUE))
#     install.packages("BiocManager")

# BiocManager::install(version = "devel", ask = FALSE) # Ensures Bioconductor is fully updated
# BiocManager::install("hipathia", dependencies = TRUE)

suppressWarnings( suppressMessages({ 
    if (!require(dotenv)) install.packages("dotenv", repos = "http://cran.us.r-project.org")
    if (!require(argparse)) install.packages("argparse", repos = "http://cran.us.r-project.org")
    if (!require("BiocManager", quietly = TRUE)) install.packages("BiocManager")
    if (!require(stringr)) install.packages("stringr", repos = "http://cran.us.r-project.org")
    if (!require(logging)) install.packages("logging", repos = "http://cran.us.r-project.org")
    })
)

suppressWarnings( suppressMessages({
    library(package = 'stringr', quietly = TRUE)
    library(package = 'argparse', quietly = TRUE)
    library(package = 'dotenv', quietly = TRUE)
    library(package = 'hipathia', quietly = TRUE)
    # BiocManager::install("hipathia", dependencies = TRUE, quietly = TRUE)
    library(package = 'reticulate', quietly = TRUE)
    library(package = 'logging', quietly = TRUE)
    })
)

suppressWarnings({
    dotenv::load_dot_env(".env")
    # Loading project specific folder detail
    project_specific_python_path <- Sys.getenv("SPN_PYTHON_PATH")

    if (project_specific_python_path != "") {
        reticulate::use_python(project_specific_python_path, required = TRUE)
    } else { stop("SPN_PYTHON_PATH not configured in .env") }
})

basicConfig()
removeHandler(writeToConsole)  # Remove default
logReset()
addHandler(writeToConsole, formatter = function(r) paste(r$levelname, ":sigpathmatrix.hipathia.r_collect_gene_entrezid: ", r$msg, sep = ""), level = "INFO")

# options(warn = -1) # turn off warning
# options(warn = 0) # turn back on warnings
gene_from_hipathia <- function(species, raw, processed){
    loginfo(paste0('          hipathia pathways are exporting for ', species))

    # The path location for output folder
    output_folder_detail = file.path(processed, 'hipathia_details')
    path_out_raw = file.path(raw, 'hipathia_gene_list_all.csv')
    path_out_processed = file.path(processed, 'hipathia_gene_list.csv')
    loginfo(paste0('          raw        ----  ', path_out_raw))
    loginfo(paste0('          processed  ----  ', path_out_processed))
    loginfo(paste0('          details    ----  ', output_folder_detail))

    # importing pathway information file
    dataset_hp <- read.table(file.path(processed, 'hipathia_pathway_ids_and_names.csv'), sep=',', header=TRUE, quote="\"")
    # print('****************************************************************')
    pathways <- load_pathways(species = species)
    # df_pathways = data.frame(pathways$all.labelids)
    c_effector_gene_subpath = rownames(data.frame(pathways$eff.norm))
    c_effector_gene_path = str_split(c_effector_gene_subpath, "-", simplify = TRUE)[, 2]
    df_effector_gene_detail = data.frame(cbind(c_effector_gene_subpath,c_effector_gene_path))
    colnames(df_effector_gene_detail) <- c('gene.effector.path', 'path.id')
    # df_effector_subgraph = data.frame(pathways$eff.norm)
    # print('****************************************************************')
    # Loaded 146 pathways
    loginfo(' ')
    loginfo('          DETAILS of COLLECTED SIGNALING PATHWAYS')
    loginfo(paste0('          Number of pathway                       , ', length(unique(df_effector_gene_detail$path.id)) ))
    # print(paste0('Number of sub-pathways (effector nodes) , ', nrow(df_pathways)))
    loginfo(paste0('          Number of sub-pathways (effector genes) , ', nrow(df_effector_gene_detail)))
    
    # [1] "SIGNALING PATHWAYS (all)"
    # [1] "Number of pathway                       , 146"
    ###### [1] "Number of sub-pathways (effector nodes) , 6826"
    # [1] "Number of sub-pathways (effector genes) , 1876"

    loginfo(' ')
    loginfo('          DETEAILS of CLEANED SIGNALING PATHWAYS (eliminated disease-associated)')
    # df_pathways = merge(dataset_hp, df_pathways)
    df_effector_gene_detail = merge(dataset_hp, df_effector_gene_detail)
    loginfo(paste0('          Number of pathway                       , ', nrow(dataset_hp)))
    # print(paste0('Number of sub-pathways (effector nodes) , ', nrow(df_pathways)))
    loginfo(paste0('          Number of sub-pathways (effector genes) , ', nrow(df_effector_gene_detail)))
    list_path_id = unique(df_effector_gene_detail$path.id)
    # [1] "SIGNALING PATHWAYS WITHOUT CANCER/DISEASE"
    # [1] "Number of pathway                       , 93"
    ##### [1] "Number of sub-pathways (effector nodes) , 4502"
    # [1] "Number of sub-pathways (effector genes) , 1211"

    # Creating empty data frame to store genes
    df_gene <- data.frame(pathways$all.genes)
    # updating column name as 'entrez'
    colnames(df_gene) = c('entrez')
    l_gene_final<-c()

    for (all_pathways_ in c(1:length(list_path_id))) {
    # for (all_pathways_ in c(1:2)) {
        df_merge = df_gene
        l_main<-c()
    #     number of sub-pathway in 
        length_subpathways = length(pathways$pathigraphs[[list_path_id[all_pathways_]]]$effector.subgraphs)
    #     details for sub-pathway
        for (sub_pathways_ in c(1:length_subpathways)) {
            l_sub<-c()
            genes_circuits = V(pathways$pathigraphs[[list_path_id[all_pathways_]]]$effector.subgraphs[[sub_pathways_]])$genesList
            sub_path_name = names(pathways$pathigraphs[[list_path_id[all_pathways_]]]$effector.subgraphs[sub_pathways_][1])
    #         name of sub-patway
    #         print(sub_path_name)
            for (sub_circuits in c(1:length(genes_circuits))){
                for (genes_ in c(1:length(genes_circuits[sub_circuits][1][[1]]))){
                    gene_value = genes_circuits[sub_circuits][1][[1]][genes_]
                    if (!is.na(gene_value) && gene_value != '/' && (gene_value == 'NA') == FALSE){
                        l_sub <-append(l_sub,gene_value)
                    }
                }
                l_sub = unique(l_sub)
            }
    #             Combining genes obtaining from sub-pathways
            if (length(l_sub) != 0) {
                l_main<-append(l_main, l_sub)
                df_temp <- data.frame(l_sub, 1)
                names(df_temp) = c('entrez', sub_path_name)
    #             print(df_temp)
            }
    #         Inner join
            df_merge = merge(df_temp,df_merge, by='entrez', all=T)
        }
        l_main = unique(l_main)
    #     Assigning all NA's as 0
        df_merge[!is.na(df_merge)] 
        indices_genes <- as.vector(which(df_merge$entrez %in% l_main, arr.ind = TRUE))
        df_path_genes <- (df_merge[c(indices_genes), ])
        rownames(df_path_genes) <- 1:nrow(df_path_genes)
        l_gene_final = append(l_gene_final, l_main)
    #     Exporting gene set of each pathways (93 txt file for using pathways for hsa)
        write.table(df_path_genes , file.path(output_folder_detail, paste0(list_path_id[all_pathways_], '_gene_list.txt')), sep=',', row.names=FALSE)
    }
    write.table(df_gene$entrez[(df_gene$entrez) != 'NA'], path_out_raw, sep=',', row.names = FALSE)
    write.table(unique(l_gene_final), path_out_processed, sep=',', row.names = FALSE)

    return_gene_list_all = df_gene$entrez[(df_gene$entrez) != 'NA']
    retrun_gene_list_processed = unique(l_gene_final)
}

gene_id_entrez_converter <- function(species, genome_annotation, processed){
    suppressMessages({BiocManager::install(genome_annotation, quiet = TRUE)})
    suppressPackageStartupMessages(library(genome_annotation, character.only = TRUE, quietly = TRUE)) # genome wide annotation
    suppressPackageStartupMessages(library('AnnotationDbi', quietly = TRUE))  # the gene name conversion

    # entrez and symbol informatinon
    entrez_keys <- keys(eval(parse(text = genome_annotation)), keytype="ENTREZID")
    # entrez_name_pair <- select(org.Hs.eg.db, keys=mmu_entrez, columns=c("ENTREZID","SYMBOL"), keytype="ENTREZID")

    entrez_symbol_pair <- select(eval(parse(text = genome_annotation)), keys=entrez_keys, columns=c("ENTREZID","SYMBOL"), keytype="ENTREZID")
    colnames(entrez_symbol_pair) = c('gene_id', 'symbol')

    ## pathway genes list
    df_h <- read.table(file.path(processed, 'hipathia_gene_list.csv'), quote='\"', comment.char='')
    colnames(df_h) = c('gene_id')
    # print(paste0('gene list head 5 - ', head(df_h)))

    df_h_es = merge(df_h, entrez_symbol_pair, by='gene_id', all.x='True')
    df_h_es <- df_h_es[which(is.na(df_h_es$symbol) == FALSE ), ]

    write.table(df_h_es, file.path(processed,'entrez_and_symbol.csv'), sep=',', row.names = FALSE)

    loginfo(paste0('          The number of gene in entrez_and_symbol_list, ', nrow(df_h_es) ))
    loginfo(paste0('          File exported!! - ', processed,'/entrez_and_symbol.csv'))
}

main <- function() {
    
    parser <- ArgumentParser()
    args <- commandArgs(trailingOnly = TRUE)
    parser$add_argument('-f', '--func', choices=c('hg', 'ga'), help='Function to execute: hg for gene_from_hipathia, ga for gene_id_entrez_converter')
    # required=True, type=str,
    parser$add_argument('-sp', '--species', help='specify the species, the location of species in ./data_spn_helper/raw/{SPECIES}')
    parser$add_argument('-raw', '--raw', help='specify the raw folder, the location of source in ./data_spn_helper/raw/{SPECIES}/{SOURCE}')
    parser$add_argument('-processed', '--processed', help='specify the processed folder, the location of source in ./data_spn_helper/processed/{SPECIES}/{SOURCE}')
    # nargs='?', type=str, default=None,
    parser$add_argument('-ga', '--genome_annotation', help='specify genome wide annotition package')
    
    args <- parser$parse_args()
    # Add function selection argument
    # parser$add_argument('-f', '--function', choices=c('hg', 'ga'), help='Function to execute: hg for gene_from_hipathia, ga for gene_id_entrez_converter')

    if(length(args)==0){
        parser$print_help()
        print("ERROR!! Please give species information.")
        quit(status=1)
    }
    
    if(args$func == 'hg'){
        suppressWarnings( 
            suppressMessages (
                gene_from_hipathia(args$species, args$raw, args$processed)
            )
        )
    } else if(args$func == 'ga'){
        if (is.null(args$genome_annotation) || is.na(args$genome_annotation)) {
            cat("Error: Parameter GA is required for gene_id_entrez_converter function\n", file = stderr())
            cat("Please enter define a valid genome annotation for selected species !!\n", file = stderr())
            quit(status = 1)
        }
        suppressWarnings(
            suppressMessages (
                gene_id_entrez_converter( args$species, args$genome_annotation, args$processed )
            )
        )
        
    } else {
        cat(sprintf("Error: Unknown function '%s'\n", args$func), file = stderr())
        quit(status = 1)
    }
}

if (getOption('run.main', default=TRUE)) {
    suppressWarnings( suppressMessages( main() ) )
}