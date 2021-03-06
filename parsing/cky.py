# CKY Parser
from cfg import CFG

import nltk
import itertools
import sys


class CKY():

    def display(self):
        print 'Table'
        for i, l in enumerate(self.cky_table):
            sys.stdout.write('|' + str(i))
        print
        for l in self.cky_table:
            sys.stdout.write('|:-:')
        print
        for line in self.cky_table:
            for cell in line:
                if not cell == []:
                    sys.stdout.write(str(cell) + '|')
                else:
                    sys.stdout.write('|')
            print

    def cky_parse(self, words, grammar):

        self.cky_table = []
        for j in range(0, len(words) + 1):
            table = []
            for i in range(0, len(words) + 1):
                table.append([])
            self.cky_table.append(table)

        # self.display()
        for j in range(1, len(words) + 1):
            self.cky_table[j - 1][j] = list(set([x
                                                 for x in grammar.return_rule([words[j - 1]])]))
            for i in range(j - 1, -1, -1):
                for k in range(i, j):
                    a = self.cky_table[i][k]
                    b = self.cky_table[k][j]

                    c = [grammar.return_rule(r)[0]
                         for r in itertools.product(a, b) if grammar.return_rule(r) != []]

                    self.cky_table[i][j] = self.cky_table[i][j] + c

        self.display()

if __name__ == '__main__':
    cfg = CFG('main.cfg')
    cky = CKY()

    cky.cky_parse(['the', 'large', 'can', 'can', 'hold', 'the', 'water'], cfg)
