from PIL import Image, ImageDraw,ImageFont
import numpy as np 
import Map as mp


def CreateImage(text):
    img = Image.new('RGB', (330, 500), color = (255,255,255))
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype("arial.ttf", 40)
    d.text((30,30), text ,font=fnt, fill=(0,0,0))
    return img

#def TrainAlgo(customData):
#    map = mp.Map(customMap=customData)
#    QTable = np.zeros([map.nStates,map.nActions])
#    # QLearn Parameters
#    eta = .628
#    gma = .9
#    epis = 5000
#    rev_list = [] 
#    for i in range(epis):
#        state = map.clear()
#        rAll = 0
#        decision = False
#        j = 0
#       # Set Qtable
#        while j < 99:
#            j+=1
#            # Choose action from Q table
#            action = np.argmax(QTable[state,:] + np.random.randn(1,map.nActions)*(1./(i+1)))
#            # Get New State and Reward Vlaues
#            newState,reward,decision,_ = map.PerformAction(action)
#            QTable[state,action] = QTable[state,action] + eta*(reward + gma*np.max(QTable[newState,:]) - QTable[state,action])
#            rAll += reward
#            state = newState
#            if decision == True:
#                break
#        rev_list.append(rAll)
#    print("Sum of Rewards:", str(sum(rev_list)/epis))

#    return map,QTable,i

def RunAlgo(customData = None):

    map = mp.Map(customMap=customData)
    QTable = np.zeros([map.nStates,map.nActions])
    # QLearn Parameters
    eta = .628
    gma = .9
    epis = 5000
    rev_list = [] 
    for i in range(epis):
        state = map.clear()
        rAll = 0
        decision = False
        j = 0
       # Set Qtable
        while j < 99:
            j+=1
            # Choose action from Q table
            action = np.argmax(QTable[state,:] + np.random.randn(1,map.nActions)*(1./(i+1)))
            # Get New State and Reward Vlaues
            newState,reward,decision,_ = map.PerformAction(action)
            QTable[state,action] = QTable[state,action] + eta*(reward + gma*np.max(QTable[newState,:]) - QTable[state,action])
            rAll += reward
            state = newState
            if decision == True:
                break
        rev_list.append(rAll)
    print("Sum of Rewards:", str(sum(rev_list)/epis))

    # Test
    state = map.clear()
    decision = False
    reward=0.0
    step = 1
    frames = []
    while decision != True:  
        print("Step:",step)
        step = step+1
        mapText = map.getMapText()
        print(mapText)
        frame = CreateImage(mapText)
        frames.append(frame)
        action = np.argmax(QTable[state,:] + np.random.randn(1,map.nActions)*(1./(i+1)))
        newState,reward,decision,_ = map.PerformAction(action)
        QTable[state,action] = QTable[state,action] + eta*(reward + gma*np.max(QTable[newState,:]) - QTable[state,action])
        state = newState
    print("Step:",step)
    mapText = map.getMapText()
    print(mapText)
    frame = CreateImage(mapText)
    frames.append(frame)

    if reward==0.0:
        print("Failed Attempt")
    else:
        print("Success")

    print("No of Steps :",step)
    gifFileName = 'FindTreasure.gif'
    frames[0].save(gifFileName, format='GIF', append_images=frames[1:], save_all=True, duration=800,  loop=0)

    print("GIF generated and stored as ",gifFileName)

def GetCustomMap():
    print("Enter Custom Map")
    print("Sample Map:")

    print("\n".join(mp.DefaultMap))

    cMap = []

    for i in range(1,9):
        line = input('Enter Line {0}:'.format(i))
        cMap.append(line)

    return cMap




print("Reinforcement Learning using QLearn")
print("Map Legend ")
print("S: Start \nx: Obstacle \n-:Free Path \nT: Treasure \n(M): Current Position \n")

print("-----------------------------------------------\n\n")

while True:
    print("Select Maps")
    print("1. Auto Generate Map")
    print("2. Enter Custom Map")

    userChoice = int(input('Select one option from above : '))

    if userChoice == 1:
        RunAlgo(None)
    elif userChoice == 2:
        cMap = GetCustomMap()
        RunAlgo(cMap)
    else:
        choice = input('Enter Valid Option. Press Y to Restart and N to Exit: ')
        if str.lower(choice) == 'n':
            sys.exit()
        else:
            continue