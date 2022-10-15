import random
import getopt, sys
import numpy as np
import matplotlib.pyplot as plt

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

def get_int(modif=0):
    return random.randint(155+modif, 255)

def get_col(modif):
    col = np.array([get_int(modif[0]), get_int(), get_int(modif[1])])
    return tuple(col.astype(int))

def make_color_plot(colors):
    plt.bar(range(1,len(colors)+1), 10, color=colors)
    try:
        plt.savefig('generated_pastel_colors.png')
    except Exception as e:
        print(e)
        
def generate_color_list(num_c=10):
    r = 0
    colors = []
    ratio = round(100/num_c)
    for i in range(num_c):    
        colors.append('#'+rgb_to_hex(get_col([r, -r])))
        r += ratio
        
    return colors

def main():
    num_c = 10
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:", ["number"])
    except getopt.GetoptError:
        # print help information and exit:
        print('args.py -n <number of colors>')
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o == "-n":
            num_c = int(a)
            

    colors = generate_color_list(num_c)
    make_color_plot(colors)
    try:
        with open('Pastel_colors.txt', 'w') as fin:
            for c in colors:
                fin.write(c+'\n')
    except Exception as e:
        print(e)
    

if __name__ == '__main__':
    main()
    