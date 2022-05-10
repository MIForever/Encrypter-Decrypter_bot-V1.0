def encrypter(word):
    cipher = ''
    for letter in word:
        if letter == '0':
            cipher+='01'
        elif letter == '1':
            cipher+='02'
        elif letter == '2':
            cipher+='03'
        elif letter == '3':
            cipher+='04'
        elif letter == '4':
            cipher+='05'
        elif letter == '5':
            cipher+='06'
        elif letter == '6':
            cipher+='07'
        elif letter == '7':
            cipher+='08'
        elif letter == '8':
            cipher+='09'
        elif letter == '9':
            cipher+='10'
        elif letter=='A':
            cipher+='11'
        elif letter=='B':
            cipher+='12'
        elif letter=='C':
            cipher+='13'
        elif letter=='D':
            cipher+='14'
        elif letter=='E':
            cipher+='15'
        elif letter=='F':
            cipher+='16'
        elif letter=='G':
            cipher+='17'
        elif letter=='H':
            cipher+='18'
        elif letter=='I':
            cipher+='19'
        elif letter=='J':
            cipher+='20'
        elif letter=='K':
            cipher+='21'
        elif letter=='L':
            cipher+='22'
        elif letter=='M':
            cipher+='23'
        elif letter=='N':
            cipher+='24'
        elif letter=='O':
            cipher+='25'
        elif letter=='P':
            cipher+='26'
        elif letter=='Q':
            cipher+='27'
        elif letter=='R':
            cipher+='28'
        elif letter=='S':
            cipher+='29'
        elif letter=='T':
            cipher+='30'
        elif letter=='U':
            cipher+='31'
        elif letter=='V':
            cipher+='32'
        elif letter=='W':
            cipher+='33'
        elif letter=='X':
            cipher+='34'
        elif letter=='Y':
            cipher+='35'
        elif letter=='Z':
            cipher+='36'
        elif letter=='a':
            cipher+='37'
        elif letter=='b':
            cipher+='38'
        elif letter=='c':
            cipher+='39'
        elif letter=='d':
            cipher+='40'
        elif letter=='e':
            cipher+='41'
        elif letter=='f':
            cipher+='42'
        elif letter=='g':
            cipher+='43'
        elif letter=='h':
            cipher+='44'
        elif letter=='i':
            cipher+='45'
        elif letter=='j':
            cipher+='46'
        elif letter=='k':
            cipher+='47'
        elif letter=='l':
            cipher+='48'
        elif letter=='m':
            cipher+='49'
        elif letter=='n':
            cipher+='50'
        elif letter=='o':
            cipher+='51'
        elif letter=='p':
            cipher+='52'
        elif letter=='q':
            cipher+='53'
        elif letter=='r':
            cipher+='54'
        elif letter=='s':
            cipher+='55'
        elif letter=='t':
            cipher+='56'
        elif letter=='u':
            cipher+='57'
        elif letter=='v':
            cipher+='58'
        elif letter=='w':
            cipher+='59'
        elif letter=='x':
            cipher+='60'
        elif letter=='y':
            cipher+='61'
        elif letter=='z':
            cipher+='62'
        elif letter=='@':
            cipher+='63'
        elif letter=='#':
            cipher+='64'
        elif letter=='$':
            cipher+='65'
        elif letter=='_':
            cipher+='66'
        elif letter=='&':
            cipher+='67'
        elif letter=='-':
            cipher+='68'
        elif letter=='+':
            cipher+='69'
        elif letter=='(':
            cipher+='71'
        elif letter==')':
            cipher+='72'
        elif letter=='/':
            cipher+='73'
        elif letter=='*':
            cipher+='74'
        elif letter=='"':
            cipher+='75'
        elif letter=="'":
            cipher+='76'
        elif letter==':':
            cipher+='77'
        elif letter==';':
            cipher+='78'
        elif letter=='!':
            cipher+='79'
        elif letter=='?':
            cipher+='80'
        elif letter=='~':
            cipher+='81'
        elif letter=='`':
            cipher+='82'
        elif letter=='|':
            cipher+='83'
        elif letter=='^':
            cipher+='84'
        elif letter=='=':
            cipher+='85'
        elif letter=='{':
            cipher+='86'
        elif letter=='}':
            cipher+='87'
        elif letter=="\t":
            cipher+='88'
        elif letter=='[':
            cipher+='89'
        elif letter==']':
            cipher+='90'
        elif letter=='>':
            cipher+='91'
        elif letter=='<':
            cipher+='92'
        elif letter==' ':
            cipher+='93'
        elif letter=='\n':
            cipher+='94'
        elif letter=='.':
            cipher+='95'
        elif letter==',':
            cipher+='96'
        else:
            cipher="In the message is not used only Latin letters or there's Emoji❌😃"
            break
    return cipher
def decrypter(cipher):
    message=''
    cipx=0
    cipex=2
    while True:
        cip=cipher[cipx:cipex]
        if cip == '01':
            message+='0'
        elif cip == '02':
            message+='1'
        elif cip == '03':
            message+='2'
        elif cip == '04':
            message+='3'
        elif cip == '05':
            message+='4'
        elif cip == '06':
            message+='5'    
        elif cip=='07':
            message+='6'
        elif cip == '08':
            message+='7'
        elif cip == '09':
            message+='8'
        elif cip == '10':
            message+='9'
        elif cip=='11':
            message+='A'
        elif cip=='12':
            message+='B'
        elif cip=='13':
            message+='C'
        elif cip=='14':
            message+='D'
        elif cip=='15':
            message+='E'
        elif cip=='16':
            message+='F'
        elif cip=='17':
            message+='G'
        elif cip=='18':
            message+='H'
        elif cip=='19':
            message+='I'
        elif cip=='20':
            message+='J'
        elif cip=='21':
            message+='K'
        elif cip=='22':
            message+='L'
        elif cip=='23':
            message+='M'
        elif cip=='24':
            message+='N'
        elif cip=='25':
            message+='O'
        elif cip=='26':
            message+='P'
        elif cip=='27':
            message+='Q'
        elif cip=='28':
            message+='R'
        elif cip=='29':
            message+='S'
        elif cip=='30':
            message+='T'
        elif cip=='31':
            message+='U'
        elif cip=='32':
            message+='V'
        elif cip=='33':
            message+='W'
        elif cip=='34':
            message+='X'
        elif cip=='35':
            message+='Y'
        elif cip=='36':
            message+='Z'
        elif cip=='37':
            message+='a'
        elif cip=='38':
            message+='b'
        elif cip=='39':
            message+='c'
        elif cip=='40':
            message+='d'
        elif cip=='41':
            message+='e'
        elif cip=='42':
            message+='f'
        elif cip=='43':
            message+='g'
        elif cip=='44':
            message+='h'
        elif cip=='45':
            message+='i'
        elif cip=='46':
            message+='j'
        elif cip=='47':
            message+='k'
        elif cip=='48':
            message+='l'
        elif cip=='49':
            message+='m'
        elif cip=='50':
            message+='n'
        elif cip=='51':
            message+='o'
        elif cip=='52':
            message+='p'
        elif cip=='53':
            message+='q'
        elif cip=='54':
            message+='r'
        elif cip=='55':
            message+='s'
        elif cip=='56':
            message+='t'
        elif cip=='57':
            message+='u'
        elif cip=='58':
            message+='v'
        elif cip=='59':
            message+='w'
        elif cip=='60':
            message+='x'
        elif cip=='61':
            message+='y'
        elif cip=='62':
            message+='z'
        elif cip=='63':
            message+='@'
        elif cip=='64':
            message+='#'
        elif cip=='65':
            message+='$'
        elif cip=='66':
            message+='_'
        elif cip=='67':
            message+='&'
        elif cip=='68':
            message+='-'
        elif cip=='69':
            message+='+'
        elif cip=='71':
            message+='('
        elif cip=='72':
            message+=')'
        elif cip=='73':
            message+='/'
        elif cip=='74':
            message+='*'
        elif cip=='75':
            message+='"'
        elif cip=='76':
            message+="'"
        elif cip=='77':
            message+=':'
        elif cip=='78':
            message+=';'
        elif cip=='79':
            message+='!'
        elif cip=='80':
            message+='?'
        elif cip=='81':
            message+='~'
        elif cip=='82':
            message+='`'
        elif cip=='83':
            message+='|'
        elif cip=='84':
            message+='^'
        elif cip=='85':
            message+='='
        elif cip=='86':
            message+='{'
        elif cip=='87':
            message+='}'
        elif cip=='88':
            message+='\t'
        elif cip=='89':
            message+='['
        elif cip=='90':
            message+=']'
        elif cip=='91':
            message+='>'
        elif cip=='92':
            message+='<'
        elif cip=='93':
            message+=' '
        elif cip=='94':
            message+='\n'
        elif cip=='95':
            message+='.'
        elif cip=='96':
            message+=','
        else:
            message='Error!!! Invalid cipher!!!'
            break
        if len(cipher)==cipex:
            break
        cipx+=2
        cipex+=2
    return message
