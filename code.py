import apkutils
from lxml import etree
import os

def insert_code_into_apk(apk_path):
    # Solicita que o usuário insira o código
    print("Insira o código que deseja adicionar ao APK:")
    code = input()

    # Carrega o arquivo APK
    a = apkutils.APK(apk_path)

    # Cria um novo arquivo .dex com o código fornecido
    dex_file = a.dex.create_dex_file(code)

    # Adiciona o novo arquivo .dex ao APK
    a.dex.add_dex(dex_file)

    # Gera o novo arquivo APK de saída
    output_apk = "output.apk"
    a.save(output_apk)

    print("Arquivo APK de saída gerado:", output_apk)

def generate_manifest():
    # Cria um objeto APK
    a = apkutils.APK()

    # Solicita ao usuário para inserir as informações do pacote
    package_name = input("Insira o nome do pacote (ex: com.example.myapp): ")
    version_name = input("Insira a versão do aplicativo (ex: 1.0): ")
    version_code = input("Insira o código da versão (ex: 1): ")

    # Define as informações do pacote
    a.set_package_name(package_name)
    a.set_version_name(version_name)
    a.set_version_code(version_code)

    # Define as permissões necessárias
    a.add_uses_permission("android.permission.INTERNET")
    a.add_uses_permission("android.permission.ACCESS_WIFI_STATE")
    a.add_uses_permission("android.permission.CHANGE_WIFI_STATE")

    # Gera o arquivo AndroidManifest.xml
    a.save_manifest("AndroidManifest.xml")

    print("Arquivo AndroidManifest.xml gerado com sucesso.")

def update_manifest(apk_path):
    # Carrega o arquivo APK
    a = apkutils.APK(apk_path)

    # Carrega o arquivo AndroidManifest.xml
    manifest_path = "AndroidManifest.xml"
    tree = etree.parse(manifest_path)

    # Obtém o elemento raiz do arquivo manifest
    root = tree.getroot()

    # Obtém a tag <manifest>
    manifest_tag = root.find("manifest")

    # Obtém a tag <application>
    application_tag = manifest_tag.find("application")

    # Obtém todas as bibliotecas usadas no APK
    libraries = a.get_libraries()

    # Percorre todas as bibliotecas e adiciona automaticamente no manifest
    for library in libraries:
        uses_library_tag = etree.Element("uses-library")
        uses_library_tag.attrib["name"] = library
        application_tag.append(uses_library_tag)

    # Salva as alterações no arquivo AndroidManifest.xml
    tree.write(manifest_path, encoding="utf-8", pretty_print=True)

    print("Arquivo AndroidManifest.xml atualizado com sucesso.")

def build_apk():
    # Executa o comando para construir o APK usando o apktool
    os.system("apktool b . -o output.apk")

    print("Arquivo APK de saída gerado: output.apk")

# Caminho do arquivo APK de entrada
apk_path = "input.apk"

# Gera o arquivo AndroidManifest.xml
generate_manifest()

# Atualiza o arquivo AndroidManifest.xml com bibliotecas ausentes
update_manifest(apk_path)

# Chama a função para inserir o código no APK
insert_code_into_apk(apk_path)

# Gera o APK final
build_apk()
