import constants
from graphtaint import getYAMLFiles

def fuzzGetYAMLFiles():
    try:
        getYAMLFiles("田中さんにあげて下さい")
    except Exception as e:
        print(e)
        print(e.args)
