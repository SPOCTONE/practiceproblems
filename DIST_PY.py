import math
 
 
def compute_distance(x1, y1, x2, y2):
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    print("Distance: "+" {:.2f}".format(distance))
 
 
if __name__ == '__main__':
    test_cases = int(input("Enter the no. of test cases you want: "))
    i = 0
    while (i < test_cases):
        coordinates = []
        coordinates = list(map(int, input("Enter x1,y1,x2,y2 in that order: ").split()))
        x1 = coordinates[0]
        y1 = coordinates[1]
        x2 = coordinates[2]
        y2 = coordinates[3]
        i += 1
        compute_distance(x1, y1, x2, y2)
 