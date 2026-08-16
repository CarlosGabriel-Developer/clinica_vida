from banco_dados import banco_dados_pacientes

def ver_estatisticas():
    
    if len(banco_dados_pacientes) == 0:
        print('Nenhum paciente foi cadastrado')
        return
    
    total_pacientes = len(banco_dados_pacientes)
    
    idades = []
    
    for paciente in banco_dados_pacientes :
        idades.append(paciente['Idade'])
        
    media_idade = sum(idades)/len(idades)
    
    maior_idade = max(idades)
    menor_idade = min(idades)
    
    print('\n=== ESTATÍSTICAS ===')
    print(f'Total de pacientes: {total_pacientes}')
    print(f'Média de idade: {media_idade:.1f} anos')
    print(f'Maior idade: {maior_idade} anos')
    print(f'Menor idade: {menor_idade} anos')