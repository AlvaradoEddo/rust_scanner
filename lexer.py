import ply.lex as lex


# APORTE EDDO
reserved = {
    'let': 'LET',
    'mut': 'MUT',
    'type': 'TYPE',
    'struct': 'STRUCT',
    'fn': 'FUNCTION',
    'return': 'RETURN',
    'true': 'B_TRUE',
    'false': 'B_FALSE',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'as': 'AS',
    'loop': 'LOOP',
    'pub': 'PUB',
    'static': 'STATIC',
    'async': 'ASYNC',
    'break': 'BREAK',
    'enum': 'ENUM',
    'match': 'MATCH',
    'ref': 'REF',
    'unsafe': 'UNSAFE',
    'await': 'AWAIT',
    'const': 'CONST',
    'extern': 'EXTERN',
    'impl': 'IMPL',
    'mod': 'MOD',
    'super': 'SUPER',
    'use': 'USE',
    'dyn': 'DYN',
    'continue': 'CONTIN',
    'in': 'IN',
    'move': 'MOVE',
    'self': 'SELFLOWERCASE',
    'Self': 'SELF',
    'trait': 'TRAIT',
    'where': 'WHERE',
    'crate': 'CRATE',
    'Hashset': 'HASHSET',
    'insert': 'INSERT_HASH',
    'union': 'UNION_HASH',
    'vec': 'VECTOR',
    'push': 'PUSH_VEC',
    'pop': 'POP_VEC',
    'contains': 'CONTAINS_SLICE',
    'get': 'GET_SLICE',
    'println': 'PRINT',
}
'''
Jaime's contribution 
Tokens and regular expressions (regex) for simple tokens
'''

tokens = (
    'NUMBER',
    'MAS',
    'MENOS',
    'MULT',
    'DIVISION',
    'MODULO',
    'OR',
    'AND',
    'NOT',
    'LESST',
    'GREATER',
    'LESSEQ',
    'GREATEQ',
    'EQUAL',
    'DIFFERENT',
    'LPAREN',
    'RPAREN',
    'MAYOR',
    'MAYORIGUAL',
    'ASIGNAR',
    'DATATYPE',
    'VARIABLE',
    'STRING',
    'NUMDATATYPES',
    'U8',
    'ENDLINE'
) + tuple(reserved.values())

t_MAS = r'\+'
t_MENOS = r'-'
t_MULT = r'\*'
t_DIVISION = r'/'
t_MODULO = r'%'
t_OR = r'\|\|'
t_AND = r'&&'
t_NOT = r'!'
t_LESST = r'<'
t_GREATER = r'>'
t_LESSEQ = r'<='
t_GREATEQ = r'>='
t_EQUAL = r'=='
t_DIFFERENT = r'!='
t_ASIGNAR = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_STRING = r'\"[a-zA-Z0-9_]*\"'
t_U8 = r'(0?[0-9]?[0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5])'
t_ENDLINE = r';'

'''
Joangie's contribution 
Tests and rules for the lexer
'''

# These are not tokens but they need to be ignored by the lexer


def t_COMMENT_SIMPLE(t):
    r'//(.*?)\n'
    pass


def t_COMMENT_DOUBLE(t):
    r'/\*'
    pass


def t_WHITESPACE(t):
    r'\s+'
    pass

# Included on symbols and special characters this might change later jajaja -Joangie


def t_ARROW(t):
    r'->'
    return t

# define a rule so we can track line numbers


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_NUMDATATYPES(t):
    r'u8 | u16 | u32 | u64 | i8 | i16 | i32 | i64'
    return t


def t_VARIABLE(t):
    r'([a-z]+[A-Z]*)|(_[a-z]+[A-Z]*[0-9]*[a-zA-Z]*)'
    print(t.value)
    t.type = reserved.get(t.value, 'VARIABLE')
    return t

   # Error handling rule


def t_error(t):
    print("Componente léxico no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

# Test it out
data = '''
 
let mut x = 10;
let mut y = 20;
let mut z: u8 = x + y;
_x2 = x + y;


'''
# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
