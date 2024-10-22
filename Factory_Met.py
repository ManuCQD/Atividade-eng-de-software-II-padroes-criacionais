from Arquivos import TxtArquivo, DocxArquivo, PdfArquivo  # Importa as classes corretamente

# Verifica o tipo de arquivo e retorna a classe correspondente

def criar_arquivos(tipo_arquivo):  # Verifica o tipo de arquivo e retorna a classe correspondente
    if tipo_arquivo == "txt":
        return TxtArquivo()  #caso verdadeiro ele ira retorna uma instância da classe TxtArquivo
    elif tipo_arquivo == "docx":
        return DocxArquivo()  #caso verdadeiro ele ira retorna uma instância da classe docx
    elif tipo_arquivo == "pdf":
        return PdfArquivo()  #caso verdadeiro ele ira retorna uma instância da classe pdf
    else:
        print("Tipo de arquivo não encontrado")
        

arquivo = criar_arquivos('pdf')  # passamos como entrada "pdf" então com 4 e 5 linha são verdadeiras, sendo assim ele retornara uma instancia da classe pdfarquivo
arquivo.ler_conteudo()  # Chama o método para ler o conteúdo
