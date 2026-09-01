
from banco_dados import banco_dados_pacientes

def cadastro_paciente() :
    
    paciente = {}
    
    from datetime import datetime
    ano_atual = datetime.now().year
    
    while True : 
        
        nome = str(input('Nome do paciente: ')).strip()
        
        if nome : 
            paciente['Nome'] = nome.capitalize()
            break
        
        print('O nome não pode ficar vazio')

    while True : 

        ano_nascimento = int(input('Ano de nacimento do paciente: '))
        
        idade_atual_paciente = ano_atual - ano_nascimento
        
        if 0 <=idade_atual_paciente <= 120 : 
            paciente['Idade'] = idade_atual_paciente
            break
        
        else : 
            print('ANO DE NASCIMENTO INVÁLIDO')
    
    while True :
        
        try : 
        
            telefone = input('Digite o telefone apenas com números: ')
            
        except : 
            print('Erro,tente novamente')

        if telefone.isdigit() and len(telefone) == 11:
            print('Telefone válido')
            paciente['Telefone'] = telefone
            break
            
        else:
            print('Telefone inválido,Digite novamente')
            
    banco_dados_pacientes.append(paciente)
        
    print('PACIENTE CADASTRADO COM SUCESSO')
    
    