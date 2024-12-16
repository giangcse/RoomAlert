import json
import time
import requests

# data = {"name": "RA12-CCDDEB", "date": "03/31/00 02:04:53", "uptime": "89d 02:04:53", "scale": 1, "macaddr": "00:80:A3:CC:DD:EB", "devtype": "12", "refresh": "5", "channel": "0", "picvers": "03", "reset_button": 0, "interval": "60", "gtmd_interval": "3600", "version": "v3.2.5", "port": 80, "ip": "10.204.165.2", "serial": "RA12-CCDDEB", "gtmd_disabled": "0", "time_config": {"timezone": "0", "format": "0", "display": "0", "daylight_saving_en": "0"}, "eth_config": {"mtu": 1024, "arpen": 1, "negotiate": "Auto"}, "sensor": [{"lab": "Internal Sensor", "tf": "66.65", "tc": "19.25", "hf": "78.63", "hc": "25.91", "lf": "57.74", "lc": "14.30", "ala": 0, "profile": 1, "t": 16, "en": 1}, {"lab": "Sensor rack 1", "tf": "75.09", "tc": "23.94", "hf": "90.80", "hc": "32.67", "lf": "67.33", "lc": "19.63", "ala": 0, "profile": 1, "t": 38, "en": 1, "h": "54.50", "hh": "88.43", "lh": "37.69", "hi": "75.09", "hic": "23.93", "hhi": "97.99", "hhic": "36.66", "lhi": "67.33", "lhic": "19.62", "hen": 0, "dpc": "14.84", "dpf": "58.71", "dphf": "74.13", "dphc": "23.41", "dplf": "54.89", "dplc": "12.72"}, {"lab": "Sensor rack 2", "tf": "76.28", "tc": "24.60", "hf": "90.77", "hc": "32.65", "lf": "67.35", "lc": "19.64", "ala": 0, "profile": 1, "t": 38, "en": 1, "h": "48.45", "hh": "75.00", "lh": "37.69", "hi": "76.28", "hic": "24.60", "hhi": "97.46", "hhic": "36.36", "lhi": "67.35", "lhic": "19.63", "hen": 0, "dpc": "14.29", "dpf": "57.72", "dphf": "73.41", "dphc": "23.01", "dplf": "54.39", "dplc": "12.44"}, {
#     "lab": "Sensor rack 3", "tf": "75.12", "tc": "23.96", "hf": "88.88", "hc": "31.60", "lf": "66.65", "lc": "19.25", "ala": 0, "profile": 1, "t": 38, "en": 1, "h": "52.14", "hh": "74.66", "lh": "39.03", "hi": "75.12", "hic": "23.95", "hhi": "94.84", "hhic": "34.91", "lhi": "66.65", "lhic": "19.25", "hen": 0, "dpc": "14.39", "dpf": "57.90", "dphf": "72.37", "dphc": "22.43", "dplf": "53.97", "dplc": "12.21"}, {"lab": "Analog Sensor", "volts": "2.04", "highv": "2.21", "lowv": "0.00", "units": {"refmin": "0", "refmax": "5", "min": "0", "max": "5", "sym": "V", "en": "0"}, "ala": 0, "profile": 1, "t": 65, "en": 0}], "signal_twr": [{"RE": {"en": 0, "stat": 0}, "OR": {"en": 0, "stat": 0}, "GR": {"en": 0, "stat": 0}, "BL": {"en": 0, "stat": 0}, "WH": {"en": 0, "stat": 0}, "A1": {"en": 0, "stat": 0}, "A2": {"en": 0, "stat": 0}, "RY": {"en": 0, "stat": 1}, "attach_type": 0, "lab": "Light Tower", "tower_id": 1}], "relay": [{"lab": "Relay Output", "stat": 0, "relay_id": 1}], "s_sen": [{"lab": "Ro ri nuoc", "en": 1, "ala": 1, "profile": 1, "stat": 1}, {"lab": "mat nguon 1", "en": 1, "ala": 1, "profile": 1, "stat": 1}, {"lab": "mat nguon 2", "en": 1, "ala": 1, "profile": 1, "stat": 1}, {"lab": "mat nguon 3", "en": 1, "ala": 1, "profile": 1, "stat": 1}]}
# data = json.loads(json.dumps(data))


def send_request():
    url = 'http://10.204.165.2/getData.json'
    while True:
        param = str(time.time())[:str(time.time()).index('.')]
        try:
            request = requests.get(url + param)
            data = dict(request.text)
            for i in data:
                if type(data[i]) is list:
                    for j in data[i]:
                        if 'tc' in j and 'h' in j:
                            print(j['lab'], ":\t ", j['tc'],
                                  "*C\t", j['h'], "%")
        except:
            print("Connection error!")


if __name__ == '__main__':
    send_request()
