    
banco_dados_pacientes = []

paciente = {}

usuario_escolha = str(input('ESCOLHA UMA OPÇÃO ENTRE 1 - 5 : '))

if usuario_escolha == "1" : 
    
    print('=== CADASTRAR PACIENTE ===')
    
    paciente['Nome'] = str(input('NOME DO PACIENTE: ')).upper()
    
    paciente_ano_nacimento = int(input('ANO DE NACIMENTO DO PACIENTE: '))
    paciente['Idade'] = paciente_ano_nacimento - datetime.today().year
    
    paciente['Telefone'] = str(input('TELEFONE (DDD) XXXXX-XXXX: '))
    
    banco_dados_pacientes.append(paciente)
    
    
    
