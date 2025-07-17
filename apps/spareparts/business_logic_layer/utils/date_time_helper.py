from datetime import datetime
import jdatetime

def gregorian_to_jalali(date_time : datetime):
    converter = jdatetime.GregorianToJalali(date_time.year, date_time.month, date_time.day)
    return f'{converter.jyear}-{converter.jmonth}-{converter.jday}'