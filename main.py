"""
1.Read file input.txt - complete
2.Parse lines with .split to separate room type from dimensions - complete
3.First create simple class room that should have fields for size, periodic number and a method to get surface in sq.m. and perimeter in meters as float - complete
4.Put all rooms from file into python list where each item is a instance of this class  - complete
5.While reading line - count number of room to save it as object property  - complete
6.Store sizes in millimeters. But dont forget to compute floor surface as square meters, not meters - complete
7.Add extra check that total appartment size do not exceed size of rooms - complete
8.Compute and store into output list extra space used by hall and corridors 
9.Output formated information about apartment, each room and it's purpose and some extra statiscics (like wall perimiter, average size, number of bathrooms and etc)
"""


class Room:

  def __init__(self, p_num, name, size):
    self.p_number = p_num
    self.name = name
    self.size = size
    self.x, self.y = size.split('x')

  def perimeter(self):
    return 2 * (float(self.x) / 1000 + float(self.y) / 1000)

  def square_meters(self):
    return float(self.x) / 1000 * float(self.y) / 1000

  def __str__(self):
    out = "room_number: " + str(
        self.p_number) + "\r\nroom purpose: " + self.name + "\r\n"
    out += "size: " + self.size + "\r\n"
    return out


def print_stat(room_list):
  r_count = len(room_list)
  x_sum = 0
  y_sum = 0
  stat_room = {}
  per_total = 0
  for r in room_list:
    x_sum += int(r.x)
    y_sum += int(r.y)
    if r.name in stat_room:
      stat_room[r.name] += 1
    else:
      stat_room[r.name] = 1
    per_total += r.perimeter()

  print("total rooms: " + str(r_count))
  print("wall_perimeter: " + str(per_total))
  print("average room size: " + str(int(round(x_sum / r_count, 0))) + "x" +
        str(int(round(y_sum / r_count, 0))))

  for key in stat_room.keys():
    print("Room " + key + " count: " + str(stat_room[key]))


#data = open("input.txt","r").read()
room_list = []
sq_total = 0
sq_total_calc = 0
with open("input.txt", "rt") as f:
  for line in f.readlines():
    room, size = line.split(':')
    #print(room, size)
    if room == 'total':
      sq_total = size.replace("sqm", "")
    else:
      room_tmp = Room(len(room_list), room, size)
      print(room_tmp)
      room_list.append(room_tmp)
      sq_total_calc += room_tmp.square_meters()

print("SQ total: ", sq_total)
print("SQ rooms calculated: ", round(sq_total_calc, 1))

if sq_total_calc > float(sq_total):
  print("Total size of rooms exceeds apartment size")
else:
  print("Total size of rooms does not exceeds apartment size")
  extra_space = round(float(sq_total) - sq_total_calc, 1)
  print("extra space", extra_space)

print("---------------")
print_stat(room_list)
'''
room_list.append(
    Room(len(room_list), "extra_space",
         float(sq_total) - sq_total_calc))
'''
