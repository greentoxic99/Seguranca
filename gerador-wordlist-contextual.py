import itertools # Pode ser útil se quiser combinar geradores

def generate_contextual_wordlist(base_username, year_range=(2020, 2025), common_suffixes=["1", "123", "!", "!?"]):
    """
    Gera senhas baseadas em um username base e padrões comuns.
    """
    username_lower = base_username.lower()
    username_capital = base_username.capitalize()
    username_upper = base_username.upper()

    # Variações básicas
    yield username_lower
    yield username_capital
    yield username_upper

    # Comuns combinações com números e anos
    for suffix in common_suffixes:
        yield f"{username_lower}{suffix}"
        yield f"{username_capital}{suffix}"
        yield f"{username_upper}{suffix}"

    for year in range(year_range[0], year_range[1] + 1):
        yield f"{username_lower}{year}"
        yield f"{username_capital}{year}"
        yield f"{username_upper}{year}"
        yield f"{username_lower}{year}!?" # Exemplo com símbolo
        yield f"{username_capital}{year}!"

    # Adicionar senhas comuns/default para "admin" (extrair de listas populares)
    # Esta lista é um exemplo, você pode usar listas mais completas
    common_admin_passwords = ["admin", "password", "123456", "letmein", "welcome", "qwerty", "abc123", "iloveyou", "admin123"]
    for pwd in common_admin_passwords:
         yield pwd

# --- Bloco para executar o gerador e salvar em arquivo ---
if __name__ == "__main__":
    # --- CONFIGURAÇÃO DO GERADOR ---
    target_username = "admin" # O username base do seu alvo
    output_filename = "contextual_passwords.txt" # Nome do arquivo de saída

    # Parametros do gerador (opcionais, use defaults se não mudar)
    current_year = 2025
    years_to_include = [current_year, current_year - 1, current_year + 1, 2020, 2021, 2022, 2023, 2024] # Anos específicos
    # Converter para range min/max se usar year_range
    min_year = min(years_to_include) if years_to_include else 2020
    max_year = max(years_to_include) if years_to_include else 2025

    suffixes = ["1", "123", "!", "?!", "@", "#", "$"] # Sufixos comuns

    # --- EXECUÇÃO ---
    print(f"Generating contextual wordlist for username '{target_username}'...")

    # Crie o gerador
    # Você pode usar year_range=(min_year, max_year) OU iterar sobre years_to_include manualmente se quiser anos não sequenciais
    # Vamos usar o year_range como no código original para simplicidade:
    contextual_generator = generate_contextual_wordlist(
        base_username=target_username,
        year_range=(min_year, max_year), # Exemplo usando min/max dos anos_a_incluir
        common_suffixes=suffixes
    )

    # Opcional: Combine com outro gerador ou lista (ex: senhas de uma wordlist pequena/media)
    # from your_other_wordlist_module import load_smaller_list
    # other_passwords_generator = load_smaller_list("small_common.txt")
    # combined_generator = itertools.chain(contextual_generator, other_passwords_generator)
    # generator_to_write = combined_generator
    generator_to_write = contextual_generator # Usando apenas o gerador contextual

    # Escreva as senhas no arquivo
    try:
        with open(output_filename, "w", encoding="utf-8") as f:
            count = 0
            for password in generator_to_write:
                f.write(password + "\n")
                count += 1
        print(f"Successfully generated {count} passwords to '{output_filename}'")
    except Exception as e:
        print(f"An error occurred while writing the wordlist: {e}")