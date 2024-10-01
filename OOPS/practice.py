class Spam:
    __ham,ham='__ham','ham'
    def __eggs(self):pass
    eggs=__eggs
s=Spam()
print(type(s._Spam__eggs).__name__)