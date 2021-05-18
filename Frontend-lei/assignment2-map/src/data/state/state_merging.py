# -*- coding: utf-8 -*-
"""
Created on Sat May 15 16:25:09 2021

@author: lei chen
"""
import json
with open('AUS_state.json', 'w') as outfile:
    dict_format = {
            'features' : []
            }
    
    fp = open('NT_state.json', 'r')
    json_object = json.load(fp)
    for i in json_object['features']:
        dict_format['features'].append(i)
    fp.close()
    
    ## vic
    fp = open('VIC_state.json', 'r')
    json_object = json.load(fp)
    for i in json_object['features']:
        dict_format['features'].append(i)
    fp.close()
    
    ## qld
    fp = open('QLD_state.json', 'r')
    json_object = json.load(fp)
    for i in json_object['features']:
        dict_format['features'].append(i)
    fp.close()
    
    ## sa
    fp = open('SA_state.json', 'r')
    json_object = json.load(fp)
    for i in json_object['features']:
        dict_format['features'].append(i)
    fp.close()
    
    ## nsw
    fp = open('NSW_state.json', 'r')
    json_object = json.load(fp)
    for i in json_object['features']:
        dict_format['features'].append(i)
    fp.close()
    
    ## act
    fp = open('ACT_state.json', 'r')
    json_object = json.load(fp)
    for i in json_object['features']:
        dict_format['features'].append(i)
    fp.close()
    
    ## wa
    fp = open('WA_state.json', 'r')
    json_object = json.load(fp)
    for i in json_object['features']:
        dict_format['features'].append(i)
    fp.close()
    
    json.dump(dict_format, outfile)    
    print(len(dict_format['features']))