class Game():
    top_score = 0 # 类属性
    count = 0 
    def __init__(self,player_name): # 实例属性，记录游戏玩家 
        self.name = player_name
        Game.count +=1
    @staticmethod
    def show_help(): # 静态方法，显示游戏信息
        print('帮助信息')
    @classmethod
    def show_top_score(cls): # 类方法
        print('最高分是{}'.format(Game.top_score))
        print('共有{}个玩家'.format(cls.count))
    def start_game(self): # 实例方法
        print('{}开始游戏'.format(self.name))
        Game.top_score = 100
game = Game('小明')
game.show_help()
game.start_game()
game.show_top_score()
