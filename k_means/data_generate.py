
import random
data_file = open("data.txt", "w")
list_pos = []
for x in range(100):
    pos_x = random.randint(0, 200)
    pos_y = random.randint(0, 200)
    pos = "%d,%d\n" % (pos_x, pos_y)
    list_pos.append(pos)

data_file.writelines(list_pos)