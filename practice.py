

# Main program logic follows:
if __name__ == '__main__':

    try:
        while True:
            alphabet = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            str1 = 'display_'

            for i in range(len(alphabet)):
                func_name = str1 + alphabet[i]
                print(func_name)
                # func_name(Color(150, 150, 150))

    except KeyboardInterrupt:
        print('done')
