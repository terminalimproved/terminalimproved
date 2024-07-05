# O que é terminalimproved?
TerminalImproved é uma aplicação que pega os comandos dos terminais normais (Linux, MacOS, Windows e etc) e melhora com comandos a mais, sendo atualizado sempre com novos comandos.

# Lista de comandos
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

# Quem é um criador disso aqui? 
é um idi... um desocu... um programador jovem chamado Artur Seixas que ama criar programas parecidos com o terminal.
# Utilização

## Linux: 
sudo apt install python3
sudo apt install git
git clone https://github.com/terminalimproved/terminalimproved
cd terminalimproved
python3 terminal.py --start

## MacOS
brew install python
brew install git
git clone https://github.com/terminalimproved/terminalimproved
cd terminalimproved
python terminal.py --start

## Windows 
git clone https://github.com/terminalimproved/terminalimproved
cd terminalimproved
python terminal.py --start
(Lembre-se de instalar o python e o git)
git : https://git-scm.com/download/win
python : https://www.python.org/downloads/windows/
