# Из исходного текстового файла (pazzl.html) выбрать все html-коды изображений, посчитать их количество.
import re
a = open('pazzl.html', 'r', encoding='UTF-8')
b = a.read()

result = re.findall('img', b)
print(len(result))

