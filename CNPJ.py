import requests
import json
import sys

if len(sys.argv) > 1:
    #Obtem o parametro da linha de comando
    cnpj = ' '.join(sys.argv[1:])
    response = requests.get('https://www.receitaws.com.br/v1/cnpj/' + cnpj)
    archive = json.loads(response.text)
    
    #print(archive['nome'])

    for i in archive:
        print (archive[i])       

    '''
    file = open("workfile.txt", "w")
    file.write(archive['nome'])
    file.write("\n")
    file.write(archive['cnpj'])

    file.close()
    '''
else:
    print("Usage: CNPJ.py [CNPJ]")