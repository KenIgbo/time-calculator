def add_time(start_time, duration_time, start_day = ''):

    p_hour = None
    days_ahead = None
    new_time = None

    # we load the parameters into the list l_arg
    l_arg = [start_time, duration_time, start_day]

    # if the third item in l_arg is day of the week, we adjust the case to
    # conform to the keys in the dictionary dic
    if l_arg[2] != '':
        l_arg[2] = (l_arg[2])[0].upper() + (l_arg[2][1:]).lower()

    # we create the dictionary dic
    dic = {'Sunday':0, 'Monday':1, 'Tuesday':2, 'Wednesday':3,
       'Thursday':4, 'Friday':5, 'Saturday':6}

    # we swap keys and values in dic to get a new dictionary dic_inv
    items = list(dic.items())
    items = [(i[1], i[0]) for i in items]
    dic_inv = dict(items)

    # we assign the value start_time in l_arg to the variable p
    p = l_arg[0]

    # if a start_time begins with '12' and ends in 'AM', we change the
    # '12' to '00' to simplify the addition process and start a new day
    if p[:p.index(':')] == '12' and p[-2:] == 'AM':
        p = '00' + p[2:]

    if p[-2:] == 'AM':
        p_hour = int(p[:p.index(':')]) + 0
    if p[-2:] == 'PM' and p[:p.index(':')] == '12':
        p_hour = int(p[:p.index(':')]) + 0
    if p[-2:] == 'PM' and p[:p.index(':')] != '12':
        p_hour = int(p[:p.index(':')]) + 12

    # we assign the value duration_time in L to the variable q
    q = l_arg[1]

    # we slice to get the minutes part of the start_time
    p_mins = int(p[-5:-3])

    # we slice to get the hour and minutes part of duration_time
    q_hour = int(q[:q.index(':')])
    q_mins = int(q[-2:])

    # we add the minutes parts of start and duration to get minutes sum
    sum_mins = p_mins + q_mins
    
    # we find an extra hour from the minutes sum if any
    sum_mins_h = sum_mins//60

    # we find the final minutes time and if its length is equal
    # to 1, we put a '0' in front of the minutes time
    mins_time = str(sum_mins%60)
    if len(mins_time) == 1:
        mins_time = '0' + mins_time

    # we add the hour parts of start and duration to the extra hour if any,
    # to get the hour sum
    sum_hour = p_hour + q_hour + sum_mins_h
    week_day = ''

    # we find all possible intervals of sum_hour and determine their
    # respective variable values
    if sum_hour == 0:
        new_time = str(12) + ':' + mins_time + ' AM'
        days_ahead = ''
        for i in dic:
            if i in l_arg:
                week_day = i

    if sum_hour > 0 and sum_hour < 12:
        new_time = str(sum_hour%12) + ':' + mins_time + ' AM'
        days_ahead = ''
        for i in dic:
            if i in l_arg:
                week_day = i

    if sum_hour == 12:
        new_time = str(12) + ':' + mins_time + ' PM'
        days_ahead = ''
        for i in dic:
            if i in l_arg:
                week_day = i

    if sum_hour > 12 and sum_hour < 24:
        new_time = str(sum_hour%12) + ':' + mins_time + ' PM'
        days_ahead = ''
        for i in dic:
            if i in l_arg:
                week_day = i

    if sum_hour == 24:
        new_time = str(12) + ':' + mins_time + ' AM'
        days_ahead = 'next day'
        for i in dic:
            if i in l_arg:
                week_day = dic_inv[(dic[i]+1)%7]

    if sum_hour > 24 and sum_hour%24 < 12:
        new_time = str(sum_hour%24) + ':' + mins_time + ' AM'

        if new_time[:new_time.index(':')] == '0':
            new_time = str(12) + ':' + mins_time + ' AM'

        day = sum_hour//24
        if day == 1:
            days_ahead = 'next day'
            for i in dic:
                if i in l_arg:
                    week_day = dic_inv[(dic[i]+1)%7]

        if day > 1:
            days_ahead = str(day) + ' days later'
            d_c = int(days_ahead[:days_ahead.index(' ')])
            for i in dic:
                if i in l_arg:
                    week_day = dic_inv[(dic[i]+d_c)%7]    # d_c gives the
                    # number in days_ahead

    if sum_hour  >24 and sum_hour%24 >= 12:
        new_time = str((sum_hour%24)%12) + ':' + mins_time + ' PM'

        if new_time[:new_time.index(':')] == '0':
            new_time = str(12) + ':' + mins_time + ' PM'

        day = sum_hour//24
        if day == 1:
            days_ahead = 'next day'
            for i in dic:
                if i in l_arg:
                    week_day = dic_inv[(dic[i]+1)%7]

        if day > 1:
            days_ahead = str(day) + ' days later'
            d_c = int(days_ahead[:days_ahead.index(' ')])
            for i in dic:
                if i in l_arg:
                    week_day = dic_inv[(dic[i]+d_c)%7]    # d_c gives the
                    # number in days_ahead

    if days_ahead == '' and week_day == '':
        return(new_time)

    if days_ahead == '' and week_day != '':
        return(new_time + ', ' + week_day)

    if days_ahead != '' and week_day == '':
        return(new_time + ' ' + '(' + days_ahead +')')

    if days_ahead != '' and week_day != '':
        return(new_time + ', ' + week_day + ' ' + '(' + days_ahead + ')')

print(add_time("8:16 PM", "466:02", "tuesday"))
