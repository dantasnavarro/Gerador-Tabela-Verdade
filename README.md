# 🧠 Gerador de Tabela-Verdade

Projeto desenvolvido em Python para gerar tabelas-verdade de fórmulas da lógica proposicional.

## 📋 Funcionalidades

- Verificação de parênteses balanceados
- Verificação básica de fórmulas bem-formadas
- Identificação automática das proposições simples
- Geração de combinações de valores verdade (V/F)
- Exibição da tabela-verdade de conectivos lógicos
- Avaliação automática de fórmulas lógicas completas
- Geração da tabela-verdade final com resultado da expressão

## 🔧 Conectivos Suportados

| Símbolo | Operação |
|----------|----------|
| `~` | Negação |
| `&` | Conjunção (E) |
| `|` | Disjunção (OU) |
| `->` | Implicação |
| `<-->` | Bicondicional |

## 🚀 Como Executar

1. Certifique-se de ter o Python instalado.
2. Baixe o arquivo do projeto.
3. Abra o terminal na pasta do arquivo.
4. Execute:

```bash
python "GERADOR DE TABELA-VERDADE.py"
```

## 💡 Exemplo de Entrada

```text
((~A|B)&(A->~C))
```

## 📊 Exemplo de Saída

```text
A B C   R
---------
V V V   F
V V F   V
V F V   F
V F F   F
F V V   V
F V F   V
F F V   V
F F F   V
```

## 📁 Estrutura do Projeto

- `verifica_parenteses()` → Verifica parênteses balanceados.
- `eh_bem_formada()` → Valida a fórmula.
- `mostrar_proposicoes()` → Identifica proposições simples.
- `tabela_verdade_combinacoes()` → Gera combinações V/F.
- `tabela_verdade_conectivo()` → Mostra tabela de um conectivo.
- `avaliar_formula()` → Avalia a expressão lógica.
- `tabela_verdade()` → Gera a tabela-verdade completa.

## 🎓 Aplicação

Projeto voltado para estudos de:

- Lógica Proposicional
- Matemática Discreta
- Ciência da Computação
- Sistemas de Informação
- Engenharia de Software

## 👨‍💻 Autor

Akira Yuki
Aguida Yasmin
Lais Navarro

---

Projeto acadêmico desenvolvido para estudo e prática de lógica computacional. 
