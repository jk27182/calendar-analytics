import glob
from collections import defaultdict

import ics
import matplotlib.pyplot as plt



_HOURS = 60*60 

cal_list = glob.glob("*.ics")
dur_per_cal = defaultdict(list)
for cal_name in cal_list:
    with open(cal_name, "r") as f:
        cal = ics.Calendar(f.read())
    for event in cal.events:
        event_meta = {
                    "name": event.name,
                    "begin": event.begin,
                    "end": event.end,
                    "duration": event.duration.seconds,
        }
        dur_per_cal[cal_name].append(event_meta)
     
fig, axs = plt.subplots(
        nrows=len(dur_per_cal.keys()),
        ncols=1,
        figsize=(20,8)
) 
for ax, cal in zip(axs, dur_per_cal.keys()):
    durations = [event_dict['duration']/ _HOURS for event_dict in dur_per_cal[cal]]
    events = [event_dict['name'] for event_dict in dur_per_cal[cal]]
    ax.bar(events, durations)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=35, ha='right')
    ax.grid(True, axis="y")

plt.show()



