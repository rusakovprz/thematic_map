# -*- coding: utf-8 -*-


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

