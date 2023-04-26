

class Checker:
    def __init__(self, ui, board):
        self.ui = ui
        self.board = board
        self.revers = False

    def journal(self, args):
        data = self.board.get_all_notes()
        flags = {"-r": self.change_revers,
                 "-d": self.data_sort,
                 "-t": self.title_sort}
        if args[1] != '-r' and args[1].count('r'):
            self.change_revers()
            args[1] = args[1].replace('r', '')
        try:
            data = flags[args[1]](self.board.get_all_notes())
            self.ui.journal(data, self.revers)
            self.change_revers()
        except:
            self.ui.not_found(args[1:])

    def add(self, args):
        flags = {}
        double_flags = {}

    def delete(self, args):
        flags = {}
        double_flags = {}

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
