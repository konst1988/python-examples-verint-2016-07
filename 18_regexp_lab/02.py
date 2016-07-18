"""
Write a function toCamelCase(text) that returns the text camel cased
Write a function to_underscore(text) that returns the text with 
underscores between words
"""
import re

def toCamelCase(text):
    return re.sub(r'_(\w)',
        lambda m: m.group(1).upper()
        , text)

print toCamelCase('welcome')
print toCamelCase('hello_world')
print toCamelCase('get_name')
print toCamelCase('no_more_shall_we_part')
