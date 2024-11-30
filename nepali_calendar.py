import ephem
import csv
from datetime import date, datetime
import calendar 

_nepdays = ("सोमबार", "मंगलबार", "बुधवार", "बिहिबार", "शुक्रबार", "शनिबार", "आइतबार")
_nepmonths = ("वैशाख", "जेष्ठ", "असार", "श्रावण", "भदौ", "आश्विन", "कार्तिक", "मंसिर", "पौष", "माघ", "फाल्गुण", "चैत्र")
_fullmonths= ("Baishakh", "Jestha", "Asar", "Shrawan", "Bhadau", "Aswin", "Kartik", "Mangsir", "Poush","Magh", "Falgun", "Chaitra")

#special events 
def load_important_events(file_path):
    important_events = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            month, day, event = line.split(",")
            important_events[(int(month), int(day))] = event
    return important_events

# path to the text file containing events
events_file_path = '/Users/ishhh/Downloads/Intern/Capstone Project I/events.txt'

# Load events
_importantevents = load_important_events(events_file_path)

# Check for special events
event = _importantevents.get((_nepmonths, _nepdays))

# Tithi list 
_tithilist = {
    # Sukla pakshya
    1: "प्रतिपदा", 2: "द्वितीया", 3: "तृतीया", 4: "चतुर्थी", 5: "पञ्चमी",
    6: "षष्ठी", 7: "सप्तमी", 8: "अष्टमी", 9: "नवमी", 10: "दशमी",
    11: "एकादशी", 12: "द्वादशी", 13: "त्रयोदशी", 14: "चतुर्दशी", 15: "पूर्णिमा",
    # Krishna pakshya
    16: "प्रतिपदा", 17: "द्वादशी", 18: "तृतीया", 19: "चतुर्थी", 20: "पञ्चमी",
    21: "षष्ठी", 22: "सप्तमी", 23: "अष्टमी", 24: "नवमी", 25: "दशमी",
    26: "एकादशी", 27: "द्वादशी", 28: "त्रयोदशी", 29: "चतुर्दशी", 30: "औंसी"
}

#the first column in the csv file is that of years and then days in each month per year
def load_bs_years_data(file_path):
    bs_years_data = {}
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skipping the header row
        for row in csv_reader:
            year = int(row[0])  
            months_data = [int(x) for x in row[1:]]
            bs_years_data[year] = months_data
    return bs_years_data

file_path = "/Users/ishhh/Downloads/Intern/Capstone Project I/calendar_bs.csv"

# Loading the CSV data into the desired dictionary format
bs_years_data = load_bs_years_data(file_path)

def get_current_time():
    return datetime.now().strftime("%H:%M:%S")

   
def load_event_data(filename="events_data.txt"):
    events = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(", ")
            date = parts[0]
            tithi = parts[1] if len(parts) > 1 else None
            event = parts[2] if len(parts) > 2 else None
            events[date] = {"tithi": tithi, "event": event}
    return events

def get_tithi(date_in):
    
    # The ephem library is a Python package used for performing high-precision astronomy calculations.
    observer = ephem.Observer()  #computer position of grahas
    observer.date = ephem.Date(date_in) #setting the observers' date to input date

    # to get solar longitude
    sun = ephem.Sun(observer)   #create a sun object linked with observer. this will represent position of sun relative to observer's date 
    sun.compute(observer)   #compute sun's position for observer's date.
    solar_longitude = sun.hlon  #retrieves longitude of sun in radians as viewed from earth

    # to get lunar longitude
    moon = ephem.Moon(observer) #as same as of sun
    moon.compute(observer)
    lunar_longitude = moon.hlon

    # Calculate Tithi based on the difference in longitude
   # Note: The difference in longitude between the Moon and the Sun is divided by 𝜋/15, which corresponds to 12 degrees, as each Tithi represents a 12° shift between the Sun and the Moon’s longitudinal positions.
    
    tithi = int((lunar_longitude - solar_longitude) % (2 * ephem.pi) / (ephem.pi / 15)) + 1
    paksha = "शुक्ल पक्ष" if tithi <= 15 else "कृष्ण पक्ष"
    
    return _tithilist[tithi], paksha

def create_nepali_calendar(year, month, start_day_index):
    _shortnepdays = ["आइ", "सोम", "मंग", "बुध", "बिही", "शुक्र", "शनि"]

    # Number of days in the specified month of the given year
    _daysmonth = bs_years_data[year][month - 1]  

    # Initializing days list with empty placeholders for the first week
    _days = [" "] * (start_day_index + 1)

    # Adding actual dates of the month
    for i in range(1, _daysmonth + 1):
        _days.append(str(i))

    # Creating calendar structure
    calendar_lines = []
    calendar_lines.append(f"{_fullmonths[month - 1]} {year}".center(29))  # Nepali month and year
    calendar_lines.append(" ".join(_shortnepdays))  # Add Nepali days to the calendar

    # Split the day list into weeks and format each week
    for i in range(0, len(_days), 7):
        week = _days[i:i + 7]
        _calendarweek = " ".join(day.ljust(3) for day in week)  # Align days
        calendar_lines.append(_calendarweek)

    return "\n".join(calendar_lines)

def main():
   
    print("\n\n------------------- Welcome to Nepali Date Converter --------------------\n")
    # Display current time
    current_time = datetime.now()
    print("The current time is:",get_current_time())
  
    _engYear, _engMonth, _engDate = map(int, input("\n\nEnter English year, month, date to be converted, separated by space: \n").split())

    # Reference English and Nepali date
    startingEngYear, startingEngMonth, startingEngDay = 1957, 4, 13
    startingNepYear, startingNepMonth, startingNepDay = 2014, 1, 1
    _daycount = calendar.SATURDAY

    # Calculate days difference
    date_ref = date(startingEngYear, startingEngMonth, startingEngDay)
    date_provided = date(_engYear, _engMonth, _engDate)
    diff = (date_provided - date_ref).days

    # Initialize Nepali date
    _nepaliYear, _nepaliMonth, _nepaliDay = startingNepYear, startingNepMonth, startingNepDay

    # Adjust Nepali date based on the difference in days
    while diff != 0:
        daysInMonth = bs_years_data[_nepaliYear][_nepaliMonth - 1]
        _nepaliDay += 1

        if _nepaliDay > daysInMonth:
            _nepaliMonth += 1
            _nepaliDay = 1
        if _nepaliMonth > 12:
            _nepaliYear += 1
            _nepaliMonth = 1

        _daycount += 1
        if _daycount > 6:
            _daycount = 0
        diff -= 1

    # Check for special events from the loaded text file
    event = _importantevents.get((_nepaliMonth, _nepaliDay),None)

    # Nepali weekday
    nepali_week_day = _nepdays[_daycount]

    # Calculate Tithi for the provided date
    tithi, paksha = get_tithi(f"{_engYear}/{_engMonth}/{_engDate}")

    # Output the equivalent Nepali date and Tithi
    print(f"\nThe corresponding nepali date is: {_nepaliYear}/{_nepaliMonth}/{_nepaliDay}, {nepali_week_day}")
    print(f"Tithi: {tithi}, {paksha}")
    print(f"Special Event: {event}")

    first_day = _daycount

    # Loop to find the first day
    for day in range(_nepaliDay, 1, -1):  # Loop from the current day back to 1
        first_day -= 1  
        if first_day < 0:
            first_day = 6  

    # Display the Nepali calendar for the given Nepali month
    print("\nThe corresponding month's calendar :")
    print(create_nepali_calendar(_nepaliYear, _nepaliMonth, first_day))

if __name__ == "__main__":
    main()

