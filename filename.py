def filename(FILE):
'''
FILE - string
takes file name with its location as copied from windows and replaces ambiguous characters
'''
    FILE = FILE.replace('\\','/')
    FILE = FILE.replace('\r','/r')
    FILE = FILE.replace('\t','/t')
    FILE = FILE.replace('\f','/f')
     FILE = FILE.replace('\f','/n')
    return FILE
