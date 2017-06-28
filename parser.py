#import libs
import json
import vk
import sqlalchemy
from BeautifulSoup import BeautifulSoup 
import re
import requests as ulrlib3

#global variables
ouputArr = []
apiKey = 'gBVKJESaEsKDTzIPmhuf8tyKnLWlwc677QZMQXey'
vkSession = vk.Session()
vkApi = vk.API(session)

#Create DB
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
	#Create sheme of db
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
data = MetaData()
users_table = Table('users', data,
	Column('id', Integer, primary_key=True),
	Column('keyword', String),
	Column('resource', String),
	Column('date', Integer)
	)
# jSon parse module
def parseJson(jsonIn):
	


#SQLalchemy input module


#parser
#resource 'for'
for mainCounter in range(0, len(resources)+1):
	stirng = in[mainCounter]
	#VK parser
	if string[0:7] == 'vk.com':
		#key search 'for'
		for keysCounter in range(0, len(keys)+1)
			vkPosts = parseJson(vkApi.wall.search(domain=resources[mainCounter], query=keys[keysCounter]))

			for vkPostsCounter in range(0, vkPosts.count +1):
				ouputArr[vkPostsCounter] = vkPosts.items
				
	#web parser
	else:
		resourceForWebParser = resources[mainCounter]
		splitDomain = resourceForWebParser.split('.')
		shortDomain = splitDomain[0]
		#parse all <a> that lead to initial web 
		page = urllib2.urlopen(resource).read()
		soup = BeautifulSoup(page)
		resultParseLinks = soup.findAll(href=re.compile(shortDomain + '$'))
		for linksParserCounter in range(0, len(resultParseLinks)):		
			headers = {'x-api-key': apiKey,}
			params = (('url', resultParseLinks[linksParserCounter]),)
			r = requests.get('https://mercury.postlight.com/parser', headers=headers, params=params)
			ouputArr[linksParserCounter] = r.text


#send via Vk
for vkSendCounter in range(0, len(ouputArr)+1):
	vkApi.message.send(userId=vkUserId, domain=vkUserDomain, message=ouputArr[vkSendCounter])

