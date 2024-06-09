import sys

input = sys.stdin.readline

def solution(m: str, musicinfos: list) -> str:
    def replace_sharps(melody: str) -> str:
        replace_dict = {'C#': 'Z', 'D#': 'Y', 'F#': 'X', 'G#': 'W', 'A#': 'V', 'B#': 'U'}
        for k, v in replace_dict.items():
            melody = melody.replace(k, v)
        return melody

    m = replace_sharps(m)
    
    candidates = []

    for idx, info in enumerate(musicinfos):
        start, end, title, sheet = info.split(',')
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        play_time = (end_h * 60 + end_m) - (start_h * 60 + start_m)
        
        sheet = replace_sharps(sheet)
        
        if play_time <= len(sheet):
            full_sheet = sheet[:play_time]
        else:
            full_sheet = (sheet * (play_time // len(sheet))) + sheet[:play_time % len(sheet)]

        if m in full_sheet:
            candidates.append((play_time, -idx, title))

    if not candidates:
        return '(None)'

    candidates.sort(reverse=True)
    return candidates[0][2]

