import sys
from collections import defaultdict

input = sys.stdin.readline

enter_format = "{}님이 들어왔습니다."
leave_format = "{}님이 나갔습니다."

def solution(record: list) -> list:
    uid_info = defaultdict(str)
    actions = []
    
    for data in record:
        command = data.split()
        action = command[0]
        uid = command[1]
        
        if action in ("Enter", "Change"):
            name = command[2]
            uid_info[uid] = name
            
        if action in ("Enter", "Leave"):
            actions.append((action, uid))
            
    answer = []
    for action, uid in actions:
        if action == "Enter":
            answer.append(enter_format.format(uid_info.get(uid)))
        else:
            answer.append(leave_format.format(uid_info.get(uid)))
            
    return answer