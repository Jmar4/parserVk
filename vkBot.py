import time
import vk


#get token acsess

#global variables
vkSession = vk.Session()
vkApi = vk.API(session)
keyEnd = ('keyend', '/keyend', '/keyEnd', '/KeyEnd', '/KEYEND')
resourceEnd = ('resourceend', '/resourceend', '/resourceEnd', '/ResourceEnd', '/RESOURCEEND')
#vk bot
#vk bot
if vkApi.message.get()==1 & vkApi.message.get().items == '/start':
	vkApi.message.send(user_id=vkApi.message.get().user_id, message="Введите через ';' ресурсы для обработки, для окончания ввода используйте команду /resourceEnd")
	message = vkApi.message.get().text
	while message != resourceEnd:
		messageCounter++
		resources[messageCounter] = message.split(';')
	vkApi.message.send(user_id=vkApi.message.get().user_id, message="Введите через ';' ключи для обработки, для окончания ввода используйте команду /keyEnd")
	message = vkApi.message.get().text
	while message != keyEnd:
		messageCounter++
		keys[messageCounter] = message.split(';')
