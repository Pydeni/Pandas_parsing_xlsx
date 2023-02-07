import pandas as pd
import pathlib
from pathlib import Path
# отключаем лимит на строки
pd.set_option('display.max_rows', None )
# отключаем лимит на колонки
pd.set_option('display.max_columns', None)
# отключаем лимит на количество символов в записи
pd.set_option('display.max_colwidth', None)
# отключаем перенос при выводе записи на экран(тут в принте), иначе перенесет на новую строку
pd.options.display.expand_frame_repr = False
# Получаем путь, можешь посмореть work_path через принт
work_path = pathlib.Path.cwd()
data_path = Path(work_path, 'Общая_информация_об_объектах-000.csv')
data_path1 = Path(work_path, 'Общая_информация_об_объектах-001.csv')
data_path2 = Path(work_path, '000.xlsx')
data_path3 = Path(work_path, '001.xlsx')
data_path4 = Path(work_path, '002.xlsx')
data_path5 = Path(work_path, '003.xlsx')
data_path6 = Path(work_path, '004.xlsx')
data_path7 = Path(work_path, '005.xlsx')

# отключаем лимит на оперативку, для больших файлов. skiprows = 10 - это с какой строки будет читать файл, header=None - что у файла нет названя столбцов.
data000 = pd.read_csv(data_path, sep=';', low_memory=False, header=None)
data001 = pd.read_csv(data_path1, sep=';', low_memory=False, header=None)
data2271193000 = pd.read_excel(data_path2, skiprows = 13)
data2271193001 = pd.read_excel(data_path3, header=None)
data2271193002 = pd.read_excel(data_path4, header=None)
data2271193003 = pd.read_excel(data_path5, header=None)
data2271193004 = pd.read_excel(data_path6, header=None)
data2271193005 = pd.read_excel(data_path7, header=None)

#  Вывод первых 10 строк csv/excel
# print(data000.head(10))
# Добавление столбца (номер индекса, название стобца)
# data2271193000.insert(3, "Совпадения", " ")
# Добавление значения в ячейку (индекс, название столбца)
# data2271193000.loc[ind,'Совпадения'] = '+'
# Получить значения ячейки по индексу СТРОКИ (не столбца) и названию столбца
# kad_kv = data2271193000['Кад. квартал'].values[ind]

new_df = pd.DataFrame({"Кадастровый номер": [], "Кадастровый квартал": [], "Площадь ЗУ": []})


ind_str = 0
for kad_num in data000[0]:
    if kad_num in data2271193000["Кад №"].unique():
        print(f'Найдено совпадение - {kad_num} ')
        ind = data2271193000.index[data2271193000['Кад №'] == kad_num].tolist()
        kad_kv = ''.join(data2271193000['Кад. квартал'].values[ind])
        square = ''.join(data2271193000['Площадь ЗУ'].values[ind])
        new_df.loc[ind_str, "Кадастровый номер"] = kad_num
        new_df.loc[ind_str, "Кадастровый квартал"] = kad_kv
        new_df.loc[ind_str, "Площадь ЗУ"] = square
        print(f'Отработана {ind_str} строка')
        ind_str = ind_str + 1
        print(f'Инд_стр равен {ind_str}')
    elif kad_num in data2271193001[2].unique():
        print(f'Найдено совпадение - {kad_num} ')
        ind = data2271193001.index[data2271193001[2] == kad_num].tolist()
        kad_kv = ''.join(data2271193001[1].values[ind])
        square = ''.join(data2271193001[21].values[ind])
        new_df.loc[ind_str, "Кадастровый номер"] = kad_num
        new_df.loc[ind_str, "Кадастровый квартал"] = kad_kv
        new_df.loc[ind_str, "Площадь ЗУ"] = square
        print(f'Отработана {ind_str} строка')
        ind_str = ind_str + 1
        print(f'Инд_стр равен {ind_str}')
    elif kad_num in data2271193002[2].unique():
        print(f'Найдено совпадение - {kad_num} ')
        ind = data2271193002.index[data2271193002[2] == kad_num].tolist()
        kad_kv = ''.join(data2271193002[1].values[ind])
        square = ''.join(data2271193002[21].values[ind])
        new_df.loc[ind_str, "Кадастровый номер"] = kad_num
        new_df.loc[ind_str, "Кадастровый квартал"] = kad_kv
        new_df.loc[ind_str, "Площадь ЗУ"] = square
        print(f'Отработана {ind_str} строка')
        ind_str = ind_str + 1
        print(f'Инд_стр равен {ind_str}')
    elif kad_num in data2271193003[2].unique():
        print(f'Найдено совпадение - {kad_num} ')
        ind = data2271193003.index[data2271193003[2] == kad_num].tolist()
        kad_kv = ''.join(data2271193003[1].values[ind])
        square = ''.join(data2271193003[21].values[ind])
        new_df.loc[ind_str, "Кадастровый номер"] = kad_num
        new_df.loc[ind_str, "Кадастровый квартал"] = kad_kv
        new_df.loc[ind_str, "Площадь ЗУ"] = square
        print(f'Отработана {ind_str} строка')
        ind_str = ind_str + 1
        print(f'Инд_стр равен {ind_str}')
    elif kad_num in data2271193004[2].unique():
        print(f'Найдено совпадение - {kad_num} ')
        ind = data2271193004.index[data2271193004[2] == kad_num].tolist()
        kad_kv = ''.join(data2271193004[1].values[ind])
        square = ''.join(data2271193004[21].values[ind])
        new_df.loc[ind_str, "Кадастровый номер"] = kad_num
        new_df.loc[ind_str, "Кадастровый квартал"] = kad_kv
        new_df.loc[ind_str, "Площадь ЗУ"] = square
        print(f'Отработана {ind_str} строка')
        ind_str = ind_str + 1
        print(f'Инд_стр равен {ind_str}')
    elif kad_num in data2271193005[2].unique():
        print(f'Найдено совпадение - {kad_num} ')
        ind = data2271193005.index[data2271193005[2] == kad_num].tolist()
        kad_kv = ''.join(data2271193005[1].values[ind])
        square = ''.join(data2271193005[21].values[ind])
        new_df.loc[ind_str, "Кадастровый номер"] = kad_num
        new_df.loc[ind_str, "Кадастровый квартал"] = kad_kv
        new_df.loc[ind_str, "Площадь ЗУ"] = square
        print(f'Отработана {ind_str} строка')
        ind_str = ind_str + 1
        print(f'Инд_стр равен {ind_str}')
new_df.to_excel(r'C:\Users\denis.osipov\PycharmProjects\pythonProject1\my_data.xlsx', index= False)









#
# with open("Общая_информация_об_объектах-000.csv", encoding='utf-8') as r_file:
#     # Создаем объект DictReader, указываем символ-разделитель ","
#     file_reader = csv.reader(r_file, delimiter = ";")
#     for stroka in file_reader:
#         kad_num = stroka[0]
#     with open("EGRN_VK_INCCA0000583503_ALS_ZU_XX (Универсальный Постановка ЗУ)-2271193-000.csv", mode = 'r+b', encoding='utf-8') as taget:
#         file_taget = csv.reader(taget,  delimiter = ";")
#         for i, row in enumerate(file_taget):
#             if i < 15:
#                 continue
#             else:
#                 for row in file_taget:
#                     if kad_num == row[2]:
#                         row[3] = "+"
