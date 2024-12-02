import os, sys
import subprocess

def get_base_path():
    return os.path.dirname(os.path.abspath(sys.argv[0]))

def rodar_git():
    mensagem = input("Digite a mensagem do commit: ")

    try:
        git_add = 'git add .'
        git_commit = f'git commit -m {mensagem}'
        git_push = 'git push'

        subprocess.run(git_add, shell=True, check=True)
        subprocess.run(git_commit, shell=True, check=True)
        
        realizar_push = input("Deseja realizar o push? ")
        if realizar_push == 's' or realizar_push == 'sim':
            subprocess.run(git_push, shell=True, check=True)

    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao tentar copiar ou atualizar a pasta: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
def copiar_pasta(pasta_remota = '', servidor = '', diretorio_local = ''):
    if not servidor:
        servidor = input("Digite o endereço do servidor (ex: usuario@192.168.0.1): ")

    if not pasta_remota:
        pasta_remota = input("Digite o caminho da pasta remota para copiar: ")
    
    if not diretorio_local:
        diretorio_local = get_base_path() + "\\PHP"

    comando = f"scp -r {servidor}:{pasta_remota} {diretorio_local}"

    try:
        subprocess.run(comando, shell=True, check=True)

        realizar_git = input("Deseja realizar o git commit e git push? ").lower()
        if realizar_git == 's' or realizar_git == 'sim':
            rodar_git()

        print(f"Pasta copiada e atualizada com sucesso para o diretório: {diretorio_local}")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao tentar copiar ou atualizar a pasta: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    try:
        copiar_pasta(pasta_remota='/var/www/sistemas/', diretorio_local="UC_Desenvolvimento_Web\\PHP")
    except KeyboardInterrupt:
        print()
        print('Saindo...')