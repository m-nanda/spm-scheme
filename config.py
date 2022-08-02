# Directory
HOME_DIR = ''
DIR = {
  'BASE': f'{HOME_DIR}\\ OneDrive - Institut Teknologi Sepuluh Nopember\\Project-Paper\\Data\\',
  'RAW_DATA': f'{HOME_DIR}\\Project-Paper\\Data\\raw_data\\',
  'PREPROCESSING_DATA': f'{HOME_DIR}\\Project-Paper\\Data\\preprocessing\\',
  'DATA_INPUT_TO_MODEL': f'{HOME_DIR}\\Project-Paper\\Data\\input_to_model\\',
  'DATA_SCDS': f'{HOME_DIR}\\Project-Paper\Data\\scds\\',
  'ALL_DATA': f'{HOME_DIR}\\Project-Paper\\Data\\all_data\\',
  'TRESHOLD': f'{HOME_DIR}\\Project-Paper\\asoc\Info\\treshold.xlsx',
  'RESULT': f'{HOME_DIR}\\Project-Paper\\Result\\',
  'LOG': f'{HOME_DIR}\\Project-Paper\\Result\\log\\',
  'PLOT': f'{HOME_DIR}\\Project-Paper\Result\\plot\\',
  'PLOT_METRIC': f'{HOME_DIR}\\Project-Paper\\Result\\plot_metric\\'
}
HOME_GDRIVE = ''
DIR_GDRIVE = {
  'BASE': f'{HOME_GDRIVE}/Project-Paper',
  'DATA_INPUT_TO_MODEL': f'{HOME_GDRIVE}/Project-Paper',
  'DATA_SCDS': f'{HOME_GDRIVE}/Project-Paper/Data/scds',
  'RESULT': f'{HOME_GDRIVE}/Project-Paper/Result',
  'LOG': f'{HOME_GDRIVE}/Project-Paper/Result/log',
  'PLOT': f'{HOME_GDRIVE}/Project-Paper/Result/plot'
}

MACHINES = ['kiln', 'rawmill']

TS = ['10s', '30s', '60s', '90s']

FEATURE_REPRESENTATION = ['raw', 'changepoint', 'lastfired']

PROCESS = ['diag', 'prog']

KILN_SENSORS= {
  'Tanggal dan Waktu': 'Timestamp',
  'Sensor-1': '533FN01U01S01',
  'Sensor-2': '533FN02U01S01',
  'Sensor-3': '533FN03U01S01',
  'Sensor-4': '541KF01A01F01X01',
  'Sensor-5': '542CL01N03T01',
  'Sensor-6': '543MD01U01S01',
  'Sensor-7': '545RL03A01F01',
}

KILN_SENSOR_NAMES= {
  'Tanggal dan Waktu': 'Timestamp',
  'Sensor-1': 'Rotary Speed 1', 
  'Sensor-2': 'Rotary Speed 2', 
  'Sensor-3': 'Rotary Speed 3', 
  'Sensor-4': 'Feeder 1',
  'Sensor-5': 'Temperature',
  'Sensor-6': 'Rotary Speed 4', 
  'Sensor-7': 'Feeder 2',
}

RAWMILL_SENSORS={
  'Tanggal dan Waktu': 'Timestamp',
  'Sensor RPM 1'  : '532BC02M01I01', 
  'Sensor Tekanan': '532FN02N01P01', 
  'Sensor RPM 2'  : '531BI01N01L01', 
  'Sensor RPM 3'  : '531BI04N01L01', 
  'Sensor Vibrasi': '532RM01N06V01' 
}

RAWMILL_SENSOR_NAMES = {
  'Tanggal dan Waktu': 'Timestamp',
  'Sensor RPM 1'  : 'Rotary'
  'Sensor Tekanan': 'Pressure Sensor', 
  'Sensor RPM 2'  : 'Rotary Speed 2'
  'Sensor RPM 3'  : 'Rotary Speed 3' 
  'Sensor Vibrasi': 'Vibration' 
}

IDX_DF = {'Tanggal dan Waktu': 'Timestamp'}

KILN_CONDITION = [
  # 0: Normal | 1: Normal
  '0001100', #| '1110011',
  '0001000', #| '1110111',
  '0000100', #| '1111011',
  '0000001', #| '1111110',
  '0000000', #| '1111111',
]

RAWMILL_CONDITION = [
  # 0: Normal | 1: Normal
  '00101',   #| '11010',
  '00100',   #| '11011',
  '00001',   #| '11110',
  '00000',   #| '11111',
  ]