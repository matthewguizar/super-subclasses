from player import Player
from enemy import Enemy, Troll, Vampyre

matthew = Player("matthew")

#
# random_monster = Enemy("Basic Enemy", 12, 1)
# print(random_monster)
#
# random_monster.take_damage(4)
# print(random_monster)
#
# troll = Troll("ug")
# print(troll)
# troll.grunt()

#
# while troll.alive:
#     troll.take_damage(1)
#     print(troll)

vamp = Vampyre("joe")
# while vamp.alive:
#     vamp.take_damage(1)
    # print(vamp)
vamp.lives = 0
vamp.hit_points = 1
print(vamp)
