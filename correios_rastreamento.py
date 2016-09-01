#coding: UTF-8
import urllib2, re

def cod_rastreamento():
	codigo = raw_input('Codigo de rastreamento: ')
	if len(codigo) != 13:
		print '\nPadrão não corresponde\n'
		cod_rastreamento()
	else:
		conectar(codigo)
def conectar(codigo):
	try:
		site = "http://websro.correios.com.br/sro_bin/txect01%24.QueryList?P_LINGUA=001&P_TIPO=001&P_COD_UNI=" + codigo.upper()
		print ' > Conectando-se a %s...' % site

		#Estabelece a conexão, com timeout de 5 segundos
		con = urllib2.urlopen(site , None , 5)
		print ' > Conexão estabelecida. Obtendo código HTML...'
		html = con.read();
		print ' > Filtrando dados...\n'
		regular(html)
	except:
		print ' > falha na conexão'

def regular(HTML):
	#procura o codigo rastreamento
	if re.search(r'[A-Z0-9]{13}', HTML) == None:
		print 'Codigo invalido!\n'
		cod_rastreamento()
	#Filtra a tabela
	local = re.search(r'</td><td>(.*?)</td>',HTML)
	horario = re.search(r'<tr><td rowspan=\d>(.*?)</td>',HTML)
	situacao = re.search(r'<font color="(.*?)">(.*?)</font>',HTML)

        try:
			print local.group(1)
			print horario.group(1)
			print situacao.group(2)
        except:
            print 'Nenhum dado encontrado...'
if __name__ == '__main__':
	cod_rastreamento()