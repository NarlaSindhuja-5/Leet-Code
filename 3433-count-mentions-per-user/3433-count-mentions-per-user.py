class Solution:
    def countMentions(self, numberOfUsers, events):
        mentions = [0] * numberOfUsers
        online = [True] * numberOfUsers
        offline_until = {}
        offline_users = set()

        events_by_time = {}
        for typ, t_str, info in events:
            t = int(t_str)
            if t not in events_by_time:
                events_by_time[t] = []
            events_by_time[t].append((typ, info))

        for t in sorted(events_by_time.keys()):
            finished = []
            for u in list(offline_users):
                if offline_until[u] <= t:
                    online[u] = True
                    finished.append(u)
            for u in finished:
                offline_users.remove(u)
                del offline_until[u]

            for typ, info in events_by_time[t]:
                if typ == "OFFLINE":
                    uid = int(info)
                    online[uid] = False
                    offline_until[uid] = t + 60
                    offline_users.add(uid)

            for typ, info in events_by_time[t]:
                if typ == "MESSAGE":
                    if info == "ALL":
                        for u in range(numberOfUsers):
                            mentions[u] += 1
                    elif info == "HERE":
                        for u in range(numberOfUsers):
                            if online[u]:
                                mentions[u] += 1
                    else:
                        for p in info.split():
                            if p.startswith("id"):
                                uid = int(p[2:])
                                mentions[uid] += 1

        return mentions
