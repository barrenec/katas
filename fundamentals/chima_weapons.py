
'''
The citizens of Chima need your help. Their weapons got mixed up! 
They need you to write a program that accepts the name of a character 
in Chima then tells which weapon he/she owns. For example: your 
program should return a solution in the format: "Gorzan-Cudjak". 
You must complete the following characters: Laval(Shado Valious), 
Cragger(Vengdualize), Lagravis(Blazeprowlor), Crominus(Grandorius), 
Tormak(Tygafyre), and LiElla(Roarburn). Return "Not a character" for invalid inputs.
'''

def identify_weapon(character):
    
    characters = {"Gorzan": "Cudjak"
    				, "Laval": "Shado Valious", "Cragger": "Vengdualize" \
    				, "Lagravis": "Blazeprowlor", "Crominus": "Grandorius" \
    				, "Tormak": "Tygafyre", "LiElla": "Roarburn"}

    return  character + "-" + characters[character]  if characters.has_key(character) else "Not a character"
    	

print identify_weapon("Tormak")
