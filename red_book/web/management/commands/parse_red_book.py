import re
from django.core.management.base import BaseCommand
from web.models import RedBook


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        file1 = []
        with open('C:\\Users\\Foxy\\PycharmProjects\\Project2\\red_book\\web\\utils\\book.txt', 'r',
                  encoding='UTF-8') as f:
            for i in f.read().split('/n'):
                file1.append(i)
        list1 = []
        for i in file1:
            for j in range(0, 202):
                list2 = []
                list2.append(re.findall(r'\d{1,3}', i)[j])
                list2.append(re.findall(r'\d{1,3}\s([А-Я][а-я]+ ?-?[А-Я]?[а-я]+ ?-?[А-Я]?[а-я]+)', i)[j])
                list2.append(re.findall(r'[A-Z][a-z]+ ?-?[A-Z]?[a-z]+', i)[j])
                list2.append(re.findall(r'[a-z] ([А-Я][а-я’ўіiѐ]+ ?-?[А-Я]?[а-я’ўiіѐ]+ ?-?[А-Я]?[а-я’ўiіѐ]+)', i)[j])
                list2.append(re.findall(r'[a-z] [А-Я][а-я’ўіiѐ]+ ?-?[А-Я]?[а-я’ўiіѐ]+ ?-?[А-Я]?[а-я’ўiіѐ]+ (I{1,}V?)', i)[j])
                list1.append(list2)
        print(list1)
        for i in list1:
            RedBook(id=i[0], name=i[1], name_L=i[2], name_B=i[3], priority=i[4]).save()
