# Name:                 Joe Lavond
# Course:               CPE 101
# Intructor:            Daniel Kauffman
# Assignment:           Crime Time
# Term:                 Spring 2017




def main():
    lines = str_data("crimes.tsv")
    times = str_data("times.tsv")
    crimes = create_crimes(lines)
    num_rob = len(crimes)
    sor_crimes = sort_crimes(crimes)



def str_data(file):
    db = open(file, "r")
    first_line = db.readline() # get rid of header
    list_lines = db.readlines()
    list_lines2 = []
    for lines in list_lines:
        lines = lines.split("\t")
        list_lines2.append(lines)        
    db.close()    
    return list_lines2


class Crime:

    def __init__(self, crime_id, category):
        self.id = crime_id
        self.category = category
        self.day_of_week = None
        self.month = None
        self.hour = None

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return ("Crime ID: {} Category: {} Day of the Week: {} Month: {} "
        "Hour: {}".format(self.id, self.category, self.day_of_week, 
        self.month, self.hour))

    def set_time(self, day_of_week, month, hour):
        pass


def create_crimes(lines):
    lines = [i for i in lines if i[1] == "ROBBERY"]
    all_robberies = []
    added_crime_nums = []
    for crime in lines: 
        crime_num = crime[0]
        crime_type = crime[1]
        if crime_num not in added_crime_nums:
            added_crime_nums.append(crime_num)
            cur_crime = [crime_num, crime_type]
            all_robberies.append(cur_crime)
    crimes = [Crime(int(item[0]), item[1]) for item in all_robberies]
    return crimes


# figuring out how to selection sort
#def sort_lst(lst):
#    sorted_lst = []
#    while len(lst) > 0:
#        small = min(lst)
#        loc = lst.index(small)
#        sorted_lst.append(lst[loc])
#        lst.remove(small)
#    return sorted_lst
    

def sort_crimes(crimes):
    sorted_id = []
    while len(crimes) > 0:
        id_left = [i.id for i in crimes] # list of id's
        smallest = min(id_left)
        loc_small = id_left.index(smallest)
        sorted_id.append(crimes[loc_small])
        crimes.remove(crimes[loc_small])
    return sorted_id
        

def update_crimes(crimes, lines):
    pass


def find_crime(crimes, crime_id):
    print(crime_id)
    low = 0
    high = (len(crimes) - 1)
    not_found = True
    while not_found:
        mid = ((low + high) // 2)
        value = crimes[mid].id
        print(value)
        if value == crime_id:
            return crimes[mid]
        elif value < crime_id:
            low = mid + 1
        else:
            high = mid - 1


# figuring out binary search
def binary(lst, num):
    print(num)
    low = 0
    high = len(lst) - 1
    not_found = True
    while not_found:
        mid = (low + high) // 2
        print(lst[mid])
        if lst[mid] == num:
            return mid
        elif num > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
    

def crime_output(num_rob, freq_day, freq_mon, freq_hr):
    cat = "ROBBERIES:"
    print("NUMBER OF PROCESSED {} {}").format(cat, num_rob)
    print("DAY WIHT MOST {} {}").format(cat, freq_day)
    print("MONTH WITH MOST {} {}").format(cat, freq_mon)
    print("HOUR WITH MOST {} {}").format(cat, freq_hour)

    

if __name__ == "__main__":
    main()
