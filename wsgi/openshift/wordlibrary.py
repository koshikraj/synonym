def find_synonyms(syn):
    synonyms_list = []
    for line in syn:
        synonyms_list.append([i.strip('\n') for i in line.split(',')])
    return synonyms_list
 
def find_antonyms(ant):
    antonyms_list = []
    for line in ant:
        antonyms_list.append([i.strip('\n') for i in line.split(',')])
    return antonyms_list 

def read_para(par):
    return par.read().split('.')[:-1]

def read_line(para):
    return [i.strip('.') for i in para.split('\n')]

def GetAllwords(word_string):
    re.findall("([\w])[' ']",word_string)

def GetNumOccurances(word_string, syn):
    return word_string.count(syn)




