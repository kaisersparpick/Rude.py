class Rude(object):
    def __init__(self):
        self.rules = {}
        self.path = []

    def add_rule(self, condition, yes=None, no=None):
        self.rules[condition] = (condition, yes, no)

    def check_conditions(self, condition):
        self.path = []

        while(True):
            rule = self.rules.get(condition, None)
            if rule == None: break

            result = rule[0]()
            self.path.append((condition.__name__, result))

            if result is True:
                condition = rule[1]
            elif result is False:
                condition = rule[2]
            else:
                break

        return True

    def get_path(self):
        out = ''
        for p in self.path:
            if p[1] is False: out += '!'
            out += p[0]
            if p[1] is not None: out += ' > '

        return out
