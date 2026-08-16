from banco_dados import banco_dados_pacientes

def buscar_paciente():
    
    nome_desejado = str(input('Buscar o paciente: ')).strip().lower()
    
    encotrado = False
    
    for paciente in banco_dados_pacientes :
        
        if paciente['Nome'].lower() == nome_desejado :
        
            print('\n=== PACIENTE ENCONTRADO ===')
            print(f"Nome: {paciente['Nome']}")
            print(f"Idade: {paciente['Idade']}")
            print(f"Telefone: {paciente['Telefone']}")

            encontrado = True
            break

    if not encontrado:
        print('Paciente não encontrado.')