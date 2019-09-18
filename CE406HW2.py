#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:01:27 2019

@author: devinpowers
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Thu Sep 12 18:27:16 2019
    
    @author: devinpowers
    """

# Program for HW 2 in Concrete Design
import sys 

Size_bars = float(input("What # Bar is Given?:"))
Number_of_Bars = float(input("Number of Bars Given: "))
Width = float(input("Width of Beam: "))
Depth = float(input("Effective depth: "))
Compressive_stress = float(input("Compressive Stress:"))
#fy = yield stress
#fc = compressive stress
yield_stress = float(input("Yield Stress:"))

# Using Condtional Statements

if Size_bars == 8:
    Size_bars = .79
    
else:
    if Size_bars == 10:
        Size_bars = 1.270
    else:
        if Size_bars == 11:
            Size_bars = 1.56123
        else:
            if Size_bars == 9:
                Size_bars = 1.0
         

print("\nSize of Bars for the given #:",Size_bars) # Printing the Size of the Bars
    

Area_Steel = Size_bars* Number_of_Bars

print("\nThe Area Steel reinforcement is (in^2): ", Area_Steel)

# Check Steel Percentage
# p = Area_steel/(width x depth)

Steel_percentage = Area_Steel/(Width*Depth)

print("\nSteel Percentage is", Steel_percentage)

# Calculate Alpha

#Alpha = (Area_c * yield_stress )/(0.85 * Compressive_stress * Width)

alpha_ = ((Area_Steel*yield_stress )/((0.85)*Compressive_stress*Width))


print("\nthe value of Alpha (compressive stress block) is: (inches) ", alpha_)


# Calculate Beta
if Compressive_stress == 4000:
    Beta_ = 0.85
else:
    Beta_ = (0.85-(((Compressive_stress - 4000)/1000)) * 0.05)
print ("\nThe beta Value is:", Beta_)

# Distance from extreme concrete Compression fibers to the neutral axis
# c = alpha/beta

c_displacement = alpha_/Beta_
print( "\nC Value: ", c_displacement)

# Calculate strain in the Reinforcing
# strain = ((d-c))/c*(0.003)

strain = ((Depth - c_displacement)/(c_displacement))*(.003)
print("\nThe Strain is:", strain)

# yield strain 
yield_strain = yield_stress/(29*10^6)
print("\nthe yield strain is:",yield_strain)

if strain >= 0.005:
    strength_reduction_factor = 0.9
    print("\nsince the strain is greater than 0.005, the beam is tension controlled and the strength reduction face is 0.9")
else: 
    if strain < 0.004:
        quit()
    else:
        if 0.004 <= strain <= 0.005:
            strength_reduction_factor = 0.65 + ((strain-yield_strain)/(0.005-yield_strain))*(.25)
            print("\nThe Beam is in a transition zone")
   
    
 
    
            

print("\nThe strength reduction factor is:",strength_reduction_factor)

#  Moment thing
# M_n = Area_steel* yield_stress *(Depth -alpha_/2)
# convert yield_stress to ksi
yield_stress_ksi = yield_stress/1000
M_n = (Area_Steel* yield_stress_ksi* (Depth - alpha_/2))*(1/12)

print("\nMn:",M_n)

# Calcualte usable flexural strength of the beam

Mn = M_n* strength_reduction_factor
print("\nThe usable flexural strength of the beam is:",Mn)


