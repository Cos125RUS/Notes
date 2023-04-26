

class Checker:
    def __init__(self, ui, board):
        self.ui = ui
        self.board = board
        self.revers = False

    def journal(self, args):
        flags = {"-r": self.change_revers,
                 "-d": self.data_sort,
                 "-t": self.title_sort}
        if args[1] != '-r' and args[1].count('r'):
            self.change_revers()
            args[1] = args[1].replace('r', '')
        if args[2].isdigit():
            size = int(args[2])
        try:
            data = flags[args[1]](self.board.get_all_notes())
            self.ui.journal(data, self.revers, size)
            self.change_revers()
        except:
            self.ui.not_found(args[1:])

    def add(self, args):
        res = {}
        double_flags = {"--title": self.ui.write_head,
                        "--msg": self.ui.write_body}
        catch = [flag for flag in double_flags if flag in args]
        if len(args) != len(catch) * 2 + 1:
            self.ui.no_args()
        elif len(catch):
            for item in catch:
                res[item] = self.take_value(args[args.index(item) + 1])
            for item in [flag for flag in double_flags if flag not in res.keys()]:
                res[item] = double_flags[item]()
            return res['--title'], res['--msg']

    def delete(self, args):
        flags = {"-i": 0,
                 "-n": 1,
                 "-h": 2}

    def show(self, args):
        flags = {}
        double_flags = {}

    def change(self, args):
        flags = {}
        double_flags = {}

    def change_revers(self, data=''):
        self.revers = True
        return data

    def data_sort(self, items):
        item_dict = {}
        for i in range(len(items)):
            item_dict[items[i].get_change_time()] = items[i]
        return [item_dict[i] for i in sorted(item_dict.keys())]

    def title_sort(self, items):
        item_dict = {}
        for i in range(len(items)):
            item_dict[items[i].get_head()] = items[i]
        return [item_dict[i] for i in sorted(item_dict.keys())]

    def take_value(self, value):
        if value[:1] == '"' and value[-1:] == '"':
            return value[1:-1]
        else:
            self.ui.fail()
            self.ui.no_quotes()
