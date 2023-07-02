import subprocess

# Instala as dependências usando o pip
subprocess.call(["pip", "install", "-r", "requirements.txt"])

print("As dependências foram instaladas com sucesso.")
