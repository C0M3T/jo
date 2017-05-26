# Name:                 Joe Lavond
# Course:               CPE 101
# Intructor:            Daniel Kauffman
# Assignment:           Crime Time
# Term:                 Spring 2017



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
        return ("{}\t{}\t{}\t{}\t{}".format(self.id, self.category, self.day_of_week, 
        self.month, self.hour))

    def set_time(self, day_of_week, month, hour):
        self.day_of_week = day_of_week
        months = ["January", "February", "March", "April", "May", "June", 
            "July", "August", "September", "October", "November", "December"]
        month -= 1
        self.month = months[month]
        pt_day = "AM"
        hours_half_day = 12
        if hour > hours_half_day:
            pt_day = "PM"
            hour -= hours_half_day
        hour = str(hour) + pt_day
        self.hour = hour


def main():
    lines = str_data("crimes.tsv")
    times = str_data("times.tsv")
    crimes = create_crimes(lines)
    num_rob = len(crimes)
    sor_crimes = sort_crimes(crimes)
    up_crimes = update_crimes(sor_crimes, times)
    print(len(up_crimes)) # Why only 17 crimes remaining!!!
    day = find_day(up_crimes)
    month = find_month(up_crimes)
    hour = find_hour(up_crimes)
    crime_output(num_rob, day, month, hour)

    print(len(sor_crimes))
    for i in range(len(sor_crimes) - 1):
        if sor_crimes[i].id  >= sor_crimes[i + 1].id:
            print(i)

#    a = [i.id for i in sor_crimes]
#    b = [int(i[0]) for i in lines]
#    checks = 0
#    for num in a:
#        if num in b:
#            checks += 1
#    print(checks)
        
    
    

def str_data(file):
    db = open(file, "r")
    first_line = db.readline() # get rid of header
    list_lines = db.readlines()
    list_lines2 = []
    for lines in list_lines:
        lines = lines.split()
        list_lines2.append(lines)        
    db.close()    
    return list_lines2


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


def sort_crimes(crimes):
    sorted_id = []
    ids = [i.id for i in crimes] # list of id's
    while len(crimes) > 0:
        smallest = min(ids)
        loc_small = ids.index(smallest)
        sorted_id.append(crimes[loc_small])
        crimes.remove(crimes[loc_small])
        ids.remove(ids[loc_small])
    return sorted_id
        

def update_crimes(crimes, lines):
    up_crimes = []
    checks = 0
    for line in lines:
        my_id = line[0]
        day = line[1]
        month_lst = line[2].split("/")
        num_month = int(month_lst[0])
        hour_lst = line[3].split(":")
        num_hour = int(hour_lst[0]) 
#        crime_obj = lin_search(crimes, my_id)
        crime_obj = find_crime(crimes, my_id)
        if crime_obj is not None:
            checks += 1
            tbu = [day, num_month, num_hour]
            crime_obj.set_time(day, num_month, num_hour)
            up_crimes.append(crime_obj)
    print(checks)
    return up_crimes
             

def lin_search(crimes, crime_id):
    crime_id = int(crime_id)
    min_rob = crimes[0].id
    max_rob = crimes[-1].id
    if crime_id < min_rob or crime_id > max_rob:
        return None
    lst_ids = [i.id for i in crimes]
    if crime_id not in lst_ids:
        return None
    index = lst_ids.index(crime_id)
    return crimes[index]    

def find_crime(crimes, crime_id):
    crime_id = int(crime_id)
#    min_rob = crimes[0].id
#    max_rob = crimes[-1].id
#    if crime_id < min_rob or crime_id > max_rob:
#        return None
    low = 0
    high = (len(crimes) - 1)
    while True:
        mid = ((low + high) // 2)
        value = crimes[mid].id
        if value == crime_id:
            return crimes[mid]
        elif (high - low) <= 0:
            return None
        elif value < crime_id:
            low = mid + 1
        high = mid - 1


def crime_output(num_rob, freq_day, freq_mon, freq_hour):
    cat = "ROBBERIES:"
    print("NUMBER OF PROCESSED {} {}".format(cat, num_rob))
    print("DAY WITH MOST {} {}".format(cat, freq_day))
    print("MONTH WITH MOST {} {}".format(cat, freq_mon))
    print("HOUR WITH MOST {} {}".format(cat, freq_hour))


def find_day(up_crimes):
    days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
        "Saturday", "Sunday"]
    crime_days = [i.day_of_week for i in up_crimes]
    day_counts = []
    for days in days_of_the_week:
        if days not in crime_days:
            day_counts.append(0)
        else:
            freq = crime_days.count(days)
            day_counts.append(freq)
    big_val = max(day_counts)
    val_loc = day_counts.index(big_val)
    name_day = days_of_the_week[val_loc]
    return name_day


def find_month(up_crimes):
    months_year = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"]
    crime_months = [i.month for i in up_crimes]
    month_counts = []
    for months in months_year:
        if months not in crime_months:
            month_counts.append(0)
        else:
            freq = crime_months.count(months)
            month_counts.append(freq)
    month_max = max(month_counts)
    month_index = month_counts.index(month_max)
    name_month = months_year[month_index]
    return name_month


def find_hour(up_crimes):
    hours_day = ["12AM", "1AM", "2AM", "3AM", "4AM", "5AM", "6AM", "7AM",
        "8AM", "9AM", "10AM", "11AM", "12PM", "1PM", "2PM", "3PM", "4PM",
        "5PM", "6PM", "7PM", "8PM", "9PM", "10PM", "11PM"]
    crime_hours = [i.hour for i in up_crimes]
    hour_counts = []
    for hours in hours_day:
        if hours not in crime_hours:
            hour_counts.append(0)
        else:
            freq = crime_hours.count(hours)
            hour_counts.append(freq)
    hour_max = max(hour_counts)
    hour_index = hour_counts.index(hour_max)
    name_hour = hours_day[hour_index]
    return name_hour
 


if __name__ == "__main__":
    main()
