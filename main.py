from player import Player
from enemy import Enemy, Troll

matthew = Player("matthew")


random_monster = Enemy("Basic Enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

troll = Troll("ug")
print(troll)
troll.grunt()
