# Project 2
# File: project2_Team15.py
# Date: 2 November 2018
# By: 
# Francisco Rivera
# river177
# Zach Ghera
# zghera
# Dylan Watson
# watso192
# Scott Haseman
# shaseman
# Section: 1
# Team: 15
#
# ELECTRONIC SIGNATURE
# Zachary Ghera
# Francisco Rivera
# Scott Haseman
# Dylan Watson
#
# The electronic signatures above indicate that the program
# submitted for evaluation is the combined effort of all
# team members and that each member of the team was an
# equal participant in its creation. In addition, each
# member of the team has a general understanding of
# all aspects of the program development and execution.

import math
import sys

ENERGY_OUT = 10000000    #j
GRAVITY = 9.81           #m/s^2
WATER_DENSITY = 1000     #kg/m^3
PHOUSE_COST = 100000     #$
GPIPE_COST = 500         #$/pipe
TOTAL_ENERGY = (4.32 * 10 ** 11)

def output():
    print("Most cost efficient system parameters for zone", zoneNum)
    print("Diameter of pipe:", diameter, "m")
    print("Volume of flow:", flow, "m^3/s")                            
    print("Most efficient pump efficiency coefficient:")


            
#function that calculates the overall cost of the hydropump system
def total_cost(zone):   
    height_wall = self.zone.getAddHeight() #changed to running total height
    height_tot = height_wall / 2 + self.zone.getZoneHeight()
    area_new = self.zone.finalArea(height_tot, height_wall)

    cost = self.zone.getTotalCost() + self.zone.getRaiseCost() + self.zone.getAdditionalCosts(area_new) 
    cost += self.zone.perimeter(area_new) * (30 + (height_wall - 5) * (60 - 30)/(7.5 - 5 ))
    cost += area_new * self.zone.getSitePrep

    return cost
 
#function that calculates the cost and efficiency of filling the reservoir
def filling(time,zone,pump,bends,pump_data,pump_epr):
    pump.upFriction(time,pump_data,pump_epr,bend_data,bend_id)

#function that calculates the cost and efficiency of draining the reservoir
def draining(time,zone,bends,pipe,turbine,pump,pipe_data,pipe_id,bend_data,bend_id,turbine_data,turbine_epr):
    pipe.frictionHeight(pipe_data,pipe_id)    
    bends.bendCostDown(time,bend_data,bend_id)
    turbine.turbineLoss(turbine_data,turbine_epr)

#12 hours is 43,200 seconds
#function that calculates the overall efficiency of the hydropump system
def efficiency(zone_num, isRaised, fill_time): #fill_time in hours
    fill_time *= 3600 #converts hours to seconds
    pump_data = {
        .8: [200,220,242,266,293,322,354,390,429,472,519],
        .83: [240,264,290,319,351,387,425,468,514,566,622],
        .86: [288,317,348,383,422,464,510,561,617,679,747],
        .89: [346,380,418,460,506,557,612,673,741,815,896],
        .92: [415,456,502,552,607,668,735,808,889,978,1076]
    }
    pump_epr = [20,30,40,50,60,70,80,90,100,110,120]

    pipe_data = {
        .05: [1.00,1.20,2.57,6.30,14,26,43,68,102,144,197,262,340],
        .03: [1.20,1.44,3.08,7.56,16,31,52,82,122,173,237,315,408],
        .02: [1.44,1.72,3.70,9.07,20,37,63,98,146,208,284,378,490],
        .01: [2.16,2.58,5.55,14,29,55,94,148,219,311,426,567,735],
        .005: [2.70,3.23,6.94,17,37,69,117,185,274,389,533,708,919],
        .002: [2.97,3.55,7.64,19,40,76,129,203,302,428,586,779,1011]
    }
    pipe_id = [.1,.25,.5, .75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3]

    bend_data = {
        20: [.1,[1.00,1.49,4.93,14,32,62,107,169,252,359,492,654,849]],
        30: [.15,[1.05,1.57,5.17,15,34,65,112,178,265,377,516,687,892]],
        45: [.2,[1.10,1.64,5.43,16,36,69,118,187,278,396,542,721,936]],
        60: [.22,[1.16,1.73,5.70,16,38,72,124,196,292,415,569,757,983]],
        75: [.27,[1.22,1.81,5.99,17,39,76,130,206,307,436,598,795,1032]],
        90: [.3,[1.28,1.90,7,18,41,80,137,216,322,458,628,835,1084]]
    }
    bend_id = [.1,.25,.5,.75,1,1.25,1.5,1.75,2,2.25,2.5,2.75,3]

    zone_bends = {
        1: [False,[30,30]],
        2: [[False,[60,60]],[True,[45,45]]],
        3: [[False,[20,45,45]],[True,[37.5,37.5]]]
    }

    turbine_data = {
        .83: [360,396,436,479,527,580,638,702,772,849,934],
        .86: [432,475,523,575,632,696,765,842,926,1019,1120],
        .89: [518,570,627,690,759,835,918,1010,1111,1222,1345],
        .92: [622,684,753,828,911,1002,1102,1212,1333,1467,1614],
        .94: [746,821,903,994,1093,1202,1322,1455,1600,1760,1936]
    }
    turbine_epr = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

    if zone_num == 1:
        z_height = 30 
        ideal_w_h = 5 
        ideal_area = 360000    
        raise_cost = 0
        site_prep = .25
        pipe_l = 67.082
        pipe_l_r = 0
    elif zone_num == 2:
        z_height = 100
        ideal_w_h = 15 
        ideal_area = 25617.377
        raise_cost = 985250   
        site_prep = .5
        if (isRaised):
            pipe_l_r = 171.421
            pipe_l = 0
        else:
            pipe_l_r = 0
            pipe_l = 187.735            
   
    else:
        z_height = 65
        ideal_w_h = 15
        ideal_area = 39760.782
        raise_cost = 633222
        site_prep = .06
        if (isRaised):
            pipe_l_r = 111.993
            pipe_l = 0
        else:
            pipe_l_r = 0
            pipe_l = 114.554
        
    zone = Zone(zone_num,z_height,ideal_w_h,ideal_area,raise_cost,site_prep,pipe_l,pipe_l_r)

    if zone_num == 1:
        angs = [30,30]
    elif zone_num == 2:
        if (isRaised):
            angs = [45,45]
        else:
            angs = [60,60]
    else: 
        if (isRaised):
            angs = [37.5,37.5]
        else:
            angs = [20,45,45]     

    bends = Bend(zone,angs)
    pipe = Pipe(zone,pipe_l,pipe_l_r,bends)
    turbine = Turbine(zone,pipe)
    pump = Pump(zone,pipe,bends)

    draining(time,zone,bends,pipe,turbine,pump,pipe_data,pipe_id,bend_data,bend_id,turbine_data,turbine_epr)
    filling(time,zone,pump,bends,pump_data,pump_epr,bend_data,bend_id,bend_data,bend_id)
    
    total_cost(zone)                                                                                                                                
    eff = self.zone.efficiencyCalc()

    

#A zone object represents one of the three water hydro storage zones
class Zone:
    def __init__(self,num,zone_height, ideal_wall_height, ideal_area,raise_cost,site_prep,pipe_l,pipe_l_r, tot_cost = 0,add_cost=0): 
        self.num = num
        self.z_height = zone_height
        self.pipe_length = pipe_l
        self.pipe_length_r = pipe_l_r
        self.raise_cost = raise_cost
        self.site_prep = site_prep
        self.add_height = ideal_wall_height
        self.ideal_area = ideal_area
        self.add_cost = add_cost
        self.tot_cost = tot_cost
        self.final_tot_height
        self.final_area
        self.pipe_box
    #getters
    def getZoneNum(self):
        return self.num

    def getPipeLength(self):
        return self.pipe_length

    def getPipeLengthR(self):
        return self.pipe_length_r

    def getAddCost(self):
        return self.add_cost

    def getZoneHeight(self):
        return self.z_height

    def getAddHeight(self):
        return self.add_height

    def getIdealArea(self):
        return self.ideal_area
    
    def getRaiseCost(self):
        return self.raise_cost                                                              

    def getSitePrep(self):
        return self.site_prep

    def getAdditionalCosts(self,area):
        costs = 0
        if self.num == 1:
            costs = 148000
            costs += (self.getPipeBox) * (math.sqrt(2) * self.getAddHeight)                                    
        elif self.num ==2:
            costs = 202000
            costs += (self.getPipeBox) * (self.getAddHeight / math.sin(math.pi / 9))
        else:
            costs = 150000 + area * .12
            costs += (self.getPipeBox) * (math.sqrt(2) * self.getAddHeight)
        
        return costs 
    def getTotalArea(self):
        return self.final_area

    def getPipeBox(self):
        return self.pipe_box            

    def getTotalCost(self):
        return self.tot_cost

    def getFinalTotalHeight(self):
        return self.final_tot_height 

    #setters
    def setPipeBox(self,cost):
        self.pipe_box = cost            

    #calcs
    def addTotalCost(self,cost):
        self.tot_cost += cost

    def addWallHeight(self,add):
        self.add_height += add

    def getfinalArea(self,area):
        self.final_area = area

    def finalTotalHeight(self):
        self.final_tot_height = self.z_height + self.getAddHeight()

    #return the perimeter of the zone based on the new area of the system with energy losses
    def perimeter(self, area_new):
        if self.num == 1:
            return 4 * math.sqrt(area_new)                          #rectangular zone
        elif self.num ==2:
            return (15/4) * math.sqrt((16*area_new)/math.sqrt(105)) #triangular zone
        else:
            return ((math.sqrt(area_new / math.pi)) * 2 * math.pi)  #circular zone

    #calculates ideal mass of system
    def idealMass(self):
        return ((4.32*10 ** 11) / (GRAVITY * (self.z_height + (.5 * self.add_height)))) 

    #calculates ideal mass based off of ideal volume
    def idealVolume(self):
        return self.idealMass() / 1000

    #calculates the ideal wall height for the zone 
    def idealWallHeight(self):
        volume = self.idealVolume()
        wallHeight = volume / self.ideal_area
        return wallHeight

    #caclulates the ideal total reservoir height from the base ground to top of wall
    def idealResHeight(self):
        return self.idealWallHeight() + self.z_height

    def finalVolume(self,height_tot):
        return (4.32 * 10 ** 11) / (GRAVITY * height_tot * 1000)

    def finalArea(self,height_tot,height_wall):
        return self.finalVolume(height_tot) / height_wall

    def finalPipeLength(self):
        #uses final res height to get additional pipe length and adds onto length_base
        pass
        
    def flowRateDown(self):
        return (ENERGY_OUT) / (GRAVITY / (self.add_height + self.z_height) / 1000)

    def flowVelocityDown(self):
        return math.sqrt(2 * GRAVITY * (self.add_height + self.z_height))
    
    def flowVelocityUp(self, up_flow): #Calculates the velocity of the water when being pumped to the reservoir
        return 1.273 * up_flow / self.pipeDiameter() ** 2  

    def pipeDiameter(self): # Calculates the ideal pipe diameter based on flow rate and velocity
        velocity = self.flowVelocityDown()
        volume = self.flowRateDown()
        return math.sqrt(1.273 * volume / velocity)
    def efficiencyCalc(self):
        heightIdeal = self.idealResHeight
        heightActual = self.getAddHeight() + self.getZoneHeight
        return heightIdeal / heightActual                             

class Pipe:
    def __init__(self, zone, pipe_l,pipe_l_r,bends = []):
        self.friction
        self.diameter
        self.zone = zone
        self.length = pipe_l + pipe_l_r
        self.bends = bends
    
    def getFriction(self):
        return self.friction
    
    def getDiameter(self):
        return self.diameter
    
    def getLength(self):
        return self.length

    def getIsRaised(self):
        return self.is_raised

    def setFriction(self,friction):
        self.friction = friction

    def setDiameter(self,diameter):
        self.diameter = diameter

    def setLength(self,length):
        self.length = length

    def setIsRaised(self,is_raised):
        self.is_raised = is_raised

    def setBends(self,bends):
        self.bends = bends

    def setZone(self,zone):
        self.zone = zone   

    def getBends(self):
        return self.bends
    
    #finds the diameter of pipe needed -- the next heighest diameter based on the ideal diameter
    def roundDiameter(self,diameter,pipe_id):
        for d in range(len(pipe_id)):
            if diameter <= pipe_id[d]:   
                return d
    
    #find the lowest cost (and its assoc. delta height) out the delta heights when factoring in pipe friction
    def frictionHeight(self, pipe_data, pipe_id):
        D = self.zone.pipeDiameter()
        V = self.zone.flowVelocityDown()
        L = self.zone.getPipeLength() + self.zone.getPipeLengthR()

        #list of delta heights based on the friction, diameter, and length of pipe as well as velocity of water
        heights = [(x * (L * V ** 2) / (D * 2 * GRAVITY)) for x in pipe_data.keys()] 
        
        indexD = self.roundDiameter(D,pipe_id)

        costs = []
        for x in range(0, len(heights)): #the jesus loop - finds the costs for each respective delta height 
            height_wall = heights[x]     #next height in heights array
            height_wall += self.zone.getAddHeight()   #update height with current height of wall
            height_tot = height_wall / 2 + self.zone.getZoneHeight()  #effective height (h in mgh) for the water --> base zone height + 1/2 of the wall height
            area_new = self.zone.finalArea(height_tot, height_wall)   #calculates the new area of zone based on new wall height and effective water height  
            cost = self.zone.perimeter(area_new) * (30 + (height_wall - 5) * (60 - 30)/(7.5 - 5)) #cost due to the new height of the wall (perimeter)
            cost += area_new * self.zone.getSitePrep()                                                 #adding cost to clear land based on clearing
            cost += self.zone.getPipeLength() * pipe_data.get(pipe_data.keys()[x])[indexD]         #cost of all the pipes
            costs.append(cost)                                                                     #append the cost to the parallel list
        
        cost_min = sys.maxsize
        index_low = -1
        for cost in costs:
            if cost < cost_min:
                lowest = cost
                index_low = costs.index(lowest)        

        final_h = heights[index_low]
        self.zone.addWallHeight(final_h)
        self.zone.addTotalCost(self.zone.getPipeLength() * pipe_data.get(pipe_data.keys()[lowest])[indexD])
        self.friction = final_h * (D * 2 * GRAVITY) / (L * V ** 2)
        self.zone.setPipeBox(pipe_data.get(pipe_data.keys()[x])[indexD])
        
class Bend:
    def __init__(self,zone, bend_angs):
        self.bend_angs = bend_angs
        self.zone = zone

    def getBendAng(self):        
        return self.bend_ang
      

    def bendLoss(self,vel,bend_data,bend_id):       # takes in a bend angle and velocity and calculates energy lost
        losses = 0
        for raised in bend_angs.get(self.zone.getZoneNum()):
            if (self.zone.getZoneNum() != 1 and self.zone.getPipeLength() == 0):
                for ang in bend_angs.get(self.zone.getZoneNum())[1]:
                    if (ang == 37.5):
                        bcoe = (bend_data.get(30)[0] + bend_data.get(45)[0])/2
                    else:
                        bcoe = bend_data.get(ang)[0]
            else:
                for ang in bend_angs.get(self.zone.getZoneNum())[0]:
                    bcoe = bend_data.get(ang)[0]
            losses += bcoe * ((vel ** 2)/(2 * GRAVITY))
                 
        return losses

    def bendCostDown(self,time, bend_data,bend_id):
        volume = self.zone.finalVolume((self.zone.getAddHeight() / 2) + self.zone.getZoneHeight())  
        vel = self.zone.flowVelocityUp(volume/time)



        heights = [self.bendLoss(vel,bend_data,bend_id) for x in turbine_data.keys()]

        costs = []
        for x in range(0, len(heights)): #the jesus loop 
            height_wall = heights[x]     
            height_wall += self.zone.getAddHeight() #changed to running total height
            height_tot = height_wall / 2 + self.zone.getZoneHeight()
            area_new = self.zone.finalArea(height_tot, height_wall)
            cost = self.zone.perimeter(area_new) * (30 + (height_wall - 5) * (60 - 30)/(7.5 - 5 ))
            cost += area_new * self.zone.getSitePrep()

            index = self.roundEPR(height_tot,turbine_epr)

            cost += self.zone.flowRateDown() * turbine_data.get(turbine_data.keys()[x])[index] #flow rate x unit cost at epr and height
            costs.append(cost)
        
        cost_min = sys.maxsize
        index_low = -1
        for cost in costs:
            if cost < cost_min:
                cost_min = cost
                index_low = costs.index(cost_min)    
                break    

        final_h = heights[index_low]
        self.zone.addWallHeight(final_h)

        final_epr = self.roundEPR((self.zone.getAddHeight() / 2 + self.zone.getZoneHeight()),bend_data)
        self.zone.addTotalCost(self.zone.flowRateDown() * turbine_data.get(turbine_data.keys()[final_epr])[index_low]))  

    

class Pump:
    def __init__(self,zone,pipe,bends):
        self.pipe = pipe
        self.elev = elev
        self.zone = zone
        self.bends = bends
        
    def getPipe(self):
        return self.pipe  
    
    def getBends(self):
        return self.bends
        
    def heightPump(self,n, time, volume):
        #D = self.zone.pipeDiameter()
        #V = self.zone.flowVelocityUp(flow)
        #EOut = EIn / n                
        #flowUp = EOut / (GRAVITY / self.zone.add_height / 1000)
        #volume = time * flowUp

        flowUp = volume / time
        EOut = flowUp * (GRAVITY / self.zone.add_height / 1000)
        EIn = EOut * n                        
        dE = EIn - EOut
        height = self.zone.getZoneHeight()
        height += dE / (GRAVITY * self.zone.idealMass())
        return height

    def bendLoss(self,vel,bend_data,bend_id):       # takes in a bend angle and velocity and calculates energy lost
        losses = 0
        for raised in bend_angs.get(self.zone.getZoneNum()):
            if (self.zone.getZoneNum() != 1 and self.zone.getPipeLength() == 0):
                for ang in bend_angs.get(self.zone.getZoneNum())[1]:
                    if (ang == 37.5):
                        bcoe = (bend_data.get(30)[0] + bend_data.get(45)[0])/2
                    else:
                        bcoe = bend_data.get(ang)[0]
            else:
                for ang in bend_angs.get(self.zone.getZoneNum())[0]:
                    bcoe = bend_data.get(ang)[0]
            losses += bcoe * ((vel ** 2)/(2 * GRAVITY))
            
        return losses

    def roundEPR(self,height,pump_epr):    # returns an effective performance rating rounded to the closest 
        for e in range(len(turbine_epr)):  # viable value
            if height <= pipe_id[e]:   
                return e
                
    def upFriction(self, time, pump_data,pump_epr, bend_data, bend_id): #dE is from pumpFlow     
        volume = self.zone.finalVolume((self.zone.getAddHeight() / 2) + self.zone.getZoneHeight())  
        heights = [self.heightPump(x, time, volume) for x in pump_data.keys()]

        costs = []

        for x in range(0, len(heights)): #the jesus loop 
            height_wall = heights[x]     
            height_wall += self.zone.getAddHeight() #changed to running total height
            height_tot = height_wall / 2 + self.zone.getZoneHeight()
            area_new = self.zone.finalArea(height_tot, height_wall)
            cost = self.zone.perimeter(area_new) * (30 + (height_wall - 5) * (60 - 30)/(7.5 - 5 ))
            cost += area_new * self.zone.getSitePrep()
            velocity = self.zone.flowVelocityUp(volume/ time)
            loss_b = self.bendLoss(velocity, bend_data, bend_id)
            height_tot += loss_b
            index = self.roundEPR(height_tot,pump_epr)

            cost += self.zone.flowRateDown() * pump_data.get(pump_data.keys()[x])[index] #flow rate x unit cost at epr and height
            costs.append(cost)
        
        cost_min = sys.maxsize
        index_low = -1
        for cost in costs:
            if cost < cost_min:
                cost_min = cost
                index_low = costs.index(cost_min)    
                break    

        final_h = heights[index_low]
        final_epr = self.roundEPR((final_h / 2 + self.zone.getAddHeight() / 2 + self.zone.getZoneHeight()),pump_epr)
        self.zone.addTotalCost(self.zone.flowRateDown() * pump_data.get(pump_data.keys()[final_epr])[index_low]))
        


class Turbine:
    def __init__(self,zone,pipe):
        self.pipe = pipe
        self.zone = zone

    def getEfficiency(self):
        return self.efficiency

    def getPipe(self):
        return self.pipe  

    def heightTurbine(self, n): # returns a height value based on gravitational potential energy
        EIn = (ENERGY_OUT) / n
        dE = EIn - (ENERGY_OUT)
        return (dE) / (GRAVITY * self.zone.idealMass())

    def roundEPR(self,epr,turbine_epr):    # returns an effective performance rating rounded to the closest 
        for e in range(len(turbine_epr)):  # viable value
            if epr <= pipe_id[e]:   
                return e

    def turbineLoss(self, turbine_data, turbine_epr):
        heights = [self.heightTurbine(x) for x in turbine_data.keys()]

        costs = []

        for x in range(0, len(heights)): #the jesus loop 
            height_wall = heights[x]     
            height_wall += self.zone.getAddHeight() #changed to running total height
            height_tot = height_wall / 2 + self.zone.getZoneHeight()
            area_new = self.zone.finalArea(height_tot, height_wall)
            cost = self.zone.perimeter(area_new) * (30 + (height_wall - 5) * (60 - 30)/(7.5 - 5 ))
            cost += area_new * self.zone.getSitePrep()

            index = self.roundEPR(height_tot,turbine_epr)

            cost += self.zone.flowRateDown() * turbine_data.get(turbine_data.keys()[x])[index] #flow rate x unit cost at epr and height
            costs.append(cost)
        
        cost_min = sys.maxsize
        index_low = -1
        for cost in costs:
            if cost < cost_min:
                cost_min = cost
                index_low = costs.index(cost_min)    
                break    

        final_h = heights[index_low]
        self.zone.addWallHeight(final_h)

        final_epr = self.roundEPR((self.zone.getAddHeight() / 2 + self.zone.getZoneHeight()),turbine_epr)
        self.zone.addTotalCost(self.zone.flowRateDown() * turbine_data.get(turbine_data.keys()[final_epr])[index_low]))

        


if __name__ == '__main__':
                   
        
                                