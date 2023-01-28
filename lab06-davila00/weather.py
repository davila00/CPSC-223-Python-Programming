import json
import calendar

def read_data(*, filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}

def write_data(*, data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def max_temperature(*, data, date):
    temperature = []
    for key in data:
        if date == key[0:8]:
            temperature.append(data[key]['t'])
    if len(temperature):
        return max(temperature)
    else:
        return None

def min_temperature(*, data, date):
    temperature = []
    for key in data:
        if date == key[0:8]:
            temperature.append(data[key]['t'])
    if len(temperature):
        return min(temperature)
    else:
        return None

def max_humidity(*, data, date):
    humidity = []
    for key in data:
        if date == key[0:8]:
            humidity.append(data[key]['h'])
    if len(humidity):
        return max(humidity)
    else:
        return None

def min_humidity(*, data, date):
    humidity = []
    for key in data:
        if date == key[0:8]:
            humidity.append(data[key]['h'])
    if len(humidity):
        return min(humidity)
    else:
        return None

def tot_rain(*, data, date):
    raintotal = []
    for key in data:
        if date == key[0:8]:
            raintotal.append(data[key]['r'])
    if len(raintotal):
        return sum(raintotal)
    else:
        return None

def report_daily(*, data, date):
    t = []
    h = []
    r = []
    for key in data:
        if key[0:8] == date:
            for key2 in data[key]:
                if key2 == 't':
                    t.append(data[key][key2])
                elif key2 == 'h':
                    h.append(data[key][key2])
                elif key2 == 'r':
                    r.append(data[key][key2])
    return None
def report_historical(*, data):
    historical = []
    for key in data:
        if data == key[0:8]:
            historical.append(data[key]['r'])
    return sum(historical) if len(historical) else None
