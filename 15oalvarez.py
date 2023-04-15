es_aurebesh = {'a': 'y', 'b': 'p', 'c': 'v', 'd': 'g', 'e': 'u',
               'f': 'k', 'g': 'd', 'h': 'x', 'i': 'j', 'j': 'i',
               'k': 'f', 'l': 'n', 'm': 'c', 'n': 'l', 'ñ': 'm',
               'o': 'e', 'p': 'b', 'q': 'h', 'r': 's', 's': 'r',
               't': 't', 'u': 'o', 'v': 'q', 'w': 'z', 'x': 'w',
               'y': 'a', 'z': 'ñ'}

aurebesh_text = ""
spanish_text = ""
text= input ("Introduce el texto a traducir (esp & aur)")

def spanish_to_aurebesh(text):
    
    # Convierte un texto en español a Aurebesh.
    
    aurebesh_text = ""
    for char in text:
        if char.lower() in es_aurebesh:
            aurebesh_text += es_aurebesh[char.lower()]
        else:
            aurebesh_text += char
    print(f"{text} en Aurebesh es {aurebesh_text}")


def aurebesh_to_spanish(text):
    
    # Convierte un texto en Aurebesh a español.
    
    spanish_text = ""
    for char in text:
        if char.lower() in es_aurebesh.values():
            for key, value in es_aurebesh.items():
                if value == char.lower():
                    spanish_text += key
        else:
            spanish_text += char
    print(f"{text} en español es {spanish_text}")


spanish_to_aurebesh(text)
aurebesh_to_spanish(text)

