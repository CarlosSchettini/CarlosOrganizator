"""
Carlos Organizator
Este é um programa que automatiza a organização de arquivos em um diretório,
classificando-os em pastas com base em suas extensões.
Autor: Carlos Schettni
Ver. 1.1 - Dezembro de 2024
"""

import os
import sys
from time import sleep

LOGO_INICIO = """                                
                           **                 
                          /**                 
  *****   ******   ****** /**  ******   ******
 **///** //////** //**//* /** **////** **//// 
/**  //   *******  /** /  /**/**   /**//***** 
/**   ** **////**  /**    /**/**   /** /////**
//***** //********/***    ***//******  ****** 
 /////   //////// ///    ///  //////  //////                                                                                                                                                       
"""

BIBLIOTECA_EXT = {
    "Audios": [
        ".wav", ".mp3", ".ogg", ".m4a", ".flac", ".aac", ".alac", ".ape", ".wma", ".opus", ".mid", ".midi", ".ra", ".ram", ".3gp", ".amr"
    ],
    "Planilhas": [
        ".xls", ".xlsx", ".csv", ".ods", ".tsv", ".xlsm", ".xlsb", ".xltx", ".xltm", ".xlam"
    ],
    "Vídeos": [
        ".mov", ".avi", ".mp4", ".mkv", ".wmv", ".flv", ".webm", ".ogv", ".3gp", ".mpeg", ".mpg", ".mts", ".m2ts", ".vob", ".rm", ".rmvb"
    ],
    "Documentos": [
        ".txt", ".doc", ".docx", ".odt", ".rtf", ".log", ".tex", ".md", ".epub", ".mobi", ".azw3", ".fb2", ".chm", ".epub3", ".xps", ".ps", ".srt", ".sub", ".idx", ".pdf"
    ],
    "Imagens": [
        ".jpg", ".jpeg", ".gif", ".png", ".bmp", ".tiff", ".webp", ".ico", ".icns", ".raw", ".nef", ".cr2", ".heif", ".heic", ".dds", ".psd", ".eps", ".indd", ".jpg2000"
    ],
    "Compactados": [
        ".zip", ".7z", ".rar", ".tar", ".gz", ".dmg", ".iso", ".bz2", ".xz", ".tar.gz", ".tar.bz2", ".tar.xz", ".tgz", ".z", ".cab", ".arj", ".lz", ".lzma", ".tar.lz", ".tar.lzma"
    ],
    "Código": [
        ".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".h", ".rb", ".php", ".go", ".ts", ".swift", ".rust", ".pl", ".lua", ".sh", ".bash", ".scala", ".dart", ".r", ".m", ".vhdl", ".for", ".f90", ".vb", ".asm", ".sql", ".json", ".xml", ".yaml", ".toml", ".ini", ".cfg", ".bash_profile", ".gitignore", ".gitattributes", ".dockerfile", ".env"
    ],
    "Fontes": [
        ".ttf", ".otf", ".woff", ".woff2", ".eot", ".fon", ".fnt", ".ttc", ".svgfont"
    ],
    "Backup": [
        ".bak", ".sqldump", ".sql.gz", ".dump", ".dat"
    ],
    "Livros": [
        ".epub", ".mobi", ".azw3", ".cbz", ".cbr", ".djvu", ".fb2", ".lit", ".epub3", ".xps"
    ],
    "Scripts": [
        ".bat", ".ps1", ".exe", ".vbs", ".cgi", ".zsh", ".cmd"
    ],
    "Web": [
        ".asp", ".aspx", ".jsp", ".xhtml", ".less", ".sass", ".scss", ".tpl", ".svg"
    ],
    "Dados": [
        ".db", ".sqlite", ".mdb", ".accdb", ".tsv"
    ],
    "Apresentações": [
        ".ppt", ".pptx", ".odp", ".key", ".pps", ".ppsx", ".potx", ".pot", ".sxi"
    ],
    "Arquivos de Sistema": [
        ".dll", ".pdb", ".cpl", ".ocx", ".inf", ".swp", ".swo", ".sublime-workspace", ".sublime-project"
    ],
    "Design": [
        ".ai", ".psd", ".xd", ".fig", ".cdr", ".indd", ".xcf", ".sketch", ".dxf", ".psp", ".pdn"
    ],
    "Arquivos de Áudio Profissionais": [
        ".aiff", ".pcm", ".dsd", ".au"
    ],
    "Arquivos de Vídeo Profissionais": [
        ".mpeg4", ".h264", ".hevc", ".x264"
    ],
    "Arquivos de Imagem Profissionais": [
        ".dng", ".arw", ".orf", ".sr2", ".x3f"
    ],
"Arquivos CAD": [
        ".dwg", ".dxf", ".ipt", ".iam", ".step", ".iges", ".sat"
    ],
    "Arquivos de Animação e Modelagem 3D": [
        ".fbx", ".blend", ".obj", ".gltf", ".dae", ".3ds", ".max", ".maya", ".c4d"
    ],
    "Arquivos de Jogos": [
        ".bin", ".cue", ".img", ".nrg", ".rom", ".mds", ".mdf", ".gcm", ".apk", ".obb"
    ],
    "Arquivos de Arquitetura": [
        ".skp", ".rvt", ".aec"
    ]
}

class Organizador:
    """
    Verifica os arquivos em um diretório,
    cria as pastas de destino,
    move os arquivos para as pastas corretas e mantém um contador dos arquivos movidos.
    """

    def __init__(self , diretorio: str):
        self.diretorio = diretorio.strip()
        self.arquivos_movidos = {pasta: 0 for pasta in list(BIBLIOTECA_EXT.keys()) + ['Outros']}

    def verifica_arq(self) -> list:
        # Verifica os arquivos presentes no diretório atual.
        # Retorna uma lista com os nomes dos arquivos (excluindo diretórios e arquivos ocultos).
        try:
            arquivos = os.listdir(self.diretorio)
            arquivos_enderecados = []
            nome_programa = os.path.basename(__file__)
            nome_executavel = os.path.basename(sys.executable)

            for arquivo in arquivos:
                caminho_completo = os.path.join(self.diretorio, arquivo)
                if (os.path.isfile(caminho_completo) #Verifica se é mesmo um arquivo
                        and not arquivo.startswith('.') #Exclui da lista os arquivos ocultos
                        and arquivo != nome_programa #Exclui o próprio script, para que ele não se mova
                        and arquivo != nome_executavel): #Exclui o próprio programa, para que ele não se mova
                    arquivos_enderecados.append(arquivo)

            if not arquivos_enderecados:
                print("Nenhum arquivo encontrado para organizar!")

            return arquivos_enderecados

        except Exception as e:
            print(f"Erro ao verificar arquivos: {e}")
            return []

    def criar_pastas(self, arquivos: list) -> None:
        # Cria as pastas para onde os arquivos serão enviados
        try:
            os.chdir(self.diretorio)

            # Itera sobre cada item da lista de arquivos e verifica as extensões
            arquivos_extensoes = set()
            for arquivo in arquivos:
                nome, ext = os.path.splitext(arquivo)
                ext = ext.lower()
                arquivos_extensoes.add(ext)

            # Verifica se há arquivos com extensões desconhecidas
            extensoes_conhecidas = {ext for pasta, extensoes in BIBLIOTECA_EXT.items() for ext in extensoes}
            extensoes_desconhecidas = arquivos_extensoes - extensoes_conhecidas

            for pasta, extensoes in BIBLIOTECA_EXT.items():
                # Cria pastas conforme os arquivos encontrados, e não cria pastas duplicadas.
                for ext in extensoes:
                    if ext in arquivos_extensoes:  # Verifica se há arquivos para aquela extensão
                        if not os.path.exists(pasta):  # Cria pasta se ela já não existir
                            os.mkdir(pasta)
                            print(f"Pasta {pasta.upper()} criada com sucesso.")
                        else:
                            print(f"Pasta {pasta.upper()} já existia.")

            # Cria a pasta "Outros" se houver extensões desconhecidas
            if extensoes_desconhecidas:
                if not os.path.exists("Outros"):
                    os.mkdir("Outros")
                    print("Pasta OUTROS criada com sucesso.")
            return

        except PermissionError:
            print("Erro: Sem permissão para criar pastas neste diretório.")
            return
        except Exception as e:
            print(f"Erro ao criar pastas: {e}")
            return

    def move_arq(self , arquivo: str) -> None:
        # Move os arquivos e atualiza o contador
        try:
            nome, ext = os.path.splitext(arquivo)
            movido = False
            for tipo in BIBLIOTECA_EXT:
                if ext in BIBLIOTECA_EXT[tipo]:
                    origem = os.path.join(self.diretorio, arquivo)
                    destino = os.path.join(self.diretorio, tipo, arquivo)
                    # Tratamento de arquivos duplicados
                    if os.path.exists(destino):
                        base, extension = os.path.splitext(destino)
                        contador = 1
                        while os.path.exists(destino):
                            destino = f"{base}_{contador}{extension}"
                            contador += 1

                    # Movimentação de arquivos
                    os.rename(origem, destino)
                    self.arquivos_movidos[tipo] += 1
                    movido = True
                    break

            # Tratamento de arquivos sem extensão conhecida
            if not movido:
                origem = os.path.join(self.diretorio, arquivo)
                destino = os.path.join(self.diretorio, "Outros", arquivo)

                # Verifica se a pasta 'Outros' existe, se não, cria
                if not os.path.exists(os.path.join(self.diretorio, "Outros")):
                    os.makedirs(os.path.join(self.diretorio, "Outros"))

                os.rename(origem, destino)
                self.arquivos_movidos["Outros"] += 1

        except Exception as e:
            print(f"Erro ao mover o arquivo {arquivo}: {e}")

class InteracaoUsuario:
    """
    Interage com o usuário para obter o diretório de destino e valida a entrada.
    """

    def __init__(self):
        self.diretorio = None

    @staticmethod
    def validar_diretorio(diretorio: str) -> tuple:

        diretorio = os.path.expanduser(diretorio)  # Expande ~ para pasta home
        diretorio = os.path.abspath(diretorio)  # Converte para caminho absoluto

        if not os.path.exists(diretorio):
            return False, "Diretório não existe"
        if not os.path.isdir(diretorio):
            return False, "O caminho não é um diretório"
        if not os.access(diretorio, os.W_OK):
            return False, "Sem permissão de escrita no diretório"

        return True, diretorio

    def menu_selecao_diretorio(self) -> str:
        print("=-" * 20)
        print("CARLOS ORGANIZATOR VER. 1.1".center(40))
        print("=-" * 20)

        while True:
            print("\nVocê deseja organizar a pasta atual ou outra?\n"
                  "\n 1 - PASTA ATUAL"
                  "\n 2 - OUTRA PASTA"
                  "\n 3 - ENCERRAR PROGRAMA")
            opcao_usuario = input(">>> ").strip()

            if opcao_usuario == "1":
                if getattr(sys, 'frozen', False):
                    self.diretorio = os.path.dirname(sys.executable)
                else:
                    self.diretorio = os.getcwd()
                print(f"\nDiretório selecionado: {self.diretorio}")
                sleep(0.5)
                return self.diretorio

            elif opcao_usuario == "2":
                diretorio = input(
                    "Digite o caminho completo ao diretório desejado (ou digite 'sair' para voltar): ").strip().lower()
                if diretorio == "sair":
                    continue

                if os.path.exists(diretorio.strip()):
                    confirma = input(f"O caminho {diretorio} está correto? [S/N]\n>>> ").strip().lower()
                    if confirma == "s":
                        self.diretorio = diretorio
                        return self.diretorio

                else:
                    print("*" * 50)
                    print("Caminho inválido. Por favor, tente novamente.".center(52))
                    print("*" * 50, "\n")

            elif opcao_usuario == "3":
                print("Programa encerrado. Até a próxima!")
                sys.exit()
            else:
                print("*" * 50)
                print("Digite apenas números de 1 a 3".center(40))
                print("*" * 50)

    @staticmethod
    def mostrar_resumo(organizador: Organizador) -> None:
        print("\n")
        print("=-" * 20)
        print("Resumo da organização:")
        print("=-" * 20)

        arquivos_movidos = False
        for pasta, quantidade in organizador.arquivos_movidos.items():
            if quantidade > 0:  # Mostra apenas pastas que receberam arquivos
                print(f"{pasta}: {quantidade} arquivo(s)")
                arquivos_movidos = True

        if not arquivos_movidos:
            print("Nenhum arquivo foi movido.")

        print("\nSua pasta está organizada! 📁✨")

    @staticmethod
    def barra_progresso(total, atual, largura=50) ->str:
        """
        Cria a barra de progresso
        """
        porcentagem = (atual / total) * 100
        preenchido = int((atual / total) * largura)
        barra = '█' * preenchido + '-' * (largura - preenchido)
        return f'\rProgresso: |{barra}| {porcentagem:.1f}% ({atual}/{total})'

    @staticmethod
    def contagem_regressiva() -> None:
        for i in range(5, -1, -1):
            sys.stdout.write(f'\rEncerrando em: {i} segundo(s).')
            sys.stdout.flush()
            sleep(1)
        print("\nAté a próxima!" , flush=True)
        sys.exit()

def main() -> None:
    """
    Função principal que coordena o fluxo do programa.
    """

    try:
        print(LOGO_INICIO)
        interface = InteracaoUsuario()
        diretorio = interface.menu_selecao_diretorio()
        valido, msg = InteracaoUsuario.validar_diretorio(diretorio)

        if not valido:
            print(msg)
            return

        organizador = Organizador(diretorio)
        arquivos = organizador.verifica_arq()

        if not arquivos:
            print("Por favor, tente novamente...")
            return

        # Iniciando a organização dos arquivos
        print(f"\nIniciando organização de {len(arquivos)} arquivos...")

        organizador.criar_pastas(arquivos)

        for i, arquivo in enumerate(arquivos, 1):
            organizador.move_arq(arquivo)
            sys.stdout.write(interface.barra_progresso(len(arquivos), i))
            sys.stdout.flush()

        # Dá um pequeno sleep e força a atualização da saída após o loop
        sleep(0.5)
        sys.stdout.flush()

        #encerramento
        interface.mostrar_resumo(organizador)
        interface.contagem_regressiva()

    except ValueError as e:
        print(e)
    except EOFError:
        print("\nPrograma encerrado.")
        sys.exit()

main()