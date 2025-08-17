import json
from datetime import datetime

file_path = "teste_estagio_instar.json"

def converter_data(data): 
    try: 
        data_original = datetime.strptime(data, "%d/%m/%Y %H:%M:%S") 
    except ValueError: 
        data_original = datetime.strptime(data, "%d/%m/%Y") 
    return data_original.strftime("%Y-%m-%d %H:%M:%S")

with open(file_path, "r", encoding="utf-8") as f:
    arquivo = json.load(f)

for item in arquivo:

    for chave in ["nome", "sobrenome", "titulo"]:
        if chave in item and item[chave]:
            item[chave] = item[chave].replace("\xa0", " ").strip()
    
    if "dataRealizacao" in item:
        data_original = item["dataRealizacao"] 
        item["dataRealizacao"] = converter_data(item["dataRealizacao"])
        

    if "titulo" in item and "..." in item["titulo"]:
        dt = datetime.strptime(data_original, "%d/%m/%Y %H:%M:%S")
        data_fmt = dt.strftime("%d/%m/%Y")
        hora_fmt = dt.strftime("%H:%M:%S")
        item["titulo"] = item["titulo"].replace("...", f"{data_fmt} às {hora_fmt}")
    
    chaves_remover = [chave for chave, valor in item.items() if valor is None] 
    for chave in chaves_remover: 
        del item[chave] 

        for arq in item["arquivos"]: 
            chaves_remover = [chave for chave, valor in arq.items() if valor is None] 

            for chave in chaves_remover: 
                arq[chave] = ""
    

    if isinstance(item.get("descricao"), list):
        item["descricao"] = " ".join(item["descricao"])
    
    item_limpo = {k: v for k, v in item.items() if v is not None}
    arquivo[arquivo.index(item)] = item_limpo

output_path = "teste_estagio_instar_tratado.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(arquivo, f, indent=4, ensure_ascii=False)

print("Arquivo tratado salvo em:", output_path)