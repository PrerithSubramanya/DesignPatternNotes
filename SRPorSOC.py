class Journal:
    """Demonstration of single responsibility pattern or separation of concerns"""
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def rm_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)


'''the below two methods are additional methods that might get changed and does not relate to the functionality of the 
     journal, hence can be moved as separate class methods'''
#
# def save_journal(self, filename):
#     with open(filename, 'w') as f:
#         f.write(str(self))
#
# def load_journal(self, filename):
#     with open(filename, 'r') as f:
#         print(f.read())


""" Functionality separate class adds more flexibility and separation from journal class to make any further changes to the file
 load and save methods"""


class Functionality:
    @staticmethod
    def save_journal(journal, filename):
        with open(filename, 'w') as f:
            f.write(str(journal))

    @staticmethod
    def load_journal(filename):
        with open(filename, 'r') as f:
            print(f.read())


j1 = Journal()
j1.add_entry('Lets get going')
j1.add_entry('Its time to get serious')
print(j1)

func = Functionality()
func.save_journal(j1, 'journalOne')
func.load_journal('journalOne')
