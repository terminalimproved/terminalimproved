import os
import cmd
import shutil
import requests
import zipfile
import socket
from g4f.client import Client

class SimpleTerminal(cmd.Cmd):
    prompt = '> '
    intro = """Bem-vindo ao terminal simples!

Este é um terminal básico com vários comandos para gerenciar arquivos, diretórios, e realizar algumas operações de rede e web. Abaixo você encontrará uma lista de comandos disponíveis, suas descrições e sintaxes.

Comandos disponíveis:

    ls
        Lista os arquivos no diretório atual.
        Exemplo: ls

    cd <caminho>
        Muda para o diretório especificado.
        Exemplo: cd /home/usuario

    pwd
        Exibe o diretório atual.
        Exemplo: pwd

    mkdir <nome_do_diretorio>
        Cria um novo diretório com o nome especificado.
        Exemplo: mkdir novo_diretorio

    rmdir <nome_do_diretorio>
        Remove um diretório vazio.
        Exemplo: rmdir diretório_vazio

    rm <nome_do_arquivo>
        Remove um arquivo.
        Exemplo: rm arquivo.txt

    cat <nome_do_arquivo>
        Mostra o conteúdo de um arquivo.
        Exemplo: cat arquivo.txt

    touch <nome_do_arquivo>
        Cria um arquivo vazio ou atualiza a data de modificação de um arquivo existente.
        Exemplo: touch novo_arquivo.txt

    echo <texto> [> <arquivo>]
        Imprime um texto ou redireciona o texto para um arquivo.
        Exemplo: echo "Olá, Mundo!" > arquivo.txt

    cp <origem> <destino>
        Copia um arquivo ou diretório para um novo destino.
        Exemplo: cp arquivo.txt backup_arquivo.txt

    mv <origem> <destino>
        Move ou renomeia um arquivo ou diretório.
        Exemplo: mv arquivo.txt novo_arquivo.txt

    find <nome_do_arquivo>
        Busca por arquivos no diretório atual ou em subdiretórios com um nome especificado.
        Exemplo: find arquivo.txt

    clear
        Limpa a tela do terminal.
        Exemplo: clear

    backup <caminho>
        Faz backup de um arquivo ou diretório criando uma cópia com o sufixo _backup.
        Exemplo: backup arquivo_ou_diretorio

    search_content <palavra> <diretório>
        Busca por uma palavra ou frase dentro dos arquivos de um diretório.
        Exemplo: search_content 'erro' /var/logs

    download_file <url> <nome_do_arquivo>
        Faz o download de um arquivo de uma URL.
        Exemplo: download_file http://exemplo.com/arquivo.zip arquivo.zip

    zip <nome_do_arquivo_zip> <arquivo1> [<arquivo2> ...]
        Compacta arquivos ou diretórios em um arquivo zip.
        Exemplo: zip arquivos.zip arquivo1.txt arquivo2.txt diretorio/

    unzip <nome_do_arquivo_zip>
        Descompacta um arquivo zip.
        Exemplo: unzip arquivo.zip

    exit
        Sai do terminal.
        Exemplo: exit

    EOF
        Sai do terminal com Ctrl-D.
        Exemplo: Ctrl-D

    head <nome_do_arquivo>
        Exibe as primeiras 10 linhas de um arquivo.
        Exemplo: head arquivo.txt

    tail <nome_do_arquivo>
        Exibe as últimas 10 linhas de um arquivo.
        Exemplo: tail arquivo.txt

    chmod <permissões> <nome_do_arquivo>
        Altera as permissões de um arquivo ou diretório.
        Exemplo: chmod 755 arquivo.txt

    rename <nome_antigo> <nome_novo>
        Renomeia um arquivo ou diretório.
        Exemplo: rename arquivo_antigo.txt arquivo_novo.txt

    listen <porta>
        Cria um servidor simples que escuta na porta especificada.
        Exemplo: listen 8080

    fetch <url>
        Obtém o conteúdo de uma URL.
        Exemplo: fetch http://exemplo.com

    history
        Exibe o histórico de comandos executados.
        Exemplo: history

    save <nome_do_arquivo>
        Salva o histórico de comandos em um arquivo.
        Exemplo: save histórico.txt

    restore <nome_do_arquivo>
        Restaura o histórico de comandos a partir de um arquivo.
        Exemplo: restore histórico.txt

    run <comando>
        Executa um comando do sistema.
        Exemplo: run ls -l

Digite 'help <comando>' para obter mais detalhes sobre um comando específico.
"""

    def __init__(self):
        super().__init__()
        self.client = Client()
        self.messages = [{"role": "user", "content": "Olá, como posso ajudar você hoje?"}]
        self.cmdqueue = []

    def do_ls(self, arg):
        "Lista os arquivos no diretório atual: ls"
        files = os.listdir('.')
        for file in files:
            print(file)

    def help_ls(self):
        print("Lista os arquivos no diretório atual.")
        print("Sintaxe: ls")

    def do_cd(self, path):
        "Muda para o diretório especificado: cd <caminho>"
        try:
            os.chdir(path)
            print(f'Diretório atual: {os.getcwd()}')
        except FileNotFoundError:
            print(f'Erro: O diretório {path} não existe.')
        except NotADirectoryError:
            print(f'Erro: {path} não é um diretório.')
        except PermissionError:
            print(f'Erro: Permissão negada para acessar {path}.')

    def help_cd(self):
        print("Muda para o diretório especificado.")
        print("Sintaxe: cd <caminho>")
        print("Exemplo: cd /home/usuario")

    def do_pwd(self, arg):
        "Exibe o diretório atual: pwd"
        print(os.getcwd())

    def help_pwd(self):
        print("Exibe o diretório atual.")
        print("Sintaxe: pwd")

    def do_mkdir(self, path):
        "Cria um novo diretório: mkdir <nome_do_diretorio>"
        try:
            os.mkdir(path)
            print(f'Diretório {path} criado.')
        except FileExistsError:
            print(f'Erro: O diretório {path} já existe.')
        except PermissionError:
            print(f'Erro: Permissão negada para criar {path}.')

    def help_mkdir(self):
        print("Cria um novo diretório com o nome especificado.")
        print("Sintaxe: mkdir <nome_do_diretorio>")
        print("Exemplo: mkdir novo_diretorio")

    def do_rmdir(self, path):
        "Remove um diretório vazio: rmdir <nome_do_diretorio>"
        try:
            os.rmdir(path)
            print(f'Diretório {path} removido.')
        except FileNotFoundError:
            print(f'Erro: O diretório {path} não existe.')
        except OSError:
            print(f'Erro: O diretório {path} não está vazio ou não pode ser removido.')

    def help_rmdir(self):
        print("Remove um diretório vazio.")
        print("Sintaxe: rmdir <nome_do_diretorio>")
        print("Exemplo: rmdir diretório_vazio")

    def do_rm(self, path):
        "Remove um arquivo: rm <nome_do_arquivo>"
        try:
            os.remove(path)
            print(f'Arquivo {path} removido.')
        except FileNotFoundError:
            print(f'Erro: O arquivo {path} não existe.')
        except PermissionError:
            print(f'Erro: Permissão negada para remover {path}.')

    def help_rm(self):
        print("Remove um arquivo.")
        print("Sintaxe: rm <nome_do_arquivo>")
        print("Exemplo: rm arquivo.txt")

    def do_cat(self, path):
        "Mostra o conteúdo de um arquivo: cat <nome_do_arquivo>"
        try:
            with open(path, 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print(f'Erro: O arquivo {path} não existe.')
        except PermissionError:
            print(f'Erro: Permissão negada para ler {path}.')
        except UnicodeDecodeError:
            print(f'Erro: Não é possível ler o arquivo {path}. Arquivo pode estar em formato binário.')

    def help_cat(self):
        print("Mostra o conteúdo de um arquivo.")
        print("Sintaxe: cat <nome_do_arquivo>")
        print("Exemplo: cat arquivo.txt")

    def do_touch(self, path):
        "Cria um arquivo vazio ou atualiza a data de modificação de um arquivo existente: touch <nome_do_arquivo>"
        try:
            with open(path, 'a'):
                os.utime(path, None)
            print(f'Arquivo {path} criado/atualizado.')
        except PermissionError:
            print(f'Erro: Permissão negada para criar/atualizar {path}.')

    def help_touch(self):
        print("Cria um arquivo vazio ou atualiza a data de modificação de um arquivo existente.")
        print("Sintaxe: touch <nome_do_arquivo>")
        print("Exemplo: touch novo_arquivo.txt")

    def do_echo(self, arg):
        "Imprime um texto ou redireciona para um arquivo: echo <texto> [> <arquivo>]"
        parts = arg.split('>')
        text = parts[0].strip()
        if len(parts) > 1:
            filename = parts[1].strip()
            try:
                with open(filename, 'w') as file:
                    file.write(text + '\n')
                print(f'Texto escrito em {filename}.')
            except PermissionError:
                print(f'Erro: Permissão negada para escrever em {filename}.')
        else:
            print(text)

    def help_echo(self):
        print("Imprime um texto ou redireciona o texto para um arquivo.")
        print("Sintaxe: echo <texto> [> <arquivo>]")
        print("Exemplo: echo \"Olá, Mundo!\" > arquivo.txt")

    def do_cp(self, arg):
        "Copia um arquivo: cp <origem> <destino>"
        try:
            src, dst = arg.split()
            shutil.copy(src, dst)
            print(f'Arquivo {src} copiado para {dst}.')
        except FileNotFoundError:
            print(f'Erro: O arquivo {src} não existe.')
        except PermissionError:
            print(f'Erro: Permissão negada para copiar {src}.')
        except Exception as e:
            print(f'Erro: {e}')

    def help_cp(self):
        print("Copia um arquivo ou diretório para um novo destino.")
        print("Sintaxe: cp <origem> <destino>")
        print("Exemplo: cp arquivo.txt backup_arquivo.txt")

    def do_mv(self, arg):
        "Move ou renomeia um arquivo ou diretório: mv <origem> <destino>"
        try:
            src, dst = arg.split()
            shutil.move(src, dst)
            print(f'{src} movido/renomeado para {dst}.')
        except FileNotFoundError:
            print(f'Erro: O arquivo ou diretório {src} não existe.')
        except PermissionError:
            print(f'Erro: Permissão negada para mover {src}.')
        except Exception as e:
            print(f'Erro: {e}')

    def help_mv(self):
        print("Move ou renomeia um arquivo ou diretório.")
        print("Sintaxe: mv <origem> <destino>")
        print("Exemplo: mv arquivo.txt novo_arquivo.txt")

    def do_find(self, name):
        "Busca arquivos no diretório atual ou em subdiretórios com um nome especificado: find <nome_do_arquivo>"
        found = False
        for root, dirs, files in os.walk('.'):
            if name in files:
                print(os.path.join(root, name))
                found = True
        if not found:
            print(f'Nenhum arquivo encontrado com o nome {name}.')

    def help_find(self):
        print("Busca por arquivos no diretório atual ou em subdiretórios com um nome especificado.")
        print("Sintaxe: find <nome_do_arquivo>")
        print("Exemplo: find arquivo.txt")

    def do_clear(self, arg):
        "Limpa a tela do terminal: clear"
        os.system('cls' if os.name == 'nt' else 'clear')

    def help_clear(self):
        print("Limpa a tela do terminal.")
        print("Sintaxe: clear")

    def do_backup(self, path):
        "Faz backup de um arquivo ou diretório: backup <caminho>"
        try:
            if os.path.isdir(path):
                shutil.copytree(path, f"{path}_backup")
                print(f'Diretório {path} copiado para {path}_backup.')
            else:
                shutil.copy(path, f"{path}_backup")
                print(f'Arquivo {path} copiado para {path}_backup.')
        except Exception as e:
            print(f'Erro: {e}')

    def help_backup(self):
        print("Faz backup de um arquivo ou diretório criando uma cópia com o sufixo _backup.")
        print("Sintaxe: backup <caminho>")
        print("Exemplo: backup arquivo_ou_diretorio")

    def do_search_content(self, arg):
        "Busca por uma palavra ou frase dentro dos arquivos de um diretório: search_content <palavra> <diretório>"
        try:
            keyword, path = arg.split()
            found = False
            for root, _, files in os.walk(path):
                for file in files:
                    try:
                        with open(os.path.join(root, file), 'r') as f:
                            if keyword in f.read():
                                print(f'{keyword} encontrado em {file}')
                                found = True
                    except UnicodeDecodeError:
                        pass  # Ignora arquivos binários
            if not found:
                print(f'Palavra {keyword} não encontrada em nenhum arquivo do diretório {path}.')
        except ValueError:
            print('Uso correto: search_content <palavra> <diretório>')
        except Exception as e:
            print(f'Erro: {e}')

    def help_search_content(self):
        print("Busca por uma palavra ou frase dentro dos arquivos de um diretório.")
        print("Sintaxe: search_content <palavra> <diretório>")
        print("Exemplo: search_content 'erro' /var/logs")

    def do_download_file(self, arg):
        "Faz o download de um arquivo de uma URL: download_file <url> <nome_do_arquivo>"
        try:
            url, filename = arg.split()
            r = requests.get(url)
            with open(filename, 'wb') as file:
                file.write(r.content)
            print(f'Arquivo {filename} baixado de {url}.')
        except Exception as e:
            print(f'Erro: {e}')

    def help_download_file(self):
        print("Faz o download de um arquivo de uma URL.")
        print("Sintaxe: download_file <url> <nome_do_arquivo>")
        print("Exemplo: download_file http://exemplo.com/arquivo.zip arquivo.zip")

    def do_zip(self, arg):
        "Compacta arquivos ou diretórios em um arquivo zip: zip <nome_do_arquivo_zip> <arquivo1> [<arquivo2> ...]"
        try:
            args = arg.split()
            zip_filename = args[0]
            files_to_zip = args[1:]
            with zipfile.ZipFile(zip_filename, 'w') as zipf:
                for file in files_to_zip:
                    if os.path.isdir(file):
                        for root, _, files in os.walk(file):
                            for f in files:
                                zipf.write(os.path.join(root, f))
                    else:
                        zipf.write(file)
            print(f'Arquivos compactados em {zip_filename}.')
        except Exception as e:
            print(f'Erro: {e}')

    def help_zip(self):
        print("Compacta arquivos ou diretórios em um arquivo zip.")
        print("Sintaxe: zip <nome_do_arquivo_zip> <arquivo1> [<arquivo2> ...]")
        print("Exemplo: zip arquivos.zip arquivo1.txt arquivo2.txt diretorio/")

    def do_unzip(self, arg):
        "Descompacta um arquivo zip: unzip <nome_do_arquivo_zip>"
        try:
            with zipfile.ZipFile(arg, 'r') as zipf:
                zipf.extractall()
            print(f'Arquivo {arg} descompactado.')
        except FileNotFoundError:
            print(f'Erro: O arquivo {arg} não existe.')
        except zipfile.BadZipFile:
            print(f'Erro: O arquivo {arg} não é um arquivo zip válido.')
        except Exception as e:
            print(f'Erro: {e}')

    def help_unzip(self):
        print("Descompacta um arquivo zip.")
        print("Sintaxe: unzip <nome_do_arquivo_zip>")
        print("Exemplo: unzip arquivo.zip")

    def do_exit(self, arg):
        "Sai do terminal: exit"
        print("Saindo do terminal...")
        return True

    def help_exit(self):
        print("Sai do terminal.")
        print("Sintaxe: exit")

    def do_EOF(self, arg):
        "Sai do terminal com Ctrl-D: EOF"
        print("Saindo do terminal...")
        return True

    def help_EOF(self):
        print("Sai do terminal com Ctrl-D.")
        print("Sintaxe: Ctrl-D")

    def do_head(self, arg):
        "Exibe as primeiras 10 linhas de um arquivo: head <nome_do_arquivo>"
        try:
            with open(arg, 'r') as file:
                for i, line in enumerate(file):
                    if i < 10:
                        print(line, end='')
                    else:
                        break
        except FileNotFoundError:
            print(f'Erro: O arquivo {arg} não existe.')
        except PermissionError:
            print(f'Erro: Permissão negada para ler {arg}.')
        except Exception as e:
            print(f'Erro: {e}')

    def help_head(self):
        print("Exibe as primeiras 10 linhas de um arquivo.")
        print("Sintaxe: head <nome_do_arquivo>")
        print("Exemplo: head arquivo.txt")

    def do_tail(self, arg):
        "Exibe as últimas 10 linhas de um arquivo: tail <nome_do_arquivo>"
        try:
            with open(arg, 'r') as file:
                lines = file.readlines()
                for line in lines[-10:]:
                    print(line, end='')
        except FileNotFoundError:
            print(f'Erro: O arquivo {arg} não existe.')
        except PermissionError:
            print(f'Erro: Permissão negada para ler {arg}.')
        except Exception as e:
            print(f'Erro: {e}')

    def help_tail(self):
        print("Exibe as últimas 10 linhas de um arquivo.")
        print("Sintaxe: tail <nome_do_arquivo>")
        print("Exemplo: tail arquivo.txt")

    def do_chmod(self, arg):
        "Altera as permissões de um arquivo ou diretório: chmod <permissões> <nome_do_arquivo>"
        try:
            permissions, path = arg.split()
            os.chmod(path, int(permissions, 8))
            print(f'Permissões de {path} alteradas para {permissions}.')
        except ValueError:
            print('Uso correto: chmod <permissões> <nome_do_arquivo>')
        except FileNotFoundError:
            print(f'Erro: O arquivo {path} não existe.')
        except PermissionError:
            print(f'Erro: Permissão negada para alterar permissões de {path}.')
        except Exception as e:
            print(f'Erro: {e}')

    def help_chmod(self):
        print("Altera as permissões de um arquivo ou diretório.")
        print("Sintaxe: chmod <permissões> <nome_do_arquivo>")
        print("Exemplo: chmod 755 arquivo.txt")

    def do_rename(self, arg):
        "Renomeia um arquivo ou diretório: rename <nome_antigo> <nome_novo>"
        try:
            old_name, new_name = arg.split()
            os.rename(old_name, new_name)
            print(f'{old_name} renomeado para {new_name}.')
        except FileNotFoundError:
            print(f'Erro: O arquivo ou diretório {old_name} não existe.')
        except PermissionError:
            print(f'Erro: Permissão negada para renomear {old_name}.')
        except Exception as e:
            print(f'Erro: {e}')

    def help_rename(self):
        print("Renomeia um arquivo ou diretório.")
        print("Sintaxe: rename <nome_antigo> <nome_novo>")
        print("Exemplo: rename arquivo_antigo.txt arquivo_novo.txt")

    def do_listen(self, port):
        "Cria um servidor simples que escuta na porta especificada: listen <porta>"
        try:
            port = int(port)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
                server_socket.bind(('localhost', port))
                server_socket.listen()
                print(f'Escutando na porta {port}...')
                conn, addr = server_socket.accept()
                with conn:
                    print(f'Conectado a {addr}')
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        conn.sendall(data)
        except ValueError:
            print('Porta deve ser um número inteiro.')
        except OSError as e:
            print(f'Erro: {e}')
        except Exception as e:
            print(f'Erro: {e}')

    def help_listen(self):
        print("Cria um servidor simples que escuta na porta especificada.")
        print("Sintaxe: listen <porta>")
        print("Exemplo: listen 8080")

    def do_fetch(self, url):
        "Obtém o conteúdo de uma URL: fetch <url>"
        try:
            response = requests.get(url)
            print(response.text)
        except requests.RequestException as e:
            print(f'Erro: {e}')

    def help_fetch(self):
        print("Obtém o conteúdo de uma URL.")
        print("Sintaxe: fetch <url>")
        print("Exemplo: fetch http://exemplo.com")

    def do_history(self, arg):
        "Exibe o histórico de comandos executados: history"
        for i, command in enumerate(self.cmdqueue):
            print(f'{i + 1}: {command}')

    def help_history(self):
        print("Exibe o histórico de comandos executados.")
        print("Sintaxe: history")

    def do_save(self, filename):
        "Salva o histórico de comandos em um arquivo: save <nome_do_arquivo>"
        try:
            with open(filename, 'w') as file:
                for command in self.cmdqueue:
                    file.write(command + '\n')
            print(f'Histórico salvo em {filename}.')
        except Exception as e:
            print(f'Erro: {e}')

    def help_save(self):
        print("Salva o histórico de comandos em um arquivo.")
        print("Sintaxe: save <nome_do_arquivo>")
        print("Exemplo: save histórico.txt")

    def do_restore(self, filename):
        "Restaura o histórico de comandos a partir de um arquivo: restore <nome_do_arquivo>"
        try:
            with open(filename, 'r') as file:
                self.cmdqueue = [line.strip() for line in file.readlines()]
            print(f'Histórico restaurado de {filename}.')
        except FileNotFoundError:
            print(f'Erro: O arquivo {filename} não existe.')
        except Exception as e:
            print(f'Erro: {e}')

    def help_restore(self):
        print("Restaura o histórico de comandos a partir de um arquivo.")
        print("Sintaxe: restore <nome_do_arquivo>")
        print("Exemplo: restore histórico.txt")

    def do_run(self, command):
        "Executa um comando do sistema: run <comando>"
        try:
            os.system(command)
        except Exception as e:
            print(f'Erro: {e}')

    def help_run(self):
        print("Executa um comando do sistema.")
        print("Sintaxe: run <comando>")
        print("Exemplo: run ls -l")

    def do_help(self, arg):
        "Mostra uma descrição detalhada dos comandos disponíveis: help <comando>"
        if arg:
            func = getattr(self, f'help_{arg}', None)
            if func:
                func()
            else:
                print(f'Comando {arg} não encontrado.')
        else:
            print("Comandos disponíveis:")
            for command in dir(self):
                if command.startswith('do_'):
                    print(f'  {command[3:]}')

    def help_help(self):
        print("Mostra uma descrição detalhada dos comandos disponíveis ou uma descrição específica para um comando.")
        print("Sintaxe: help <comando>")
        print("Exemplo: help ls")

if __name__ == '__main__':
    SimpleTerminal().cmdloop()
