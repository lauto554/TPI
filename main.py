from functions.dependencias import verificar_dependencias


def main():
    if not verificar_dependencias():
        return
    from functions.menu import ejecutar_menu
    ejecutar_menu()


if __name__ == "__main__":
    main()
