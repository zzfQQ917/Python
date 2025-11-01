import random

def Attack_hitBall():
    chosen = random.randint(0, 31)

    while True:
        hitter = int(input("타자는 0부터 30까지의 숫자를 입력하시오: "))
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
    print(f"\n타자가 친 공은 [ {hitResult} ]입니다\n")
    newHitter = position[0]
    newPosition = {
        0: None,
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
                return newPosition, score

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

    if hitResult != "홈런":
        newPosition[add] = newHitter
    else:
        score += 1

    return newPosition, score



comPosition = {
    0: "컴타자",
    1: "컴선수1",
    2: "컴선수2",
    3: None
}

def Defend_Catcher():
    throwType = ["커브볼", "직구", "슬라이더"]
    comSelection = random.choice(throwType)
    for i, type in enumerate(throwType):
        print(f"{type} - {i + 1}")
    while True:
        unExpected = input("숫자 1, 2, 3 중 입력해 투수가 던진 공의 종류를 맞추시오: ")
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
    hitType = ["안타", "2루타", "홈런", "파울", "아웃"]
    hitResult = random.choice(hitType)
    print(f"컴퓨터 타자가 친 공의 결과는 {hitResult}입니다.")
    return hitResult

myTeam = ["서균", "황영국", "이창진", "박준혁", "최윤석", "김혁민"]
comTeam = ["컴1", "컴2", "컴3", "컴4", "컴5", "컴6"]

def print_status(myScore, comScore, whosAttack, remainAttempt, hitter):
    print("-------------------------------------------------------------------------------")
    print(f"현재 공격 차례: {whosAttack}")
    print(f"남은 공격 횟수: {remainAttempt}")
    print(f"현재 타자: {hitter}")
    print(f"현재 우리 팀 점수 : {myScore} | 현재 상대 팀 점수 : {comScore} ")
    print("-------------------------------------------------------------------------------")
def print_stadium(position):
    print(f"               {position[2]}")
    print("           /           \\")
    print("          /             \\")
    print("         /               \\")
    print("        /                 \\")
    print("       /                   \\")
    print("      /                     \\")
    print("     /                       \\")
    print(f"   {position[3]}                    {position[1]}")
    print("     \\                       /")
    print("      \\                     /")
    print("       \\                   /")
    print("        \\                 /")
    print("         \\               /")
    print("          \\             /")
    print("           \\           /")
    print(f"              {position[0]}")

def mainLogic():
    while True:
        myPos = {
        0:None,
        1:None,
        2:None,
        3:None
    }
        comPos = {
            0:None,
            1:None,
            2:None,
            3:None
        }
        userAttempt = int(input("게임 진행 횟수를 입력하시오 : "))
        myScore = 0
        comScore = 0
        for i in range(userAttempt):
            remainAttempt = 3
            hitterNum = 0
            
            while True:
                if remainAttempt == 0:
                    print("삼진 아웃되었습니다. ")
                    break
                elif hitterNum == len(myTeam):
                    print("수비로 전환됩니다. ")
                    break
                print_status(myScore, comScore, "우리 팀", remainAttempt, myTeam[hitterNum])
                myPos[0] = myTeam[hitterNum]  
                print_stadium(myPos)
                hitRes = Attack_hitBall()
                if hitRes == "파울":
                    print(f"\n타자가 친 공은 [ {hitRes} ]입니다. 타자는 다시 한번 공을 칩니다.\n")
                    continue
                myPos, score = Attack_movePosition(hitRes, myPos)
                myScore += score
                if hitRes == "아웃":
                    remainAttempt -= 1
                hitterNum += 1
            comhitterNum = 0
            comremainAttempt =3
            while True:
                if comremainAttempt == 0:
                    print("상대 팀이 삼진 아웃되었습니다. ")
                    break
                elif comhitterNum == len(comTeam):
                    print("상대 팀이 수비로 전환됩니다. ")
                    break
                print_status(myScore, comScore, "상대 팀", comremainAttempt, comTeam[comhitterNum])
                comPos[0] = comTeam[comhitterNum]
                print_stadium(comPos)
                comhitRes = Defend_Catcher()
                if comhitRes == "파울":
                    print(f"\n컴퓨터 타자가 친 공은 [ {comhitRes} ]입니다. 컴퓨터 타자는 다시 한번 공을 칩니다.\n")
                    continue
                comPos, newScore = Attack_movePosition(comhitRes, comPos)
                comScore += newScore
                if comhitRes == "아웃":
                    comremainAttempt -= 1
                comhitterNum += 1
        if myScore > comScore:
            print("당신의 팀이 승리를 거머쥐었습니다! ")
        elif comScore > myScore:
            print("아쉽게도 당신의 팀이 패배하였습니다.. ")
        else:
            print("무승부입니다. ")
        reStart = input("다시 진행하시겠습니까? (Yes/No) : ")
        if reStart == "Yes":
            print("게임을 다시 진행합니다. ")
            continue
        else:
            print("Baseball.py를 종료합니다. ")
            break
mainLogic()