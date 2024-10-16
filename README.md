# Examen DVC et Dagshub
Dans ce dépôt vous trouverez l'architecture proposé pour mettre en place la solution de l'examen. 

```bash       
├── examen_dvc          
│   ├── data       
│   │   ├── processed      
│   │   └── raw       
│   ├── metrics       
│   ├── models      
│   │   ├── data      
│   │   └── models        
│   ├── src  
│   │   ├── data_module_def      
│   │   └── models_module_def
│   │   └── pipeline_steps
|   ├── config*
|   ├── logs  
│   └── README.md.py       
```


## DVC
dvc init    
dvc remote add -d remote_storage data  


# Pipeline

### Data Ingestion
dvc stage add -f -n data_ingestion \
-d https://datascientest-mlops.s3.eu-west-1.amazonaws.com/mlops_dvc_fr/raw.csv \
-o data/raw/raw.csv \
python3 src/pipeline_steps/stage00_data_ingestion.py

### Data Preparation
dvc stage add -f -n data_preparation \
-d data/raw/raw.csv \
-o data/processed/X_train.csv \
-o data/processed/y_train.csv \
-o data/processed/X_test.csv \
-o data/processed/y_test.csv \
python3 src/pipeline_steps/stage01_data_preparation.py

### Data Transformation
dvc stage add -f -n data_transformation \
-d data/processed/X_train.csv \
-d data/processed/X_test.csv \
-o data/processed/X_train_scaled.csv \
-o data/processed/X_test_scaled.csv \
python3 src/pipeline_steps/stage02_data_transformation.py

### Grid Search
dvc stage add -f -n grid_search \
-d data/processed/X_train_scaled.csv \
-d data/processed/X_test_scaled.csv \
-d data/processed/y_train.csv \
-d data/processed/y_test.csv \
-o models/params.pkl \
python3 src/pipeline_steps/stage03_gridsearch.py

### Model Trainer
dvc stage add -f -n model_trainer \
-d data/processed/X_train_scaled.csv \
-d data/processed/X_test_scaled.csv \
-d data/processed/y_train.csv \
-d data/processed/y_test.csv \
-d models/params.pkl \
-o models/model.joblib \
python3 src/pipeline_steps/stage04_model_trainer.py

### Model Evaluation
dvc stage add -f -n model_evaluation \
-d data/processed/X_test_scaled.csv \
-d data/processed/y_test.csv \
-d models/model.joblib \
-o metrics/metrics.json \
python3 src/pipeline_steps/stage05_model_evaluation.py







