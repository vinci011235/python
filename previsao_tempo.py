#coding: UTF-8
import urllib2,re

try:
	site = 'http://www.tempoagora.com.br/previsao-do-tempo/'
	cidade = raw_input('Nome da cidade: ')
	estado = raw_input('Sigla do estado: ')

	#Remove os espaços que possam existir em um nome de cidade composto
	cidade = cidade.replace(' ' , '')

	#Aborta a execução caso a sigla do estado tenha mais de dois caracteres
	if len(estado) != 2:
	   print '\nA sigla do estado deve ter duas letras!\n'
	   exit(1)

	#Formata a URL da cidade, garantindo que as siglas do estado serão maiúsculas	
	url = site + estado + '/' + cidade
	print ' > Conectando-se a %s...' % url

	#Estabelece a conexão, com timeout de 5 segundos
	con = urllib2.urlopen(url , None , 5)
	print ' > Conexão estabelecida. Obtendo código HTML...'

	#Obtém o código HTML	
	HTML = con.read()
	print ' > Filtrando informações...\n'

	#Valida a página buscando o padrão "cidade - estado", que só é exibido em páginas válidas	
	#EXEMPLO HTML: londrina - PR
	if re.search(r'[A-Z][^-]+- [A-Z]{2}' , HTML) == None:
	   print 'Cidade inválida!\n'
	   exit(1)

	#Busca a condição climática, que é informada entre os fragmentos de tags %;\"> e <
	#EXEMPLO HTML:<div class="pull-left description"><p>Tempo fechado e chuvoso, com possíveis trovoadas</p>
	status = re.search(r'\"pull-left description\">\
			<\p>(.*?)<', HTML)

	#Obtém a data última atualização
	#EXEMPLO HTML:<div class="dsp-cell"><h3>30/08</h3>
	atualizado = re.search(r'\"dsp-cell\">\
                <\h3>(.*?)<', HTML)

	print cidade.upper(), estado.upper()
	print status.group(1)
	print atualizado.group(1),'\n'

except urllib2.URLError:
   print '> Falha na conexão!'