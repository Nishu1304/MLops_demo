import os
from pathlib import Path

list_of_files = [
    '.github/workflows/.gitkeep',
    'src/__init__.py',
    'src/components/__init__.py',
    'src/components/data_ingestion.py',
    'src/components/data_transformation.py',
    'src/components/model_trainer.py',
    'src/components/model_evaluation.py',
    'src/pipeline/__init__.py',
    'src/pipeline/training_pipeline.py',
    'src/pipeline/prediction_pipeline.py',
    'src/utils/__init__.py',
    'src/utils/utils.py',
    'src/logger/loggin.py',  # Typo in 'logging.py'
    'src/exception/exception.py',  # Missing file extension
    'test/unit/__init__.py',
    'test/integration/__init__.py',  # Typo in 'integration'
    'init_setup.sh',  # Typo in 'init_setup.sh'
    'requirements.txt',
    'requirements_dev.txt',  # Missing comma after 'requirements_dev.txt'
    'setup.py',
    'setup.cfg',
    'pyproject.toml',
    'tox.ini',
    'experiment/experiments.ipynb'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    # Check if the file doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        # Open the file with 'w' mode to write content to it
        with open(filepath, 'w') as f:
            # Write some content to the file (e.g., 'Hello, world!')
            f.write("Hello, world!")
