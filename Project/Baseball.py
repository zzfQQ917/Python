import random


def Attack_hitBall():
    chosen = random.randint(0, 31)

    while True:
        hitter = int(input("타자는 0부터 30까지의 숫자를 입력하시오. "))
        if hitter > 0 and hitter < 30:
            break
        else:
            continue

    Subtracted = abs(chosen - hitter)
    if Subtracted <= 5:
        return "홈런"
    elif Subtracted <= 10:
        return "2루타"
    elif Subtracted <= 12:
        return "안타"
    elif Subtracted <= 18:
        return "파울"
    elif Subtracted >= 18:
        return "아웃"


position = {
    0: "타자",
    1: "홍길동",
    2: "김성근",
    3: None
}


def Attack_movePosition(hitResult, position):
    newHitter = position[0]
    newPosition = {
        1: None,
        2: None,
        3: None,
    }
    score = 0
    if hitResult == "안타":
        add = 1
    elif hitResult == "2루타":
        add = 2
    elif hitResult == "홈런":
        add = 4
    elif hitResult == "파울":
        add = 0
    elif hitResult == '아웃':
        newPosition = position
        while True:
            deleteTarget = random.choice(list(position.keys()))
            if newPosition[deleteTarget] is None:
                newPosition[deleteTarget] = None
                return newPosition

    newPosition[add] = newHitter

    for key, value in position.items():
        if key == 0:
            continue
        if value is None:
            continue
        key += add
        if key <= 3:
            newPosition[key] = value
        else:
            score += 1
    return newPosition, score


comPosition = {
    0: "컴타자",
    1: "컴선수1",
    2: "컴선수2",
    3: None
}

def Defend_Catcher(comPosition, deadBallpercentages):
    newHitter = comPosition[0]

    if not 1 > deadBallpercentages > 0:
        return "데드볼 확률 0보다 크고, 1보다 작아야 합니다. "

    throwType = ["커브볼", "직구", "슬라이더"]
    comSelection = random.choice(throwType)
    for i, type in enumerate(throwType):
        print(f"{type} - {i + 1}")
    while True:
        unExpected = input("숫자 1, 2, 3 중 입력해 투수가 던진 공의 종류를 맞추시오. ")
        emptyList = ["1", "2", "3"]
        if unExpected in emptyList:
            unExpected = int(unExpected)
            break
        else:
            continue

    success = comSelection == unExpected
    if success == True:
        print("투수가 던진 공의 종류를 맞추셨습니다.")
    else:
        print("투수가 던진 공의 종류를 못 맞추셨습니다.")

    HBP = random.choices(range(0, 2), weights= [1 - deadBallpercentages, deadBallpercentages])
    HBP = HBP[0]
    if HBP == 0:
        hitType = ["안타", "2루타", "홈런", "파울", "아웃"]
        hitResult = random.choice(hitType)
        print(f"컴퓨터 타자가 친 공의 결과는 {hitResult}입니다.")
        newPosition = {
            1: None,
            2: None,
            3: None,
        }
        score = 0
        if hitResult == "안타":
            add = 1
            if success == True:
                return comPosition, score
        elif hitResult == "2루타":
            add = 2
            if success == True:
                add -= 1
        elif hitResult == "홈런":
            add = 4
            if success == True:
                add -= 1
        elif hitResult == "파울":
            add = 0
            if success == True:
                return comPosition, score
        elif hitResult == '아웃':
            newPosition = comPosition
            while True:
                deleteTarget = random.choice(list(comPosition.keys()))
                if newPosition[deleteTarget] is None:
                    newPosition[deleteTarget] = None
                    return newPosition

        newPosition[add] = newHitter

        for key, value in comPosition.items():
            if key == 0:
                continue
            if value is None:
                continue
            key += add
            if key <= 3:
                newPosition[key] = value
            else:
                score += 1
        return newPosition, score


print(Defend_Catcher(comPosition, 0.1))