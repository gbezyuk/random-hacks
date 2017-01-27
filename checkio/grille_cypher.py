def rotate_grille_clockwise (grille):
    return zip(*grille[::-1])

def generate_all_full_product_matrix(gl):
    return zip([0]*gl+[1]*gl+[2]*gl+[3]*gl, range(gl)*gl)

def recall_password(cipher_grille, ciphered_password, number_of_turns=4):
    res = ''
    gl = len(cipher_grille)    
    for k in range(number_of_turns):
        res += ''.join([
            ciphered_password[i][j] for i, j in generate_all_full_product_matrix(gl) if cipher_grille[i][j] == 'X'
        ])
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
print(recall_password(grille, cypher))

assert(recall_password(grille, cypher) == password)
