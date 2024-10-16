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



