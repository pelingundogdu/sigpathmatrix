
# def print_sigprimednet_banner():
#     text = "sigPrimedNet_PBK"
# patterns = { 's':["  sss  "," s     "," s     ","  sss  ","     s ","     s ","  sss  "],
#         'i':["   i   ","   i   ","   i   ","   i   ","   i   ","   i   ","   i   ",""],
#         'g':["  ggg  "," g   g "," g     ",    " g  gg "," g   g "," g   g ",    "  ggg  "],
#         'P':[" PPPP  "," P   P "," P   P "," PPPP  "," P     "," P     "," P     ",""],
#         'r':[" rrr   "," r   r "," r   r "," rrr   "," r r   "," r  r  "," r   r ",""],
#         'i':["   i   ","   i   ","   i   ",        "   i   ","   i   ","   i   ","   i   "],
#         'm':[" m   m "," mm mm "," m m m "," m   m "," m   m ",   " m   m "," m   m "],
#         'e':[" eeee  "," e     "," e     "," eeee  "," e     "," e     "," eeee  "],
#         'd':["    d  ","    d  ","    d  "," dddd  "," d   d "," d   d "," dddd  "],
#         'N':[" N   N "," NN  N "," N N N "," N  NN "," N   N "," N   N "," N   N "],
#         # 'e':[" eee   "," e   e "," e     "," eeee  "," e     "," e   e "," eee   ",""],
#         'e':[" eeee  "," e     "," e     "," eeee  "," e     "," e     "," eeee  "],
#         't':[" ttt   ","  t    ","  t    ","  t    ","  t    ","  t    ","  t    "],
#         '_':["       ","       ","       ","       ","       ","       ","_______"],
#         'P':[" PPPP  "," P   P "," P   P "," PPPP  "," P     ",   " P     "," P     "],
#         'B':[" BBB   "," B   B "," B   B "," BBB   "," B   B "," B   B "," BBB   "],
#         'K':[" K   K "," K  K  "," K K   "," KK    "," K K   ",    " K  K  "," K   K "]
#         }


patterns = {
        's': ["  sss  ", " s   s ", " s     ", "  sss  ", "     s ", " s   s ", "  sss  "," "],
        'i': ["   i   ", "   i   ", "   i   ", "   i   ", "   i   ", "   i   ", "   i   "," "],
        'g': ["  ggg  ", " g   g ", " g     ", " g  gg ", " g   g ", " g   g ", "  ggg  "," "],
        'p': [" pppp  ", " p   p ", " p   p ", " pppp  ", " p     ", " p     ", " p     "," "],
        'a': ["  aaa  ", " a   a ", " a   a ", " aaaaa ", " a   a ", " a   a ", " a   a "," "],
        't': ["  ttt  ", "   t   ", "   t   " ,"   t   " ,"   t   " ,"   t   ", "   t   "," "],
        'h': [" h   h ", " h   h ", " h   h ", " hhhhh ", " h   h ", " h   h ", " h   h "," "],
        'm': [" m   m ", " mm mm ", " m m m ", " m   m ", " m   m ", " m   m ", " m   m "," "],
        'r': [" rrr   ", " r   r ", " r   r ", " rrr   ", " r r   ", " r  r  ", " r   r "," "],
        'x': [" x   x ", " x   x ", "  x x  ", "   x   ", "  x x  ", " x   x ", " x   x "," "],
    }

def print_sigpathmatrix_banner():
    # text = "sigPrimedNet_PBK"
    text = "sigpathmatrix"
    
    # Each letter represented as a 5x7 matrix using the actual letter
    def get_letter_pattern(ch):
        return patterns.get(ch, ['     '] * 7)
    
    print('\n')
    # Print the banner
    for row in range(7):
        line = ""
        for char in text:
            pattern = get_letter_pattern(char)
            line += pattern[row] + " "  # 1 spaces between letters
        print(line)

    print('\n')