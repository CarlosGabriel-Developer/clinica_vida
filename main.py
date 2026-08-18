from cadastro import cadastro_paciente
from estatisticas import ver_estatisticas
from busca import buscar_paciente
from paciente import lista_pacientes

def menu():
    
    print ("-"*40)

    print("=== SISTEMA CLÍNICA VIDA+ ===")
    print('[1] CADASTRAR PACIENTE')
    print('[2] VER ESTATÍSTICAS')
    print('[3] BUSCAR PACIENTE')
    print('[4] LISTA DE TODOS OS PACIENTES')
    print('[5] SAIR')

    print ("-"*40)

while True :
    
    menu()
    
    Usuario_escolha = str(input('Escolha um opção: '))
    
    if Usuario_escolha == '1' : 
        cadastro_paciente()
        
    elif Usuario_escolha == '2' :
        ver_estatisticas()
        
    elif Usuario_escolha == '3' : 
        buscar_paciente()
        
    elif Usuario_escolha == '4' :
        lista_pacientes()
        
    elif Usuario_escolha == '5' : 
        break
    
    else:
        print('Opção invalida')

print ("-"*40)