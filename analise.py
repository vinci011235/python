def analise(codigo, tokens, estruturas):
    for i in range(0, len(estruturas)):
    	codigo = codigo.replace(estruturas[i], ' ')
    
    c = codigo.split()
    
    for i in range (0, len(c)):
    	if not c[i].isdigit():
    		if not c[i] in tokens:
    			return 'Erro de Sintaxe: ', c[i]
    
    return 'Codigo correto'
    
if __name__ == '__main__':
    codigo = 'int main(){ a=1; b=2; return 0; }'
    tokens = ['int','main','return','if','for','a','b']
    estruturais = [';','(',')','{','}','=']
    
    print analise(codigo, tokens, estruturais)