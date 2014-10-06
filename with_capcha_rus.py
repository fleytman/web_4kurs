# -*- coding: utf-8 -*-
from grab import Grab


g = Grab()
g.go('http://gs46.gs1ru.org/GEPIR31/index.jsp?p=gtin&lng=ru')
g.response.save("out.html")

print g.tree
print g.tree.xpath("//img")[0]

#print g.xpath_text('//img[@id="recaptcha_challenge_image"')
print g.search(u"recaptcha_image")
##Устанавливаем в форму поиска значение
#g.set_input('TabContainerGTIN:TabPanelGTIN:txtRequestGTIN', '4607005930248')
##Выбираем checkbox
#g.set_input('TabContainerGTIN:TabPanelGTIN:rblGTIN', 'item')
#
#
##Отправляем запрос
#g.submit()
#
#g.response.save("out1.aspx")
#
#print g.search(u'4607005930248')
#
