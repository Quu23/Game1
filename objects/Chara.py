class Chara:
    #あらゆる生き物
    def __init__(self,id,name):
        self.id = id
        self.name = name

class NomalChara(Chara):
    #村人など　戦わない生き物
    def __init__(self,id,name):
        super().__init__(id,name)

class ButtleChara(Chara):
    #戦う生き物　魔物、主人公
    def __init__(self, id, name):
        super().__init__(id, name)

