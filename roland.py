import ast

def api():
    '''This function calls the api key already pre-defined.'''
    api_key = 'AIzaSyAb0qDYFKw-0-S2X9WkpUebpnMRdXu5WMI'
    return api_key

def convert(t):
    '''This function converts the place_id column of the dataframe from a string to a list'''

    t = t.replace('""','')
    t = ast.literal_eval(t)
    return t