#coding: UTF-8
import urllib2,re

try:
	URL = "http://websro.correios.com.br/sro_bin/txect01%24.QueryList?P_LINGUA=001&P_TIPO=001&P_COD_UNI="
	codigo = raw_input('Codigo de rastreamento: ')

	#Aborta a execução se for diferente de 13 memo
	if len(codigo) != 13:
	   print '\nPadrão nao corresponde PORRA MONSTRAO\n'
	   exit(1)

	#Formata a URL da cidade, garantindo que as siglas do estado serão maiúsculas	
	url = URL + codigo.upper()
	print ' > Conectando-se a %s...' % url

	#Estabelece a conexão, com timeout de 5 segundos
	con = urllib2.urlopen(url , None , 5)
	print ' > Conexão estabelecida. Obtendo código HTML...'

	#Obtém o código HTML	
	HTML = con.read()
	print ' > Filtrando informações...\n'

	#Valida a página buscando o codigo de rastreamento	
	if re.search(r'[A-Z0-9]{13}', HTML) == None:
	   print 'Codigo invalido!\n'
	   exit(1)

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

except urllib2.URLError:
   print '> Falha na conexão!'
