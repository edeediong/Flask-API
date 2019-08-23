import ast

def api():
    '''This function calls the api key already pre-defined.'''
    api_key = input('Enter your API key:' )
    return api_key

def convert(t):
    '''This function converts the place_id column of the dataframe from a string to a list'''

    t = t.replace('""','')
    t = ast.literal_eval(t)
    return t