def rotate_grille_clockwise (grille):
    return zip(*grille[::-1])

def recall_password(cipher_grille, ciphered_password):
    res = ''
    for k in range(4):
        for i in range(len(cipher_grille)):
            res += ''.join([ciphered_password[i][j] for j in range(len(cipher_grille[i])) if cipher_grille[i][j] == 'X'])            
        
        cipher_grille = rotate_grille_clockwise(cipher_grille)
    return res

grille = (
    'X...',
    '..X.',
    'X..X',
    '....'
)

cypher = (
    'itdf',
    'gdce',
    'aton',
    'qrdi'
)

password = 'icantforgetiddqd'

assert(recall_password(grille, cypher) == password)
