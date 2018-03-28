import rasterio
from types import FunctionType
#import matplotlib.pyplot as plt



# This function checks if the doi th user has supplied is invalid
def check_invalid_doi(doi):

    if ('10.' not in doi) or ('/' not in doi):
        invalid = True
    else:
        invalid = False

    return invalid

'''
This funtction asks the user for:
-The name of the file to be converted
-The doi of the dataset
-The doi of the publication

It also sanity-check the supplied information e.g. valid filetype,
And keeps asking until a reasonable answer has been provided.
'''
def info_from_user(valid_filetypes):

    # Ask the user for their filename
    # Keep asking until a valid file has been given
    
    ask = True
    while ask:

        # Get name from user
        filename = input('Input the filename. ')#'sample_data/subset_data_1/subset_data_1.tif'

        # Check a valid response has been given
        valid = True

        # Check the input is a file 
        if '.' not in filename:
            print('That is not a file.')
            valid = False

        # If it is a file check it's a valid file type
        else:
            filetype = filename[filename.rfind('.')+1:]
            if filetype not in valid_filetypes:
                valid = False
                print('Invalid filetype. Your filetype is ', filetype, '.\n\nValid filetypes are:', '\n\n\n', valid_filetypes)

        ask = not valid


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    # Ask the user for the doi of their dataset and publication
    # Keep asking until a valid dois has been given
    
    ask = True
    while ask:

        # Get doi from user
        doi_dataset = input('Input the dataset doi. ')
        ask = check_invalid_doi(doi_dataset)

    ask = True
    while ask:

        # Get doi from user
        doi_pub = input('Input the publication doi. ')
        ask = check_invalid_doi(doi_pub)

    return filename, doi_dataset, doi_pub

# List of valid filetypes
valid_filetypes = ['gen', 'thf', 'adf', 'blx', 'xlb', 'bag', 'bmp', 'kap',
                   'bt', 'doq', 'dt0', 'dt1', 'dt2', 'ers', 'n1', 'fits', 
                   'hdr', 'gif', 'grb', 'tif', 'img', 'mpr', 'mpl', 'mem', 
                   'jpg', 'jp2', 'j2k','ntf', 'nsf', 'grc', 'tab', 'grd',
                   'png', 'ppm', 'pgm', 'prf', 'rik', 'rsw', 'mtw', 'xml',
                   'safe', 'ter', 'TIL', 'vrt', 'xpm']

# Get required information from the user.
filename, doi_dataset, doi_pub = info_from_user(valid_filetypes)

