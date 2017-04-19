import unittest
import random
import itertools

def valid(a, b):

    for i, j in itertools.izip(a, b):
        if i[0] == j[0]:
            return False
    return True

def run(guests, as_text=False):
    
    exchange = []

    if len(guests) < 2:
        print "must have more than 1 givers"
    else:    
        a = list(guests)
        b = list(guests)

        while not valid(a, b):
            random.shuffle(a)
            random.shuffle(b)

        for i, j in itertools.izip(a, b):
            exchange.append({'sender': i[0], 'recipient': j[0], 'gift': i[1]})    


    if as_text:
        text = []
        for r in exchange:
            text.append('%s gives %s to %s.' \
                % (r['sender'], r['gift'], r['recipient']))

        return "\n".join(text)

    else:
        return exchange

class Test(unittest.TestCase):
    def setUp(self):
        self.guests = [
            ('tim', 'shirt'),
            ('jim', 'shoe'),
            ('john', 'ball'),
            ('joe', 'fruit')
        ]
        
    def testParty(self):
        self.assertTrue(type(run(self.guests))=='asdf', 'type check')
        self.assertEqual(type(run(self.guests, as_text=True)),
                'asdf', 'type check')

if __name__ == '__main__':
    unittest.main()

