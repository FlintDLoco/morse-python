from dictionary import DiccionarioMorse
morse_text = []

def main():
    start = "Traductor texto a morse\n"
    print("*" * len(start))
    print(start + "*" * len(start) + "\n")
    morse = input("Ingresa tu texto a morse: ").lower()
    for a in morse:
        if a in DiccionarioMorse:
            print(DiccionarioMorse[a], end=" ")
            morse_text.append("{} / {}".format(a, DiccionarioMorse[a]))
    print("\n")
    print("Texto a traducir: {}. Traduccion: {}\n".format(morse, morse_text))


if __name__ == "__main__":
    main()
