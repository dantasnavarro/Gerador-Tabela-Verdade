# ========================================================
# GERADOR DE TABELA-VERDADE 
# ========================================================

# ==================== FUNÇÃO 1 ====================
def verifica_parenteses(formula):
    """1) Verifica parênteses balanceados."""
    pilha = []
    for char in formula:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if not pilha:
                return False
            pilha.pop()
    return len(pilha) == 0


# ==================== FUNÇÃO 2 ====================
def eh_bem_formada(formula):
    """2) Verifica se a fórmula é bem-formada."""
    if not verifica_parenteses(formula):
        return False
    return True


# ==================== FUNÇÃO 3 ====================
def mostrar_proposicoes(formula):
    """3) Mostra proposições simples."""
    proposicoes = []
    for char in formula:
        if char.isalpha() and char.isupper() and char not in proposicoes:
            proposicoes.append(char)
    proposicoes.sort()
    print("Proposições simples:", proposicoes)
    return proposicoes


# ==================== FUNÇÃO 4 ====================
def tabela_verdade_combinacoes(n):
    """4) Mostra combinações de V/F."""
    cabecalho = " ".join([chr(65 + i) for i in range(n)])
    print(cabecalho)
    print("-" * (n * 4))
    total = 1 << n
    for i in range(total):
        linha = ['V' if (i & (1 << (n-1-j))) else 'F' for j in range(n)]
        print(" ".join(linha))


# ==================== FUNÇÃO 5 ====================
def tabela_verdade_conectivo(conectivo):
    """5) Tabela-verdade de um conectivo."""
    print(f"\nTabela do conectivo '{conectivo}':")
    for a in ['V','F']:
        for b in ['V','F']:
            if conectivo == '&':   res = 'V' if a==b=='V' else 'F'
            elif conectivo == '|': res = 'V' if a=='V' or b=='V' else 'F'
            elif conectivo == '->': res = 'F' if a=='V' and b=='F' else 'V'
            elif conectivo == '<-->': res = 'V' if a == b else 'F'
            else: res = '?'
            print(f"{a} {conectivo} {b} = {res}")


# ==================== AVALIADOR ROBUSTO (Melhorado) ====================
def avaliar_formula(formula, valores):
    """Avalia fórmula lógica de forma mais confiável."""
    expr = formula.replace(" ", "")
    
    # Substitui as proposições
    for p, v in valores.items():
        expr = expr.replace(p, '1' if v == 'V' else '0')
    
    # Substituições na ordem correta
    expr = expr.replace('<-->', ' == ')
    expr = expr.replace('->', ' <= ')
    expr = expr.replace('&', ' and ')
    expr = expr.replace('|', ' or ')
    
    # Trata negação (~)
    expr = expr.replace('~1', '0')
    expr = expr.replace('~0', '1')
    expr = expr.replace('~', 'not ')  # para casos restantes
    
    try:
        resultado = eval(expr, {"__builtins__": {}}, {})
        return 'V' if resultado else 'F'
    except:
        return 'ERRO'


# ==================== FUNÇÃO PRINCIPAL ====================
def tabela_verdade(formula):
    print(f"\n=== TABELA-VERDADE PARA: {formula} ===")
    
    if not eh_bem_formada(formula):
        print("ERRO: Fórmula mal formada!")
        return
    
    proposicoes = mostrar_proposicoes(formula)
    n = len(proposicoes)
    
    if n == 0:
        print("Nenhuma proposição.")
        return
    
    cabecalho = " ".join(proposicoes) + "   R"
    print(cabecalho)
    print("-" * len(cabecalho))
    
    total = 1 << n
    for i in range(total):
        valores = {}
        linha = []
        for j in range(n):
            val = 'V' if (i & (1 << (n - 1 - j))) else 'F'
            valores[proposicoes[j]] = val
            linha.append(val)
        
        resultado = avaliar_formula(formula, valores)
        linha.append(resultado)
        print(" ".join(linha))


# ==================== EXECUÇÃO ====================
if __name__ == "__main__":
    print("=== GERADOR DE TABELA-VERDADE ===\n")
    formula = input("Digite a fórmula: ").strip()
    
    if formula:
        tabela_verdade(formula)
    else:
        print("Rodando testes padrão...\n")
        testes = ["A&B", "A->B", "A<-->B", "~A", "((~A|B)&(A->~C))"]
        for f in testes:
            tabela_verdade(f)