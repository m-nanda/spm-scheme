def tresholding_below(value_th, value_sensor):
  '''
  Function for tresholding value from sensor which sign is '<'
  
  Output:
  0 : Normal
  1 : Broken / Breakdown 
  '''
  if value_sensor < value_th:
    return 1
  return 0


def tresholding_upper(value_th, value_sensor):
  '''
  Function for tresholding value from sensor which sign is '>'
  
  Output:
  0 : Normal
  1 : Broken / Breakdown
  '''
  if value_sensor > value_th:
    return 1
  return 0


def tresholding_equalto(value_th, value_sensor):
  '''
  Function for tresholding value from sensor which sign is '=='
  
  Output:
  0 : Normal
  1 : Broken / Breakdown
  '''
  if value_sensor != value_th:
    return 1
  return 0


def generate_cp(col_series):
  '''
  This function is to generate feature representation
  changepoint (cp) of the input in the form of representation
  raw features. It will return the value '0'
  if the representation of the raw index feature at u-1 is the same
  at index u, besides that, will return the value '1'.

  Input:
    col_series: Series that contains a raw feature 
                representation that will be transformed 
                into a changepoint feature representation.
  
  Output:
    Raw features that have been transformed to 
    changepoint
  '''
  # list of data raw
  input_raw = col_series.values

  # initial state for cp
  output_cp = [0]
  
  # looping to transform raw feature to changepoint
  for u in range(1, len(input_raw)):
    if input_raw[u-1] == input_raw[u]:
      output_cp += [0]
    else:
      output_cp += [1]
  
  return output_cp


def change_state(s):
  if s==0:
    return 1
  return 0


def generate_lf(base_sensor, other_sensor):
  '''
  This function is to generate feature representation
  lastfired (lf) of the input in the form of representation
  raw features. 

  Input:
    col_series: Series that contains a raw feature 
                representation that will be transformed 
                into a lastfired feature representation.
  
  Output:
    Raw features that have been transformed to 
    lastfired
  '''
  # print(base_sensor, other_sensor)
  output_lf = [base_sensor[0]]    
  for i in range(1, len(base_sensor)):        

    # "any" or "all" ..?
    if base_sensor[i]!=base_sensor[i-1] or all(other_sensor[i]!=other_sensor[i-1]):
      output_lf += [change_state(output_lf[i-1])]
    else:
      output_lf += [output_lf[i-1]]
  return output_lf