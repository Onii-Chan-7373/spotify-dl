import os
def main():
    while True:
        link = input('Enter the link: ')
        options = input('Enter the options: ')
        print(f"./cli.js {link} --o ./songs --{options}")
        os.system(f"./cli.js ${link} --o ./songs --${options}")

if __name__ == '__main__':
    main()