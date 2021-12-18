import os
import distutils.dir_util
import shutil
import sys
import time

run_prog = True
lay_path = ''
img_path = ''
mart_dir = ''
bios_dir = ''
rom_dir = ''


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def main_funk():
    global lay_path, img_path, mart_dir, bios_dir, rom_dir

    bios_list = []
    rom_list = []

    for root, dirs, files in os.walk(bios_dir):
        for file in files:
            if file.endswith('.zip'):
                print('-- found bios:', file)
                bios_list.append(file)
    print('-- found', len(bios_list), 'bios files')

    for root, dirs, files in os.walk(rom_dir):
        for file in files:
            if not file in bios_list and file.endswith('.zip'):
                print('-- found rom:', file)
                rom_list.append(file)
    print('-- found', len(rom_list), 'roms files')

    skipped = []

    distutils.dir_util.mkpath(mart_dir + '\\' + 'MAME_BEZEL_GENERATOR')
    shutil.copyfile(img_path, mart_dir + '\\' + 'MAME_BEZEL_GENERATOR\\' + 'mame_bezel_generator.png')

    i = 0
    for _ in rom_list:
        new_path = mart_dir + '\\' + _.replace('.zip', '')
        print(i, '/', len(rom_list), '-- creating & populating artwork directory:', new_path)

        try:
            distutils.dir_util.mkpath(new_path)
            shutil.copyfile(lay_path, new_path+'\\default.lay')
        except:
            print('-- error creating/populating:', new_path, '. skipping..')
            skipped.append(new_path)
        i += 1
    print('\nskipped:', len(skipped))
    for _ in skipped:
        print('skipped:', _)


def help_message():
    print('')
    print('-' * 100)
    print(' ' * 44 + 'MAME BEZEL GENERATOR')
    print('')
    print('Creates directories matching ROM names in MAME artwork directory and populates the new directories')
    print('with lay files that point to one single artwork file.')
    print('')
    print('Information:')
    print('    A. Please backup your MAME installation before using this program.')
    print('    B. Please do not modify the included lay file unless you keep tag <image file> unaltered or you')
    print('       know what you are doing.')
    print('    C. Please ensure artwork png specified is called "mame_bezel_generator.png".')
    print('    D. Creating Theme Directories recommended for almost instantly changing the bezel accross all')
    print('       roms. To easily change between themes include the following in a directory and configure')
    print('       a configuration file:')
    print('        1. default.lay')
    print('        2. mame_bezel_generator.png')
    print('        3. mame_bezel_generator_configuration.txt (This file can be called anything you like).')
    print('')
    print('Configuration File:')
    print('    1. Enter full path to desired .lay file.')
    print('    2. Enter full path to desired image file.')
    print('    3. Enter MAME installation artwork directory path.')
    print('    4. Enter a MAME BIOS directory path that contasins only BIOS files (Crucial for distinguishing')
    print('       between ROMs and BIOSs so that artwork is only generated for ROMs).')
    print('    5. Finally enter MAME installation ROM directory path.')
    print('')
    print('Example Configuration File:')
    print('    LAY: C:\\default.lay')
    print('    IMG: C:\\mame_bezel_generator.png')
    print('    DIR_ART: C:\\Programs\\MAME\\artwork')
    print('    DIR_BIOS: C:\\Archives\\MAME\\BIOS_v0.237\\MAME (bios-devices)\\MAME (bios-devices)')
    print('    DIR_ROM: D:\\Programs\\MAME\\roms')
    print('')
    print('Create/Change Bezels For all ROMS:')
    print('    mame_bezel_generator.exe -c any_configuration_file_name.txt')
    print('')
    print('Command Line Arguments:')
    print('    -c                  Specifies configuration file [-c file].')
    print('    --make-defalut-lay  Creates the default lay file for this program (Recommended if missing or overwritten).')
    print('    -h                  Displays a help message')
    print('-' * 100)
    print('')


def default_lay():
    v_0 = '<!-- HorizontalTemplate.lay -->'
    v_1 = ''
    v_2 = '<mamelayout version="2">'
    v_3 = ''
    v_4 = '  <element name="Artwork_1">'
    v_5 = '    <image file="../MAME_BEZEL_GENERATOR/mame_bezel_generator.png" />'
    v_6 = '  </element>'
    v_7 = ''
    v_8 = '   <view name="Full">'
    v_9 = '    <screen index="0">'
    v_10 = '      <bounds x="240" y="0" width="1440" height="1080" />'
    v_11 = '    </screen>'
    v_12 = ''
    v_13 = '    <bezel element="Artwork_1">'
    v_14 = '      <bounds x="0" y="0" width="1920" height="1080" />'
    v_15 = '    </bezel>'
    v_16 = '  </view>'
    v_17 = ''
    v_18 = '</mamelayout>'
    lines_to_file = [v_0, v_1, v_2, v_3, v_4, v_5, v_6, v_7, v_8, v_9, v_10, v_11, v_12, v_13, v_14, v_15, v_16, v_17, v_18]
    specify_output_dir = input('Save location directory: ')
    if os.path.exists(specify_output_dir):
        out_f = specify_output_dir + '\\default.lay'
        with open(out_f, 'w') as fo:
            for _ in lines_to_file:
                print('-- writing:', _)
                fo.write(_+'\n')
        fo.close()


try:
    cfg = ''

    if len(sys.argv) == 1:
        print('\n-- unspecified arguments\n')

    i = 0
    for _ in sys.argv:

        if _ == '-c':
            if len(sys.argv) > i + 1:
                cfg = sys.argv[i + 1]
                break

        elif _ == '--make-default-lay':
            print('-- running make default lay file')
            default_lay()
            break

        elif _ == '-h':
            help_message()
            break

        i += 1

    if os.path.exists(cfg):
        print('-- found configuration file:', cfg)
        with open(cfg, 'r') as fo:
            for line in fo:
                line = line.strip()
                if line.startswith('LAY: '):
                    line = line.replace('LAY: ', '')
                    lay_path = line

                if line.startswith('IMG: '):
                    line = line.replace('IMG: ', '')
                    img_path = line

                if line.startswith('DIR_ART: '):
                    line = line.replace('DIR_ART: ', '')
                    mart_dir = line

                if line.startswith('DIR_BIOS: '):
                    line = line.replace('DIR_BIOS: ', '')
                    bios_dir = line

                if line.startswith('DIR_ROM: '):
                    line = line.replace('DIR_ROM: ', '')
                    rom_dir = line
        fo.close()

        if os.path.exists(lay_path) and os.path.exists(img_path) and os.path.exists(mart_dir) and os.path.exists(bios_dir) and os.path.exists(rom_dir):
            print('\nConfiguration Entries:')
            print('LAY:', lay_path)
            print('IMG:', img_path)
            print('DIR_ART:', mart_dir)
            print('DIR_BIOS:', bios_dir)
            print('DIR_ROM:', rom_dir)

            usr_accept = input('\nDo you wish to continue? (y/n): ')
            if usr_accept == 'y' or usr_accept == 'Y':
                main_funk()
            else:
                print('-- quitting')
                time.sleep(2)

except Exception as e:
    print(e)

print('')
