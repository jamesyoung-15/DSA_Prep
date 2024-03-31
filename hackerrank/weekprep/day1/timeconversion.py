""" 
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time. 

Ex: 
s = '12:01:00AM'

returns: '00:01:00'

"""


def timeConversion(s):
    # Write your code here
    
    # need to get the hour (first two strings)
    hour_string = s[:2]
    hour_int = int(hour_string)
    print(hour_int)
    # checking if it is am or pm
    am_pm = s[8:]
    # if it is pm, add 12 hours (eg. 1:00 pm is 13:00), and check special case of 12 am and convert to 00
    if am_pm == 'PM':
        # only time we don't add 12 hours is for 12 pm
        if hour_int!=12:
            hour_int += 12
        hour_string = str(hour_int)
    else:
        # if 12 am, convert to 00
        if hour_int == 12:
            hour_string = "00"
        # for cases where hour is less than 10, we need to add a 0 to the string ie. 1:00 to 01:00
        elif hour_int<10:
            hour_string = "0" + str(hour_int)
        else:
            hour_string = str(hour_int)
    
    # add the updated hour string to rest of time excluding am/pm
    output = hour_string + s[2:8]
    return output


if __name__ == '__main__':
    s = "12:40:22PM"
    output = timeConversion(s)
    print(output)