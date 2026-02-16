from school_manager.menu import CLI

if __name__ == '__main__':
    menu = CLI()
    try:
        menu.run()
    except Exception as e:
        print(f'[ERROR] {e}')
        input('press ENTER to continue...')
        menu.run()


