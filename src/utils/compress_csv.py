# -*- coding: utf-8 -*-
"""
script robusto de otimização de csv.
lê o arquivo csv mais recente da pasta, corrige formatações e sobrescreve o original.
converte todas as colunas e textos para letras minúsculas.
exibe contagem de linhas e redução de tamanho (memória).
"""

import pandas as pd
import os
from pathlib import Path
import shutil

def compress_table(path_data):
    
    csv_files = list(path_data.glob("*.csv"))
    if not csv_files:
        print("nenhum arquivo csv encontrado na pasta.")
        return

    latest_file = max(csv_files, key=os.path.getmtime)
    original_size = os.path.getsize(latest_file) / (1024 * 1024)

    try:
        with open(latest_file, "r", encoding="utf-8", errors="ignore") as f:
            amostra = f.read(5000)
        sep = ";" if amostra.count(";") > amostra.count(",") else ","

        df = pd.read_csv(
            latest_file,
            sep=sep,
            encoding="utf-8",
            on_bad_lines="skip",
            engine="python"
        )

    except Exception as e:
        print(f"erro ao ler o csv: {e}")
        return

    df.dropna(axis=1, how='all', inplace=True)
    colunas_excluir = [c for c in df.columns if 'unnamed' in c.lower() or 'extra' in c.lower()]
    df.drop(columns=colunas_excluir, errors='ignore', inplace=True)

    for col in df.select_dtypes(include=['float64']).columns:
        df[col] = pd.to_numeric(df[col], downcast='float')
    for col in df.select_dtypes(include=['int64']).columns:
        df[col] = pd.to_numeric(df[col], downcast='integer')

    for col in df.select_dtypes(include=['object']).columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .str.lower()  
            .str.replace(r'\s+', ' ', regex=True)
            .str.replace(r'[^\x20-\x7e]+', '', regex=True)
        )

    df.columns = [col.lower().strip() for col in df.columns]

    df.drop_duplicates(inplace=True)

    temp_file = latest_file.with_name(f"temp_{latest_file.name}")
    df.to_csv(temp_file, index=False, encoding='utf-8', float_format='%.4g')
    shutil.move(temp_file, latest_file)

    new_size = os.path.getsize(latest_file) / (1024 * 1024)
    reducao = 100 - (new_size / original_size * 100)

    print("\nrelatório de otimização =>")
    print("-" * 35)
    print(f"linhas totais        : {len(df)}")
    print(f"tamanho original     : {original_size:.2f} mb")
    print(f"tamanho otimizado    : {new_size:.2f} mb")
    print(f"redução de tamanho   : {reducao:.1f}%")
    print("-" * 35)
