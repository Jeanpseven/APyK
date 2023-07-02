# Script de Injeção de Código Python para fazer APK

Este script em Python permite que você insira código personalizado em um arquivo APK, atualize o arquivo `AndroidManifest.xml` com as bibliotecas ausentes e gere um novo APK final.

## Requisitos

- Python 3.x
- apkutils
- lxml

## Instalação

1. Certifique-se de ter o Python instalado em seu sistema. Você pode fazer o download do Python em [python.org](https://www.python.org/downloads/).

2. Clone ou baixe este repositório para o seu ambiente local.

3. No diretório do projeto, execute o seguinte comando para instalar as dependências necessárias:


## Uso

1. No diretório do projeto, execute o seguinte comando para gerar o arquivo `AndroidManifest.xml`:


2. Insira as informações solicitadas, como nome do pacote, versão do aplicativo e código da versão.

3. Após gerar o `AndroidManifest.xml`, execute o seguinte comando para atualizar o arquivo com as bibliotecas ausentes:


Certifique-se de substituir `<caminho_do_apk>` pelo caminho completo do arquivo APK.

4. Em seguida, insira o código personalizado que deseja adicionar ao APK:


Mais uma vez, substitua `<caminho_do_apk>` pelo caminho completo do arquivo APK.

5. Por fim, execute o seguinte comando para gerar o APK final:


O APK final será gerado com o nome `output.apk`.





