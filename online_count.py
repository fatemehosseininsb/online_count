def online_count(statuses):
     s = 0
     for i in statuses:
          if statuses[i] == "online":
               s += 1
     return s
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
print(online_count(statuses))