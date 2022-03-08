# Necessary imports.
import os
import subprocess
from subprocess import Popen, PIPE


# Creating the "Program" Class.
class Program:
    def __init__(self):
        # Show an example.
        print('''\n    Write your resolution:
        Examples:
        Width: 1920
        Height: 1080
        Refresh Rate: 60\n''')

        # Variables for everything.
        self.width = int(input('''    Width: '''))
        self.height = int(input('''    Height: '''))
        self.refresh_rate = int(input('''    Refresh Rate: '''))
        
        # Calling the function that adds a new mode
        self.new_mode(self.width, self.height, self.refresh_rate)
    

    # Function for create a new mode with the resolution settings.
    def new_mode(self, width, height, refresh_rate):
        # Starting with the CVT command.
        self.var_subprocess = subprocess.Popen(f'cvt {width} {height} {refresh_rate}', shell=True, stdout=subprocess.PIPE)
        
        # Getting the output.
        self.var_subprocess_read = self.var_subprocess.stdout.read()

        # Translating for string.
        self.var_subprocess_decode = self.var_subprocess_read.decode()

        # Split the string.
        self.var_subprocess_split = self.var_subprocess_decode.splitlines()
        self.lines = self.var_subprocess_decode.splitlines()
        
        # Final result
        modeline = self.lines[1].lstrip("Modeline")
        os.system(f'''xrandr --newmode{modeline}''')

        # For the resolution.
        self.resolution = (f'''"{self.width}x{self.height}_{self.refresh_rate}.00"''')
        
        # Calling the function that add mode and change the resolution.
        self.change_res(self.resolution)


    # Function for create and change the resolution.
    def change_res(self, resolution):
        # Adding and changing the resolution. 
        os.system(f'''
        xrandr --addmode Virtual1 {resolution};
        xrandr --output Virtual1 --mode {resolution}''')

        print(f'''
        xrandr --addmode Virtual1 {resolution};
        xrandr --output Virtual1 --mode {resolution}''')

        
        # For know if the script is working.
        print(f'\n    All commands done! Changed resolution for {resolution}.\n')


# Will only run if it is the main program.
if __name__ == "__main__":
    run = Program()
