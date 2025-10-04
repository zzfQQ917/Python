def print_stairs(total, player_intent, computer_intent):
    
    square = 1
    allStairs = [] 

    if total//2 != 0:
        space = total - 1 
        for i in range((total+1)//2):
            newList = []
            for j in range(square):
                newList.append('■')
            
            for k in range(space): 
                newList.append(' ')
            
            for l in range(square):
                newList.append('■')
            allStairs.append(newList)
            square += 1 
            space -= 2
    else:
        space = total
        for i in  range(total//2): 
            newList = [] 
            for j in range(square): 
                newList.append('■')
            
            for k in range(space):
                newList.append(' ')
            
            for l in range(square):
                newList.append('■')
            allStairs.append(newList) 
            space -= 2

        # 공식: 사용자가 내려가는 칸수 = (player_intent, player_intent), 사용자가 올라가는 칸수 = (total - player_intent, player_intent)
        # 컴퓨터가 내려가는 칸수 = (total - computer_intent, computer_intent), 컴퓨터가 올라가는 칸수 = (computer_intent, computer_intent)  
        player_circle = '○'
        computa_circle = '●'
        combined_circle = '◐'
        if player_intent + computer_intent != total:
            if player_intent <= total//2: 
                allStairs[player_intent][player_intent] = player_circle

            else:
                allStairs[total - player_intent][player_intent] = player_circle
            
            if computer_intent >= total//2:
                allStairs[computer_intent][computer_intent] = computa_circle
            
            else:
                allStairs[total - computer_intent][computer_intent] = computa_circle
        
        else:
            if player_intent <= total//2:
                allStairs[player_intent][player_intent] = combined_circle
            
            else:
                allStairs[total - player_intent][player_intent] = combined_circle