from factionData import getSystems,getFactions,datetime,findLatestTick,dumpList,loadList,cf,formatData

def findExpandingSystems(targetSystem):
    systems = getSystems(targetSystem)
    factions = getFactions()    
    expandingSystems = []
    latestTick = findLatestTick()
    for sys in systems.values():
        for fac in sys['minor_faction_presences']:
            for stateType in ['active_states','pending_states','recovering_states']:
                for state in fac[stateType]:
                    if state['name']=='Expansion':
                        name = sys['name']
                        facId = fac['minor_faction_id']
                        factionName = factions[facId]['name']
                        if datetime.utcfromtimestamp(sys['lastUpdatedAt'] ) > latestTick:
                            updatedToday = True
                        else:
                            updatedToday = False
                        expandingSystems.append({
                            "system":name,
                            "faction":factionName,
                            "stateType":stateType,
                            "updatedToday":updatedToday
                        })
    dumpList(expandingSystems,cf.get('expandingSystem'),returnSystemName)
  
def showExpandingData():
    data = loadList(cf.get('expandingSystem'),10)
    if len(data) > 0:
        output = formatData(data)
    return output

def returnSystemName(sys):
    return sys['system']


findExpandingSystems('Dahan')