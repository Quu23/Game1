class Chara:
    #コンストラクタ
    def __init__(self,id,name):
        self.id = id
        self.name = name
class NomalChara(Chara):

    def __init__(self,id,name):
        super.__init__(id,name)

