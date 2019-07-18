import argparse

'''
Skeleton code for a specific tool

Config Dir: .mo config file to process Pre & Post values
Input Dir: .csv file to be parsed for Pre & Post inputs

zip() for .csv Pre & Post values
'''

def main():
        args = _initArguments()

        if args.dir == None:
                if args.config != None:
                        print("Using config path:", args.config)
                        # Toggle a flag
                if args.input != None:
                        print("Using input path:", args.input)
                        # Toggle a flag
        else:
                print("Using directory:", args.dir)
                # Toggle a flag

        if args.split != None:
                print("Splitting .mo by folder:", args.dir)
                # Toggle a flag
 
def _initArguments() -> argparse.Namespace:
        parser = argparse.ArgumentParser(description='Script description: Replaces strings in a large file based on .csv columns.')

        parser.add_argument('-d', '--dir', type=str, help='Run script for all .mo files in folder')
        parser.add_argument('-c', '--config', type=str, help='Path of a single .mo config file')
        parser.add_argument('-i', '--input', type=str, help='Path of a single .csv input file')
        parser.add_argument('-s', '--split', type=str, help='Split output .mo files by folder per .csv specification')

        return parser.parse_args()

main()
