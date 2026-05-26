import string, math

ALPHABET = string.ascii_uppercase

def clean_letters(text):
    return ''.join(ch for ch in text.upper() if ch.isalpha())

def caesar(text, shift, mode='encrypt'):
    if not 1 <= shift <= 25:
        raise ValueError('Shift Caesar harus 1 sampai 25.')
    k = shift if mode == 'encrypt' else -shift
    out = []
    steps = []
    formula = 'E(x)=(x+k) mod 26' if mode == 'encrypt' else 'D(x)=(x-k) mod 26'

    for ch in text:
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            x = ord(ch) - ord(base)
            y = (x + k) % 26
            res = chr(y + ord(base))
            out.append(res)
            steps.append(f"{ch} -> {ch.upper()}={x}, hasil=({x}{'+' if k>=0 else ''}{k}) mod 26 = {y} -> {res.upper()}")
        else:
            out.append(ch)
            steps.append(f"{repr(ch)} bukan huruf, tetap ditulis.")
    return ''.join(out), formula, steps, None

def vigenere_table():
    table = []
    for i in range(26):
        row = []
        for j in range(26):
            row.append(ALPHABET[(i + j) % 26])
        table.append(row)
    return table

def vigenere(text, key, mode='encrypt'):
    key_clean = clean_letters(key)
    if not key_clean:
        raise ValueError('Key Vigenère harus berupa huruf.')
    out = []
    steps = []
    idx = 0
    formula = 'E_i=(P_i+K_i) mod 26' if mode == 'encrypt' else 'D_i=(C_i-K_i) mod 26'

    for ch in text:
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            x = ord(ch) - ord(base)
            key_ch = key_clean[idx % len(key_clean)]
            kv = ord(key_ch) - 65
            y = (x + kv) % 26 if mode == 'encrypt' else (x - kv) % 26
            res = chr(y + ord(base))
            out.append(res)
            op = '+' if mode == 'encrypt' else '-'
            steps.append(f"{ch.upper()} dengan key {key_ch}: ({x} {op} {kv}) mod 26 = {y} -> {res.upper()}")
            idx += 1
        else:
            out.append(ch)
            steps.append(f"{repr(ch)} bukan huruf, tetap ditulis dan key tidak bergeser.")

    return ''.join(out), formula, steps, {
        'vigenere_table': vigenere_table(),
        'alphabet': list(ALPHABET),
        'key': key_clean
    }

def affine(text, a, b, mode='encrypt'):
    if math.gcd(a, 26) != 1:
        raise ValueError('Nilai a harus relatif prima dengan 26. Contoh valid: 1,3,5,7,9,11,15,17,19,21,23,25.')
    if not 0 <= b <= 25:
        raise ValueError('Nilai b harus 0 sampai 25.')

    inv = pow(a, -1, 26)
    formula = 'E(x)=(a*x+b) mod 26' if mode == 'encrypt' else 'D(x)=a^-1*(x-b) mod 26'
    out = []
    steps = []

    for ch in text:
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            x = ord(ch) - ord(base)
            if mode == 'encrypt':
                y = (a * x + b) % 26
                steps.append(f"{ch.upper()}={x}: ({a}*{x}+{b}) mod 26 = {y} -> {ALPHABET[y]}")
            else:
                y = (inv * (x - b)) % 26
                steps.append(f"{ch.upper()}={x}: {inv}*({x}-{b}) mod 26 = {y} -> {ALPHABET[y]}")
            out.append(chr(y + ord(base)))
        else:
            out.append(ch)
            steps.append(f"{repr(ch)} bukan huruf, tetap ditulis.")

    return ''.join(out), formula, steps, {'a_inverse': inv}

def det2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]

def det3(m):
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )

def inv_matrix_mod(m):
    n = len(m)
    d = det2(m) if n == 2 else det3(m)
    dm = d % 26

    if math.gcd(dm, 26) != 1:
        raise ValueError(f'Determinan matriks = {d}, tidak punya invers modulo 26. Ganti matriks key.')

    di = pow(dm, -1, 26)

    if n == 2:
        adj = [
            [m[1][1], -m[0][1]],
            [-m[1][0], m[0][0]]
        ]
    else:
        cof = []
        for r in range(3):
            row = []
            for c in range(3):
                sub = [[m[i][j] for j in range(3) if j != c] for i in range(3) if i != r]
                row.append(((-1) ** (r + c)) * det2(sub))
            cof.append(row)
        adj = [[cof[j][i] for j in range(3)] for i in range(3)]

    return [[(di * adj[i][j]) % 26 for j in range(n)] for i in range(n)], d, di

def parse_matrix(s, n):
    nums = [int(x.strip()) for x in s.replace(';', ',').replace('\n', ',').split(',') if x.strip() != '']
    if len(nums) != n * n:
        raise ValueError(f'Matriks Hill {n}x{n} harus berisi {n*n} angka, pisahkan dengan koma.')
    return [nums[i*n:(i+1)*n] for i in range(n)]

def hill(text, matrix, mode='encrypt'):
    n = len(matrix)
    work = clean_letters(text)

    if not work:
        raise ValueError('Teks Hill harus memiliki huruf.')

    while len(work) % n != 0:
        work += 'X'

    key = matrix
    extra = {'key_matrix': matrix}

    if mode == 'decrypt':
        key, det, det_inv = inv_matrix_mod(matrix)
        extra.update({
            'inverse_matrix': key,
            'determinant': det,
            'det_inverse': det_inv
        })
        formula = 'P = K^-1 x C mod 26'
    else:
        _inv, det, det_inv = inv_matrix_mod(matrix)
        extra.update({
            'determinant': det,
            'det_inverse': det_inv
        })
        formula = 'C = K x P mod 26'

    result = []
    steps = []

    for i in range(0, len(work), n):
        block = work[i:i+n]
        vec = [ALPHABET.index(c) for c in block]
        res = []

        for r in range(n):
            res.append(sum(key[r][c] * vec[c] for c in range(n)) % 26)

        letters = ''.join(ALPHABET[v] for v in res)
        result.append(letters)
        steps.append(f"Blok {block} -> vektor {vec}; hasil {res} -> {letters}")

    final_text = ''.join(result)

    if mode == 'decrypt':
        final_text = final_text.rstrip('X')

    return final_text, formula, steps, extra

def playfair_matrix(key):
    seen = []

    for ch in clean_letters(key).replace('J', 'I'):
        if ch not in seen:
            seen.append(ch)

    for ch in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if ch not in seen:
            seen.append(ch)

    return [seen[i*5:(i+1)*5] for i in range(5)]

def pos(mat, ch):
    ch = 'I' if ch == 'J' else ch

    for r, row in enumerate(mat):
        if ch in row:
            return r, row.index(ch)

    raise ValueError('Huruf tidak ditemukan di tabel Playfair.')

def pair_text(text):
    s = clean_letters(text).replace('J', 'I')
    pairs = []
    i = 0

    while i < len(s):
        a = s[i]
        b = s[i+1] if i + 1 < len(s) else 'X'

        if a == b:
            pairs.append(a + 'X')
            i += 1
        else:
            pairs.append(a + b)
            i += 2

    return pairs

def playfair(text, key, mode='encrypt'):
    mat = playfair_matrix(key)

    if not clean_letters(key):
        raise ValueError('Key Playfair harus berupa huruf.')

    if mode == 'encrypt':
        pairs = pair_text(text)
    else:
        clean_text = clean_letters(text).replace('J', 'I')
        pairs = [clean_text[i:i+2] for i in range(0, len(clean_text), 2)]

    if any(len(p) != 2 for p in pairs):
        raise ValueError('Ciphertext Playfair harus berjumlah genap.')

    result = []
    steps = []

    for p in pairs:
        a, b = p[0], p[1]
        r1, c1 = pos(mat, a)
        r2, c2 = pos(mat, b)

        if r1 == r2:
            shift = 1 if mode == 'encrypt' else -1
            x = mat[r1][(c1 + shift) % 5]
            y = mat[r2][(c2 + shift) % 5]
            rule = 'baris sama'
        elif c1 == c2:
            shift = 1 if mode == 'encrypt' else -1
            x = mat[(r1 + shift) % 5][c1]
            y = mat[(r2 + shift) % 5][c2]
            rule = 'kolom sama'
        else:
            x = mat[r1][c2]
            y = mat[r2][c1]
            rule = 'persegi panjang'

        result.append(x + y)
        steps.append(f"Pair {a}{b}: {rule}, posisi ({r1+1},{c1+1}) & ({r2+1},{c2+1}) -> {x}{y}")

    final_text = ''.join(result)

    if mode == 'decrypt':
        final_text = final_text.rstrip('X')

    return final_text, 'Aturan Playfair: baris sama, kolom sama, atau persegi panjang', steps, {
        'matrix': mat,
        'pairs': pairs
    }
