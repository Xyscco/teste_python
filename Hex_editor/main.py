def substituir_texto_binario(arquivo_entrada, arquivo_saida, texto_antigo, texto_novo):
    """
    Substitui texto em um arquivo binário
    """
    # Ler o arquivo binário
    with open(arquivo_entrada, 'rb') as arquivo:
        conteudo = arquivo.read()
    
    # Converter strings para bytes
    texto_antigo_bytes = texto_antigo.encode('utf-8')
    texto_novo_bytes = texto_novo.encode('utf-8')
    
    # Realizar a substituição
    conteudo_modificado = conteudo.replace(texto_antigo_bytes, texto_novo_bytes)
    
    # Salvar o arquivo modificado
    with open(arquivo_saida, 'wb') as arquivo:
        arquivo.write(conteudo_modificado)
    
    print(f"Substituição concluída: {arquivo_entrada} -> {arquivo_saida}")

# Exemplo de uso
substituir_texto_binario('Hex_editor/TEKFARMA.fbd', 'Hex_editor/tekfarma_modificado.fdb', 'SYSDBA', 'SYDBB')