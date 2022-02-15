class Solution:
    def countPoints(self, rings: str) -> int:
        count=0
        for i in range(1,len(rings),2):
            if 'B0' in rings and 'G0' in rings and 'R0' in rings:
                count+=1
                rings = rings.replace('B0','X0')
                rings = rings.replace('G0','X0')
                rings = rings.replace('R0','X0')
            elif 'B1' in rings and 'G1' in rings and 'R1' in rings:
                count+=1
                rings = rings.replace('B1','X0')
                rings = rings.replace('G1','X0')
                rings = rings.replace('R1','X0')
            elif 'B2' in rings and 'G2' in rings and 'R2' in rings:
                count+=1
                rings = rings.replace('B2','X0')
                rings = rings.replace('G2','X0')
                rings = rings.replace('R2','X0')
            elif 'B3' in rings and 'G3' in rings and 'R3' in rings:
                count+=1
                rings = rings.replace('B3','X1')
                rings = rings.replace('G3','X1')
                rings = rings.replace('R3','X1')
            elif 'B4' in rings and 'G4' in rings and 'R4' in rings:
                count+=1
                rings = rings.replace('B4','X1')
                rings = rings.replace('G4','X1')
                rings = rings.replace('R4','X1')
            elif 'B5' in rings and 'G5' in rings and 'R5' in rings:
                count+=1
                rings = rings.replace('B5','X1')
                rings = rings.replace('G5','X1')
                rings = rings.replace('R5','X1')
            elif 'B6' in rings and 'G6' in rings and 'R6' in rings:
                count+=1
                rings = rings.replace('B6','X1')
                rings = rings.replace('G6','X1')
                rings = rings.replace('R6','X1')
            elif 'B7' in rings and 'G7' in rings and 'R7' in rings:
                count+=1
                rings = rings.replace('B7','X1')
                rings = rings.replace('G7','X1')
                rings = rings.replace('R7','X1')
            elif 'B8' in rings and 'G8' in rings and 'R8' in rings:
                count+=1
                rings = rings.replace('B8','X1')
                rings = rings.replace('G8','X1')
                rings = rings.replace('R8','X1')
            elif 'B9' in rings and 'G9' in rings and 'R9' in rings:
                count+=1
                rings = rings.replace('B9','X1')
                rings = rings.replace('G9','X1')
                rings = rings.replace('R9','X1')
        return count