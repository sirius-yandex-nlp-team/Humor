import setuptools

setuptools.setup(
    name="humor",
    packages=setuptools.find_packages(),
    install_requires=[
        'pytorch-pretrained-bert==0.6.2',
        'tqdm==4.50.0',
        'boto3==1.12.31',
        'requests==2.25.1',
        'regex==2021.3.17',
        'pytorch-nlp==0.5.0',
        'sacremoses==0.0.43',
        'sentencepiece==0.1.95',
        'pytorch_transformers==1.2.0',
        'transformers==2.5.1',
        'gensim==3.8.1',
        'spacy==3.0.5',
        'python-box==5.3.0',
        'scikit-learn==0.22.1',
        'keras-preprocessing==1.1.2',
        'pandas==0.25.3',
        'click==7.1.2',
    ],
)
