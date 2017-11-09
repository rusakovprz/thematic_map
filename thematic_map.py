# -*- coding: utf-8 -*-

from Tkinter import *
from tkMessageBox import *
from tkFileDialog  import *

from thematic_map_lib  import *

#=======================================================================================================================

def strToFloat( arg ):
  try:
    return float(arg)
  except:
    return 0

#=======================================================================================================================

def strToInt( arg ):
  try:
    return int(arg)
  except:
    return 0

#=========== GUI ============================================================================================================

class gui(Tk):
  def __init__(self):
    Tk.__init__(self)

    row_input_file = Frame(self)
    row_input_file.pack(side=TOP, fill=X)

    label_input_file_name = Label(row_input_file, text='Имя входного файла c данными')
    label_input_file_name .pack(side=LEFT, fill=X)

    self.entry_input_file_name = Entry(row_input_file,)
    self.entry_input_file_name.insert(0, "statistic.scv")
    self.entry_input_file_name.pack(side=LEFT, expand=YES, fill=X)

    button_set_input_file = Button(row_input_file,text='Выбрать файл', command = (lambda: self.get_input_file_name(self.entry_input_file_name)) )
    button_set_input_file.pack(side=RIGHT,fill=X)

    row_collor = Frame(self)
    row_collor.pack(side=TOP, fill=X)

    label_input_file_name = Label(row_collor, text='Укажите цветовую палитру')
    label_input_file_name .pack(side=LEFT, fill=X)

    self.current_color = StringVar()
    opt1 = OptionMenu(row_collor, self.current_color, "Градации серого","Оранжевый","Фиолетовый","Зелёный" )
    opt1.pack(side=LEFT, fill=X)
    self.current_color.set("Градации серого")

    row_band = Frame(self)
    row_band.pack(side=TOP, fill=X)

    label_input_file_name = Label(row_band, text='Укажите количество интервалов')
    label_input_file_name .pack(side=LEFT, fill=X)

    self.current_band = StringVar()
    opt1 = OptionMenu(row_band, self.current_band, 'Автоматически','4','5','6' )
    opt1.pack(side=LEFT, fill=X)
    self.current_band.set('Автоматически')

    frame_intervals = Frame(self)
    frame_intervals.pack(side=TOP, fill=X)
    frame_interval_header  = Frame(frame_intervals)
    frame_interval_header.pack(side=TOP, fill=X)
    frame_interval_1  = Frame(frame_intervals)
    frame_interval_1.pack(side=TOP, fill=X)
    frame_interval_2  = Frame(frame_intervals)
    frame_interval_2.pack(side=TOP, fill=X)
    frame_interval_3  = Frame(frame_intervals)
    frame_interval_3.pack(side=TOP, fill=X)
    frame_interval_4  = Frame(frame_intervals)
    frame_interval_4.pack(side=TOP, fill=X)
    frame_interval_5  = Frame(frame_intervals)
    frame_interval_5.pack(side=TOP, fill=X)
    frame_interval_6  = Frame(frame_intervals)
    frame_interval_6.pack(side=TOP, fill=X)

    Label(frame_interval_header, text='Интервалы').pack(side=LEFT)
    Label(frame_interval_header, text='от', width=15).pack(side=LEFT)
    Label(frame_interval_header, text='до', width=20).pack(side=LEFT)

    Label(frame_interval_1, text='Интервал 1').pack(side=LEFT)
    self.interval_1_from = Entry(frame_interval_1 )
    self.interval_1_from.pack(side=LEFT)
    self.interval_1_to   = Entry(frame_interval_1 )
    self.interval_1_to.pack(side=LEFT)

    Label(frame_interval_2, text='Интервал 2').pack(side=LEFT)
    self.interval_2_from = Entry(frame_interval_2 )
    self.interval_2_from.pack(side=LEFT)
    self.interval_2_to   = Entry(frame_interval_2 )
    self.interval_2_to.pack(side=LEFT)

    Label(frame_interval_3, text='Интервал 3').pack(side=LEFT)
    self.interval_3_from = Entry(frame_interval_3 )
    self.interval_3_from.pack(side=LEFT)
    self.interval_3_to   = Entry(frame_interval_3 )
    self.interval_3_to.pack(side=LEFT)

    Label(frame_interval_4, text='Интервал 4').pack(side=LEFT)
    self.interval_4_from = Entry(frame_interval_4 )
    self.interval_4_from.pack(side=LEFT)
    self.interval_4_to   = Entry(frame_interval_4 )
    self.interval_4_to.pack(side=LEFT)

    Label(frame_interval_5, text='Интервал 5').pack(side=LEFT)
    self.interval_5_from = Entry(frame_interval_5 )
    self.interval_5_from.pack(side=LEFT)
    self.interval_5_to   = Entry(frame_interval_5 )
    self.interval_5_to.pack(side=LEFT)

    Label(frame_interval_6, text='Интервал 6').pack(side=LEFT)
    self.interval_6_from = Entry(frame_interval_6 )
    self.interval_6_from.pack(side=LEFT)
    self.interval_6_to   = Entry(frame_interval_6 )
    self.interval_6_to.pack(side=LEFT)


    row_output_file = Frame(self)
    row_output_file.pack(side=TOP, fill=X)

    label_output_file_name = Label(row_output_file, text='Имя выходного файла с изображением')
    label_output_file_name.pack(side=LEFT, fill=X)

    self.entry_output_file_name = Entry(row_output_file)
    self.entry_output_file_name.insert(0, "image.png")
    self.entry_output_file_name.pack(side=LEFT, expand=YES, fill=X)

    button_set_output_file = Button(row_output_file,text='Выбрать файл', command = (lambda: self.get_output_file_name(self.entry_output_file_name)) )
    button_set_output_file.pack(side=RIGHT,fill=X)

    Button(self,text= 'Создать зображение', command =  (lambda: self.create_image() )).pack()

  def get_input_file_name(self, entry):
    entry.delete(0,500)
    entry.insert(0, askopenfilename())

  def get_output_file_name(self, entry):
    entry.delete(0,500)
    entry.insert(0, asksaveasfilename())

  def create_image(self):

    # Имя входного файла
    file_name_input = self.entry_input_file_name.get()
    # Цветовая палитра
    current_color = self.current_color.get()

    current_color_n = 0
    if current_color == u"Градации серого":
      current_color_n = 0
    if current_color == u"Оранжевый":
      current_color_n = 1
    if current_color == u"Фиолетовый":
      current_color_n = 2
    if current_color == u"Зелёный":
      current_color_n = 3

    # Количество интервалов
    current_band = strToInt(self.current_band.get())
    # Значения интервалов
    intervals = [
                 [strToFloat(self.interval_1_from.get()), strToFloat(self.interval_1_to.get())],
                 [strToFloat(self.interval_2_from.get()), strToFloat(self.interval_2_to.get())],
                 [strToFloat(self.interval_3_from.get()), strToFloat(self.interval_3_to.get())],
                 [strToFloat(self.interval_4_from.get()), strToFloat(self.interval_4_to.get())],
                 [strToFloat(self.interval_5_from.get()), strToFloat(self.interval_5_to.get())],
                 [strToFloat(self.interval_6_from.get()), strToFloat(self.interval_6_to.get())]]
    # Имя выходного файла
    file_name_output = self.entry_output_file_name.get()

    # Читаем и парсим SCV файл
    statistic = read_and_parse_csv(file_name_input)

    # Загружаем  SVG файл c границами регионов
    file_name_regions = 'RF_Regions.svg'

    try:
      svg_code = open(file_name_regions, 'r').read()
    except:
      showerror("Ошибка", "Не найден файл '" + file_name_regions + "'.")
      return

    # Проверяем и подготавливаем данные (интервалы значений для автоматического режима)
    if current_band == 0:
       current_band = 5
       intervals = []
       (min_value, max_value) = get_min_max_values( statistic.values() )

       step = (max_value - min_value)/5
       intervals = [
                 [min_value, min_value+step],
                 [min_value+step, min_value+step*2],
                 [min_value+step*2, min_value+step*3],
                 [min_value+step*3, min_value+step*4],
                 [min_value+step*4, min_value+step*5,]]

    # Редактируем SVG файл
    ret_svg = edit_svg(svg_code, statistic, current_band, intervals, current_color_n)

    # Конвертируем SVG в PNG
    img =  cairo.ImageSurface(cairo.FORMAT_ARGB32, 1700,1050)
    ctx = cairo.Context(img)
    handler= rsvg.Handle(None, ret_svg)
    handler.render_cairo(ctx)
    img.write_to_png(file_name_output)

if __name__ == '__main__':
  gui().mainloop()      # запустить цикл событий

