import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime, timedelta
import zoneinfo
import shutil
import sys

load_dotenv()

path_download = Path(os.getenv("PATH_DOWNLOAD"))
path_data = Path(os.getenv("PATH_DATA"))

TZ = zoneinfo.ZoneInfo("America/Sao_Paulo")
MAX_MINUTES = 3 

def now_local():
    return datetime.now(TZ)

def file_mtime_local(path: Path) -> datetime:
    ts = path.stat().st_mtime
    return datetime.fromtimestamp(ts, TZ)

def safe_filename(s: str) -> str:
    return "".join(ch for ch in s if ch.isalnum() or ch in "._-")

def manipulacao_path():
    global path_download, path_data

    for var_name, var_value in {"PATH_DOWNLOAD": path_download, "PATH_DATA": path_data}.items():
        if not var_value:
            print(f"Variável {var_name} ausente no .env")
            sys.exit(1)

    path_download, path_data = map(Path, (path_download, path_data))

    for p, msg in [(path_download, "Pasta de downloads não encontrada"),
                   (path_data, "Pasta de dados criada (caso não exista)")]:
        if not p.exists():
            if p == path_download:
                print(f"{msg}: {p}")
                sys.exit(1)
            else:
                p.mkdir(parents=True, exist_ok=True)
                print(msg)

    now = now_local()
    today_str = now.strftime("%Y-%m-%d")
    pattern = f"programacao--{today_str}*"
    candidates = list(path_download.glob(pattern))

    if not candidates:
        print(f"Nenhum arquivo encontrado com o padrão '{pattern}' em {path_download}")
        return None

    candidates.sort(key=lambda f: file_mtime_local(f), reverse=True)
    chosen_file = candidates[0]
    age = now - file_mtime_local(chosen_file)

    if age > timedelta(minutes=MAX_MINUTES):
        print(f"O arquivo '{chosen_file.name}' é antigo ({age.total_seconds()/60:.1f} minutos). Ignorado.")
        return None

    latest_overall = max((p for p in path_download.iterdir() if p.is_file()),
                         key=lambda p: p.stat().st_mtime)
    if latest_overall.resolve() != chosen_file.resolve():
        print("O arquivo encontrado não é o último modificado da pasta.")
        return None

    ext = chosen_file.suffix
    timestamp = now.strftime("%Y-%m-%d_%H%M%S")
    new_name = safe_filename(f"table_{timestamp}{ext}")
    dest_path = path_data / new_name

    try:
        shutil.move(str(chosen_file), str(dest_path))
        print(f"Sucesso: '{chosen_file.name}' movido para '{dest_path}'")
        return dest_path
    except Exception as e:
        print(f"Erro ao mover o arquivo: {e}")
        return None

def remove_files(): 
    """
    Mantém apenas o último arquivo adicionado/modificado em uma pasta,
    removendo os demais.
    """
    
    arquivos = [f for f in path_data.iterdir() if f.is_file()]

    if not arquivos:
        print("Nenhum arquivo encontrado na pasta.")
        exit()

    ultimo_arquivo = max(arquivos, key=lambda f: f.stat().st_mtime)

    for arquivo in arquivos:
        if arquivo != ultimo_arquivo:
            try:
                os.remove(arquivo)
            except Exception as e:
                print(f"Erro ao remover {arquivo.name}: {e}")
