from banco_dados import banco_dados_pacientes

print('=== LISTA DOS PACIENTES CADASTRADOS ===')

def lista_pacientes() :

    for i,paciente in enumerate(banco_dados_pacientes,start=1):
        
        print(
            f"{i} - {paciente['Nome']} | "
            f"{paciente['Idade']} anos | "
            f"{paciente['Telefone']}"
        )