chain = {'A': 'start', 'B': 'A', 'end': 'B', '-': 'end'}


def parse_chain(key):
    if chain[key] == 'start':
        return 'start'
    return parse_chain(chain[key]) + ' ' + chain[key]

print(parse_chain('-'))
