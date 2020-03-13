from math import atan, cos, pi

P_n_of_teeth, G_n_of_teeth = 15, 30
P_diameter, G_diameter = 50, 80 #AKA Pitch Diameter D

def Pinion(NumberOfTeathPinion, DiameterOfPitchCirclePinion, NumberOfTeethGear):
    DiametralPitch = NumberOfTeathPinion / DiameterOfPitchCirclePinion
    WholeDepth = 2.188 / DiametralPitch + 0.002
    Addendum = 1 / DiametralPitch
    Dedendum = WholeDepth - Addendum
    Clearance = WholeDepth - 2 * Addendum
    CircularToothThickness = 1.5708 / DiametralPitch
    PitchAngle = (atan(NumberOfTeathPinion / NumberOfTeethGear)) * 180 / pi
    OutsideDiameter = DiameterOfPitchCirclePinion + 2 * Addendum * cos(PitchAngle*pi/180)
    return [NumberOfTeathPinion, DiametralPitch, WholeDepth, Addendum, Dedendum, Clearance, CircularToothThickness,
            PitchAngle, OutsideDiameter]

def Gear(NumberOfTeathGear, DiameterOfPitchCircleGear, PitchAnglePinion):
    DiametralPitch = NumberOfTeathGear / DiameterOfPitchCircleGear
    WholeDepth = 2.188 / DiametralPitch + 0.002
    Addendum = 1 / DiametralPitch
    Dedendum = WholeDepth - Addendum
    Clearance = WholeDepth - 2 * Addendum
    CircularToothThickness = 1.5708 / DiametralPitch
    PitchAngle = (90 - PitchAnglePinion)
    OutsideDiameter = DiameterOfPitchCircleGear + 2 * Addendum * cos(PitchAngle*pi/180)
    return [NumberOfTeathGear, DiametralPitch, WholeDepth, Addendum, Dedendum, Clearance, CircularToothThickness,
            PitchAngle, OutsideDiameter]

Names=["NumberOfTeath", "DiametralPitch", "WholeDepth", "Addendum", "Dedendum", "Clearance", "CircularToothThickness",
            "PitchAngle", "OutsideDiameter"]

Pinionlst=Pinion(P_n_of_teeth, P_diameter, G_n_of_teeth)

Gearlst=Gear(G_n_of_teeth, G_diameter, Pinionlst[7])

for i in range(len(Names)):
    print(Names[i]+"\t"+str(round(Pinionlst[i], 3))+"\t"+str(round(Gearlst[i], 3)))

print("(Gearlst[1]**-1)*pi=" + str((Gearlst[1]**-1)*pi))
print("(Pinionlst[1]**-1)*pi=" + str((Pinionlst[1]**-1)*pi))