# Nepali Date Converter

## Description
The **Nepali Date Converter** is a Python program that converts an English (Gregorian) date to its corresponding Nepali date (Bikram Sambat). It provides additional details such as the Nepali day of the week, Tithi (lunar phase), and any special events associated with the date. The conversion is based on a reference date and calculates the difference in days between the English and Nepali calendars.

### Features:
- Converts English (Gregorian) dates to Nepali (Bikram Sambat) dates.
- Displays the Nepali day of the week (सोमबार, मंगलबार, etc.).
- Provides the Tithi (lunar phase) for the given date, along with the paksha (Shukla or Krishna).
- Retrieves and displays special events based on the date from an external file.
- Displays the current time when the program is executed.

## Requirements
- Python 3.x
- Libraries:
  - `ephem` (for astronomy calculations)
  - `csv`
  - `datetime`
  - `calendar`

To install `ephem`, use the following command:
```bash
pip install ephem
```

## Files:
1. **Nepali Calendar Program (`nepali_calendar.py`)**: The main program that handles the conversion.
2. **Events Data File (`events.txt`)**: A text file containing important events associated with Nepali dates in the format `Month, Day, Event`. It needs more updates.
3. **Bikram Sambat Data File (`calendar_bs.csv`)**: A CSV file containing the number of days for each month in the Nepali calendar from 1975 BS to 2100 BS.

## How to Use:
1. Run the program `nepali_calendar.py` in your Python environment.
2. Enter the English date (year, month, day) to be converted when prompted.
3. The program will display the corresponding Nepali date, the day of the week, Tithi, and any special events for that date.
4. The program will also show the current Nepali date and time when executed.

### Example:
```bash
Enter English year, month, date to be converted, separated by space:
2024 12 01
```

The program will output the Nepali equivalent of the provided date, Tithi, special events (if any), and the current Nepali calendar for the month.

## Contributions
Feel free to fork this repository, make improvements, or submit issues and pull requests!

## License
This project is open-source and available under the MIT License.
