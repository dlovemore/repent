from parle.parse import *

ab='abcdefghijklmnopqrstuvwxyz'
AB=ab.upper()
alphabet=ab+AB
digits='0123456789'
hexdigits=digits+'abcdefABCDEF'
opchar='~!%^&*-+=[];:()|/?.<>'
otherchar='$'
filechar=alphabet+digits+opchar+otherchar+' '
anychar=alphabet+digits+opchar+otherchar+' \t\n'

alpha=either(alphabet)
alphanum=either(AB+ab+digits)
digit=either(digits)
hexdigit=either(hexdigits)

ident=cat(alpha, anytimes(alphanum))
num=many(digit)
hexnum=cats([match('0'),either('xX'),many(hexdigit)])
op=either(opchar)
comment=cat(matches('/*'),mintimes(either(anychar)),matches('*/'))
sws=anytimes(either(' \t'))
ws=cut(anytimes(alt(match('\n'),sws)))
nl=match('\n')
hashe=match('#')
filename=mintimes(either(filechar))
includefile=alt(cat(match('"'),filename,match('"')),cat(match('<'),filename,match('>')))
hashcommands=cat(matches('include'),sws,includefile,sws,nl)
hashcommand=cat(match('#'),sws,hashcommands)

# >>> from parle import *
# >>> from lexer import *
# >>> pall(maybe(match('x'))(''))
# [[]]
# >>> 
# >>> pall(comment('/* abc */ 456 */'))
# [['/', '*', ' ', 'a', 'b', 'c', ' ', '*', '/'], ['/', '*', ' ', 'a', 'b', 'c', ' ', '*', '/', ' ', '4', '5', '6', ' ', '*', '/']]
# >>> pone(ident('abc1+abc'))
# ['a', 'b', 'c', '1']
# >>> pone(num('123'))
# ['1', '2', '3']
# >>> pone(op('+1'))
# ['+']
# >>> pone(op('++1'))
# ['+']
# >>> pone(ws('   '))
# [' ', ' ', ' ']
# >>> pone(ws('   \n  1'))
# [' ', ' ', ' ', '\n', ' ', ' ']
# >>> pone(nl('\n  1'))
# ['\n']
# >>> pone(hexnum('0xABC1g'))
# ['0', 'x', 'A', 'B', 'C', '1']
# >>> 
