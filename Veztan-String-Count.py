#!/usr/bin/env python
"""Veztan-String-Count.py"""
String = 'The new patients were an 18-year-old female student who returned from Britain on Friday, and a 61-year-old man whose granddaughter and domestic helper was infected previously, according to Dr Chuang Shuk-kwan, head of the Centre for Health Protection’s communicable disease branch.'

def NaiveCount(str):
    dictrecord = {}
    record = []
    for char in str:
        if char in dictrecord:
            dictrecord[char] += 1
        else:
            dictrecord[char] = 1
    #convert dict to list to match output format
    for key in dictrecord:
        temp = [key, dictrecord[key]]
        record.append(temp)
    return record

def ListMethodCount(str):
    #get a list of unique char in str
    record = list(dict.fromkeys(str))
    #count occurence for each unqie char
    for i in range(len(record)):
        occurence = str.count(record[i])
        record[i] = list(record[i])
        record[i].append(occurence)
    return record

def SortCount(str):
    #sort the list
    sorted_char = sorted(str)
    str = "".join(sorted_char)
    record = [[str[0], 1]]
    current = 0
    #count occurence
    for i in range(1, len(str)):
        if str[i] == str[i-1]:
            record[current][1] += 1
        else:
            record.append([str[i], 1])
            current += 1
    return record

print(NaiveCount(String))
print(ListMethodCount(String))
print(SortCount(String))
