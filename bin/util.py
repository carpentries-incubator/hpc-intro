import sys

class Reporter(object):
    '''Collect and report errors.'''

    def __init__(self, args):
        '''Constructor.'''

        super(Reporter, self).__init__()
        self.messages = []

    def check(self, condition, message):
        '''Append error if condition not met.'''

        if not condition:
            self.add(message)


    def add(self, message):
        '''Append error unilaterally.'''

        self.messages.append(message)


    def report(self, stream=sys.stdout):
        '''Report all messages.'''

        if not self.messages:
            return
        print('***', file=stream)
        for m in self.messages:
            print(m, file=stream)
