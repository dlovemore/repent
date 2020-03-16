from parle.parse import *

ab='abcdefghijklmnopqrstuvwxyz'
AB=ab.upper()
alphabet=ab+AB
digits='0123456789'
opchar='~!%^&*-+=[];:()|/?'
anychar=alphabet+digits+opchar+' \t\n'

alpha=either(AB+ab)
alphanum=either(AB+ab+digits)

ident=cat(alpha, digits)
op=either(opchar)
comment=cats([matches('/*'),mintimes(either(anychar)),matches('*/')])
ws=anytimes(alts(matches('\\\n'),either(' \t')))
nl=match('\n')
hashe=match('#')

# >>> from parle import *
# >>> from lexer import *
# >>> 
