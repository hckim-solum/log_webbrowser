import webbrowser


def print_h(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    url = 'http://blindfish.tistory.com'

    webbrowser.open(url)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_h('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
