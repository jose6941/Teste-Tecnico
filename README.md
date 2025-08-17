<div>
    <h1 align="center">
        Teste técnico estágio Instar
    </h1>
    <p>
        Este repositório contém três partes do teste técnico: 

        Raciocínio Lógico em Python, que consiste em realizar uma série de tratamentos nos dados, para garantir que os dados estejam formatados corretamente e prontos para uso em um sistema.

        Consultas em Banco de Dados SQL, para a criação de consultas entre tabelas de clientes e pedidos. Obtendo todos os clientes que realizaram pedidos acima de R$ 100, ordenados pelo nome e o total de pedidos realizados por cada cliente.

        Extração de Dados com Scrapy, consiste em implementar um projeto que extraia as informações da página books.toscrape utilizando a biblioteca Scrapy do Python, tudo isso em um ambiente virtual.
    </p>
</div>

## Raciocínio lógico em Python

Este código realiza uma série de tratamentos nos dados, para garantir que os dados estejam formatados corretamente e prontos para uso em um sistema, com os seguintes passos: 

- [Remoção de Espaçamentos e Erros de NBSP]
- [Conversão de Data]
- [Substituição de Marcadores]
- [Transformação de Lista em String]
- [Exclusão de chaves com valores nulos]

## Lógica do script

1. **Leitura do arquivo JSON**
Abre o arquivo original (`teste_estagio_instar.json`) e carrega os dados em memória usando `json.load()`.

```bash

    # Abre o arquivo json no modo leitura
    with open(file_path, "r", encoding="utf-8") as f:

        # Guarda o arquivo em uma variável
        arquivo = json.load(f)
```
2. **Limpeza de campos de texto**
Remove caracteres especiais como `\xa0` e espaços extras usando a função `strip()` dos campos `nome`, `sobrenome` e `titulo`.  

```bash

    # Analise cada chave para remover o caracter especial
    for chave in ["nome", "sobrenome", "titulo"]:
        if chave in item and item[chave]:

            # Substitui o caracter especial por espaço e depois remove esse espaço, deixando-o formatado
            item[chave] = item[chave].replace("\xa0", " ").strip()
```

3. **Padronização de datas**
Utiliza a função `converter_data()` para tenta converter datas no formato `"dd/mm/yyyy HH:MM:SS"`, se caso for o formato sem o horário, converte no formato `"dd/mm/yyyy"`. Assim ele retorna a data no padrão `"YYYY-MM-DD HH:MM:SS"`. Escolhi fazer uma função para conversão de datas para facilitar a conversão dos dois tipos que foram pedidos, o dataRealizacao e a data dentro dos arquivos.

```bash
    def converter_data(data): 
        try: 

            # Tenta converter primeiro a string da data que está no formato ("%d/%m/%Y %H:%M:%S")
            data_original = datetime.strptime(data, "%d/%m/%Y %H:%M:%S") 
        except ValueError: 

            # Caso não seja o primeiro formato, a string será convertida no formato ("%d/%m/%Y")
            data_original = datetime.strptime(data, "%d/%m/%Y") 

        # Retorno a data já convertida em string, se caso não tiver o horário, sera colocado como 00:00:00
        return data_original.strftime("%Y-%m-%d %H:%M:%S")

    # Convertendo dataRealizacao
    if "dataRealizacao" in item:
        data_original = item["dataRealizacao"] 
        item["dataRealizacao"] = converter_data(item["dataRealizacao"])

    # Convertendo data para cada objeto dos arquivos
    for arq in item["arquivos"]: 
        arq["data"] = converter_data(arq["data"])
       
```



4. **Formatação de títulos**
Se o campo `titulo` contiver "...", substitui pela data e hora correspondente ao item, no formato `"dd/mm/yyyy às HH:MM:SS"`, que foi guardado na variável data_original.

```bash

    # Verfica se a chave titulo está contido no arquivo e se há "..." na string
    if "titulo" in item and "..." in item["titulo"]:

        # Converte a data original da dataRealizacao para o formato ("%d/%m/%Y %H:%M:%S")
        dt = datetime.strptime(data_original, "%d/%m/%Y %H:%M:%S")

        # Seapra a data original em dois formatos, data e hora
        data_fmt = dt.strftime("%d/%m/%Y")
        hora_fmt = dt.strftime("%H:%M:%S")

        # Substitui o "..." pelos formatos da data original, data e hora
        item["titulo"] = item["titulo"].replace("...", f"{data_fmt} às {hora_fmt}")
```

5. **Remoção de valores nulos**
Remove chaves com valor "None" ,Para o objeto "arquivos",percebi que na saída desejada os valores nulos não foram excluídos, logo os valores nulos foram substituídos por strings vazias, como estava no arquivo de saída.

```bash

    # Para cada chave do arquivo json que tiver campo nulo, sera armazenado em um vetor para depois serem deletadas
    chaves_remover = [chave for chave, valor in item.items() if valor is None] 
    for chave in chaves_remover: 

        # Deleta as chaves nulas que foram encontradas no arquivo json
        del item[chave] 

        # Verifica todos os valores das chaves do objeto "arquivos"
        for arq in item["arquivos"]: 

            # Armazena os valores nulos em um vetor
            chaves_remover = [chave for chave, valor in arq.items() if valor is None] 

            for chave in chaves_remover: 
                # Substitui os valores nulos por string vazia
                arq[chave] = ""
```

6. **Concatenação de listas**
Se o campo `descricao` for uma lista, converte para uma única string separada por espaços.

```bash

    # Verifica se o valor da chave "descricao" é uma lista
    if isinstance(item.get("descricao"), list):

        # Junta todos os valores da lista em uma única string separado por espaço
        item["descricao"] = " ".join(item["descricao"])
    
    # Armazena apenas as chaves que não forem nulas
    item_limpo = {chave: valor for chave, valor in item.items() if valor is not None}
    arquivo[arquivo.index(item)] = item_limpo
```

7. **Criação do arquivo final**
Salva os dados tratados em "teste_estagio_instar_tratado.json" usando json.dump() com indentação e codificação UTF-8.

```bash

    # Arquivo de saída
    output_path = "teste_estagio_instar_tratado.json"

    # Abre o arquivo de saída como escrita
    with open(output_path, "w", encoding="utf-8") as f:

        # Grava o arquivo no formato json no arquivo de saída
        json.dump(arquivo, f, indent=4, ensure_ascii=False)
```
