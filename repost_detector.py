import json
import sys
import csv
from datetime import datetime

o = dict()
with open("./userTweet.json", "r", encoding="utf-8") as f:
  o = json.loads(f.read())
  
o2 = o["data"]["user"]["result"]["timeline_v2"]["timeline"]
o3 = o2["instructions"]
o4 = [i for i in o3 if "entries" in i.keys()]
if len(o4) != 1:
  print("o4 parsing failed")
  sys.exit(1)
o4 = o4[0]["entries"]

res_list = [["RP_DATE", "RP_URL", "ORG_DATE", "ORG_URL"]]

for o5 in o4:
  if o5["content"]["entryType"] == "TimelineTimelineItem":
    o6 = o5["content"]["itemContent"]["tweet_results"]["result"]
    print(o6["core"]["user_results"]["result"]["legacy"]["screen_name"], end="/status/")
    print(o6["legacy"]["id_str"], end=",")
    print(o6["legacy"]["created_at"], end="")
    if "retweeted_status_result" in o6["legacy"].keys():
      o7 = o6["legacy"]["retweeted_status_result"]["result"]
      print("", end=",")
      print(o7["core"]["user_results"]["result"]["legacy"]["screen_name"], end="/status/")
      print(o7["legacy"]["id_str"], end=",")
      print(o7["legacy"]["created_at"])
      res_list.append([
        datetime.strptime(o6["legacy"]["created_at"], "%a %b %d %H:%M:%S %z %Y").astimezone().isoformat(),
        "https://x.com/"
          + o6["core"]["user_results"]["result"]["legacy"]["screen_name"]
          + "/status/"
          + o6["legacy"]["id_str"],
        datetime.strptime(o7["legacy"]["created_at"], "%a %b %d %H:%M:%S %z %Y").astimezone().isoformat(),
        "https://x.com/"
          + o7["core"]["user_results"]["result"]["legacy"]["screen_name"]
          + "/status/"
          + o7["legacy"]["id_str"],
      ])
    else:
      print()
      
with open("./rp_data.csv", "w", encoding="utf-8", newline="") as f:
  writer = csv.writer(f)
  writer.writerows(res_list)