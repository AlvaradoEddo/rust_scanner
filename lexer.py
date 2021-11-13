import ply.lex as lex


#APORTE EDDO
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
    'insert':'INSERT_HASH',
    'union':'UNION_HASH',
    'vec':'VECTOR',
    'push': 'PUSH_VEC',
    'pop':'POP_VEC',
    'contains':'CONTAINS_SLICE',
    'get':'GET_SLICE',
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
 
t_MAS               = r'\+'
t_MENOS             = r'-'
t_MULT              = r'\*'
t_DIVISION          = r'/'
t_MODULO            = r'%'
t_OR                = r'\|\|'
t_AND               = r'&&'
t_NOT               = r'!'
t_LESST             = r'<'
t_GREATER           = r'>'
t_LESSEQ            = r'<='
t_GREATEQ           = r'>='
t_EQUAL             = r'=='
t_DIFFERENT         = r'!='
t_ASIGNAR           = r'='
t_LPAREN            = r'\('
t_RPAREN            = r'\)' 
t_STRING            = r'\"[a-zA-Z0-9_]*\"'
t_U8                = r'(0?[0-9]?[0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5])'
t_ENDLINE           = r';'