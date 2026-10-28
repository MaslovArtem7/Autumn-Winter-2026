class File:
    def __init__(self, id_file, name, size, type, id_catalog):
        self.id_file = id_file
        self.name = name
        self.size = size
        self.type = type
        self.id_catalog = id_catalog


class Catalog:
    def __init__(self, id_catalog, name):
        self.id_catalog = id_catalog
        self.name = name


class File_catalog:
    def __init__(self, id_file, id_catalog):
        self.id_file = id_file
        self.id_catalog = id_catalog


data_file = [
    File(1, 'Атлас', 100, 'txt', 1),
    File(2, 'Инструкция', 120, 'txt', 1),
    File(3, 'Сборник рассказов', 519, 'pdf', 2),
    File(4, 'Документация', 87, 'docx', 3),
    File(5, 'Презентация', 317, 'pdf', 2),
    File(6, 'Дид. материал', 629, 'pdf', 4)
]

data_catalog = [
    Catalog(1, 'текстовые файлы'),
    Catalog(2, 'pdf - файлы'),
    Catalog(3, 'word - файлы'),
    Catalog(4, 'Учебные материалы')
]

data_catalog_file = [
    File_catalog(1, 1),
    File_catalog(2, 1),
    File_catalog(2, 4),
    File_catalog(3, 2),
    File_catalog(4, 3),
    File_catalog(5, 2),
    File_catalog(4, 4)
]

# Запрос 1
'''request = [(a.name, b.name) for a in data_file for b in data_catalog if a.id_catalog == b.id_catalog]

answer = sorted(request, key=lambda x: x[0])

for x in answer:
    print(*x)'''

# Запрос 2
'''request = [(a.id_file, b.id_catalog) for a in data_file for b in data_catalog if a.id_catalog == b.id_catalog]
answer = []

for k in data_catalog:
    count_files = len([x for x in data_file if x.id_catalog == k.id_catalog])
    answer.append([k.name, count_files])

answer = sorted(answer, key=lambda x: x[1])
for x in answer:
    print(*x)'''

# Запрос 3

request = [(a.name, b.name)
           for a in data_file
           for ab in data_catalog_file
           for b in data_catalog
           if a.id_file == ab.id_file and ab.id_catalog == b.id_catalog]
print(request)
