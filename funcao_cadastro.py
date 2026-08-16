def cadastro_paciente(nome,telefone,ano_nascimento) :
    
    banco_dados_pacientes = [], 
    paciente = {}
    
    from datetime import datetime
    ano_atual = datetime.now().year
    
    nome = str(input('Nome do paciente: ')).capitalize()
    paciente['Nome'] = nome

    while True : 

        ano_nascimento = int(input('Ano de nacimento do paciente: '))
        
        idade_atual_paciente = ano_atual - ano_nascimento
        
        if 0 <=idade_atual_paciente <= 120 : 
            paciente['Idade'] = idade_atual_paciente
            break
        
        else : 
            print('ANO DE NASCIMENTO INVÁLIDO')
            
    telefone = input('Digite o telefone apenas com números: ')

    if telefone.isdigit() and len(telefone) == 11:
        print('Telefone válido')
        paciente['Telefone'] = telefone
        
    else:
        print('Telefone inválido')
            
    banco_dados_pacientes.append(paciente)
        
    print('PACIENTE CADASTRADO COM SUCESSO')
    
    