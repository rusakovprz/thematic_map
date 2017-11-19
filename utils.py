# -*- coding: utf-8 -*-
import csv


def strToFloat( arg ):
  try:
    return float(arg)
  except:
    return 0


def strToInt( arg ):
  try:
    return int(arg)
  except:
    return 0


def get_min_max_values(values):
  tmp_array = []

  for item in values:
    try:
      tmp_array.append(float(item))
    except:
      pass

  return min(tmp_array), max(tmp_array)


def parse_csv(filename):
  data = {}

  try:
    reader = csv.reader(open(filename), delimiter=",")
  except IOError:
    showerror("Ошибка", "Указанный файл не найден.")
    return data

  for row in reader:
    try:
      region = row[0]
      value =  row[1].strip()
      data[region] = value

    except IndexError as err:
      print "read_and_parse_csv Error:", err

    except :
      showerror("Ошибка", "Нарушена стркутура CSV файла.")

  return data

