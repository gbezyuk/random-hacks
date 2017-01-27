def rotate_grille_clockwise (grille):
    return list(zip(*grille[::-1]))

def recall_password(cipher_grille, ciphered_password):
    res = ['', '', '', '']
    cg = list(cipher_grille)
    for k in range(4):
        for i in range(len(cg)):
            for j in range(len(cg[i])):
                if cg[i][j] == 'X':
                    res[k] += ciphered_password[i][j]
        
        cg = rotate_grille_clockwise(cg)
    return ''.join(res)

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
