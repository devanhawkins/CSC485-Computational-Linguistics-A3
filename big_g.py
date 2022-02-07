import nltk
from nltk import parse_cfg
from nltk.parse import ChartParser, BU_STRATEGY
from nltk.parse import TestGrammar
from nltk import parse, draw

g_s='''
%start S
S -> NP[SEM=?c] VP[GAP_SEM=?c]

VP[GAP_SEM=?c] -> V NP[GAP_SEM=?c]

NP[SEM='cans'] -> 'cans'
V[SEM='kicked'] -> 'kicked'
NP[SEM=?c, GAP_SEM=?c] -> 

'''

g=nltk.parse_fcfg(g_s)

parser = parse.FeatureBottomUpLeftCornerChartParser(g)
tokens='cans kicked'.split()
trees = parser.nbest_parse(tokens)

#parser=ChartParser(g,BU_STRATEGY)
for t in trees:
	print t
	draw.draw_trees(t)
#for t in trees:
#	print t
