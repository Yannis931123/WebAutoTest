from datetime import datetime

def base_url():
    return "https://passport.cnblogs.com/user/signinuser/signin"

def current_time():
    time="%a %b %d %H:%M:%S %Y"
    return datetime.now().strftime(time)

def time_diff(start,end):
    time="%a %b %d %H:%M:%S %Y"
    return datetime.strftime(end,time)-datetime.strftime(start,time)