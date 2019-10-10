from traxss import Menu

if __name__ == "__main__":
    try:
        menu = Menu()
        menu.start()
    except KeyboardInterrupt:
        exit()