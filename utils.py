import json
from typing import Any


def salvar_json(arquivo: str, dados: Any) -> None:
    """Salva os dados em um arquivo JSON."""
    with open(arquivo, "w", encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def carregar_json(arquivo: str) -> Any:
    """Carrega os dados de um arquivo JSON (ou retorna [] se não existir ou estiver vazio)."""
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []