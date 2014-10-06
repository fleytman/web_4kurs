# -*- coding: utf-8 -*-
from grab import Grab

##Логирование
#import logging
#logger = logging.getLogger('grab')
#logger.addHandler(logging.StreamHandler())
#logger.setLevel(logging.DEBUG)

g = Grab()
g.go('http://gepir.gs1.org/v32/xx/gtin.aspx')
#Устанавливаем в форму поиска значение
g.set_input('TabContainerGTIN:TabPanelGTIN:txtRequestGTIN', '4607005930248')
#Выбираем checkbox
g.set_input('TabContainerGTIN:TabPanelGTIN:rblGTIN', 'item')


#Отправляем запрос
g.submit()

g.response.save("out1.aspx")

print g.search(u'4607005930248')
