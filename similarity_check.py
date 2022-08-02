def diagnosis_pattern_kiln(val):
    '''
    Function to find diagnosis pattern in 2015
    
    Input:
    > a: Data Column in 2015
    
    Output:
    'Diagnosis Pattern'
    '''
    return str(val[1])+str(val[2])+str(val[3])+str(val[4])+str(val[5])+str(val[6])+str(val[7])
    
def diagnosis_pattern_rawmill(val):
    '''
    Function to find diagnosis pattern in 2015
    
    Input:
    > a: Data Column in 2015
    
    Output:
    'Diagnosis Pattern'
    '''
    return str(val[1])+str(val[2])+str(val[3])+str(val[4])+str(val[5])

def diagnosis_pattern_label(pattern, patterns): # label_dari_pola_diagnosis(col, list_pola_1):
    '''
    This function to change diagnosis condition base on data 2015
    
    Input:
    > col : diagnosis column
    > pattern_list : list pattern from a certain class
    
    Output:
    label / class. 0: Normal, 1: Broken
    '''
    if pattern in patterns: return 0
    return 1

def find_diagnosis_pattern(val):# cari_pola_diag(a):
    '''
    Function to find diagnosis pattern from some senors (in 2015)
    
    Input:
    > val: Data Column in 2015
    
    Output:
    'Diagnosis Pattern - Class'
    '''
    return str(val[1])+str(val[2])+str(val[3])+str(val[4])+str(val[5])+'-'+str(val[6])


def find_prognosis_pattern(val):
    '''
    Function to find prognosys pattern (in 2015)
    
    Input:
    > val: data column 2015
    
    Output:
    'prognosis pattern - class'
    '''    
    return str(val[1])+str(val[2])+str(val[3])+str(val[4])+str(val[5])+str(val[6])+'-'+str(val[7])

def prognosis_pattern(val):
    '''
    Function to build prognosis pattern in 2016
    
    Input:
    > val : data column 2016
    
    Output:
    'Prognosis pattern'
    '''
    return str(val[6])+str(val[7])+str(val[8])+str(val[9])+str(val[10])+str(val[11]) # need to verify


def diagnosis_pattern_label(col, pattern_list ): 
    '''
    Functin to change prognosis pattern based data 2015 (?)
    
    Input:
    > col : Prognosis column
    > pattern_list : list pattern from a certain class
    
    Output:
    label / class
    '''
    if col in pattern_list[:-2]: 
        return 1 
    return 0