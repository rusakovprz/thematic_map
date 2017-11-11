# -*- coding: utf-8 -*-
import csv
from xml.dom import minidom
import xml.etree as etree

import cairo
import rsvg


global colors

colors = [
[
# 4 градации серого (gray)
[[247, 247, 247],[204, 204, 204],[150, 150, 150],[82, 82, 82]],
# 5 градаций серого
[[247, 247, 247],[204, 204, 204],[150, 150, 150],[99, 99, 99],[37, 37, 37]],
# 6 градаций серого
[[247, 247, 247],[217, 217, 217],[189, 189, 189],[150, 150, 150],[99, 99, 99],[37, 37, 37]]
],
[
# 4 градации оранжевого (orange)
[[254, 240, 217],[253, 204, 138],[252, 141, 89],[215, 48, 31]],
# 5 градаций оранжевого
[[254, 240, 217],[253, 204, 138],[252, 141, 89],[227, 74, 51],[179, 0, 0]],
# 6 градаций оранжевого
[[254, 240, 217],[253, 212, 158],[253, 187, 132],[252, 141, 89],[227, 74, 51],[179, 0, 0]]
],
[
# 4 градации фиолетового (purple)
[[242, 240, 247],[203, 201, 226],[158, 154, 200],[106, 81, 163]],
# 5 градаций фиолетового
[[242, 240, 247],[203, 201, 226],[158, 154, 200],[117, 107, 177],[84, 39, 143]],
# 6 градаций фиолетового
[[242, 240, 247],[218, 218, 235],[188, 189, 220],[158, 154, 200],[117, 107, 177],[84, 39, 143]]
],
[
# 4 градации зелёного
[[237, 248, 233],[186, 228, 179],[116, 196, 118],[35, 139, 69]],
# 5 градаций зелёного
[[237, 248, 233],[186, 228, 179],[116, 196, 118],[49, 163, 84],[0, 109, 44]],
# 6 градаций зелёного
[[237, 248, 233],[199, 233, 192],[161, 217, 155],[116, 196, 118],[49, 163, 84],[0, 109, 44]]
]		]


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


def edit_svg(svg, statistic, match_band, bands, palett):
  flag_no_data = False                      # Признак отсутствия данных хотябы для одного региона.
  doc = minidom.parseString(svg)            # Парсим SVG.
  paths = doc.getElementsByTagName("path")  # Просматриваем всю карту. Находим соответствующий узел и редактируем его.

  for path in paths:
    region = path.getAttribute("id")
    if region == "":  # В SVG файле могут быть объекты с тегом "path" не опписывающие границы региона.
      continue
    try:
      value = float(statistic[region])
    except:
      flag_no_data = True
      if palett == 0:
        path.setAttribute("style", "")
        path.setAttribute("fill", "url(#hatching)")
        path.setAttribute("stroke", "black")
        path.setAttribute("stroke-width", "2")
      else:
        [r,g,b] = colors[0][2][3]
        style="fill: rgb(" + str(r) + ", " + str(g) + ", " + str(b) + "); fill-opacity: 1;"
        path.setAttribute("style", style)
      continue
    else:
      col = 0
      i = 0
      while i < match_band:
        if value >= bands[i][0] and value < bands[i][1]:
          col = i
          break
        i += 1
      [r,g,b] = colors[palett][match_band-4][col]
      style="fill: rgb(" + str(r) + ", " + str(g) + ", " + str(b) + "); fill-opacity: 1;"
      path.setAttribute("style", style)

  edit_legend(doc, bands, match_band, palett, flag_no_data)
  return doc.toprettyxml(encoding='utf-8')


def edit_legend(doc, bands, match_band, palett, flag_no_data):
  # Легенда.
  for path in doc.getElementsByTagName("rect"):
    ID = path.getAttribute("id")
    if int(ID) > match_band:
      if flag_no_data:
        if palett > 0:
          [r,g,b] = colors[0][2][3]
          style="fill: rgb(" + str(r) + ", " + str(g) + ", " + str(b) + "); fill-opacity: 1;"
          path.setAttribute("style", style)
        else:
          path.setAttribute("style", "")
          path.setAttribute("fill", "url(#hatching)")
          path.setAttribute("stroke", "black")
          path.setAttribute("stroke-width", "2")
      break
    [r,g,b] = colors[palett][match_band-4][int(ID)-1]
    style="fill: rgb(" + str(r) + ", " + str(g) + ", " + str(b) + "); fill-opacity: 1;"
    path.setAttribute("style", style)

  # Подпись легенды.
  for path in doc.getElementsByTagName("text"):
    ID = path.getAttribute("id")
    if int(ID) > match_band:
      if flag_no_data:
        path.setAttribute("style", "font-size: 30px; fill: rgb(0, 0, 0); fill-opacity: 1; font-family: Arial;")
        s = unicode( "Значение не задано", encoding='utf-8' )
        textnode = doc.createTextNode( s )
        path.appendChild(textnode)
      break
    path.setAttribute("style", "font-size: 30px; fill: rgb(0, 0, 0); fill-opacity: 1; font-family: Arial;")
    s = unicode( str(bands[ int(ID)-1 ][0]) + " - " + str(bands[int(ID)-1][1]) , encoding='utf-8' )
    textnode = doc.createTextNode( s )
    path.appendChild(textnode)


def save_svg_to_png(svg, file_name, image_width, image_height):
    """
        Конвертирует и сохраняет SVG в PNG.
    """
    img =  cairo.ImageSurface(cairo.FORMAT_ARGB32, image_width, image_height)
    ctx = cairo.Context(img)
    handler= rsvg.Handle(None, svg)
    handler.render_cairo(ctx)
    img.write_to_png(file_name)

