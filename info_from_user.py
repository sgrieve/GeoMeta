# This function checks if a valid filename has been provided
def check_invalid_filename(filename):

    # List of valid filetypes
    valid_filetypes = ['gen', 'thf', 'adf', 'blx', 'xlb', 'bag', 'bmp', 'kap',
                   'bt', 'doq', 'dt0', 'dt1', 'dt2', 'ers', 'n1', 'fits', 
                   'hdr', 'gif', 'grb', 'tif', 'img', 'mpr', 'mpl', 'mem', 
                   'jpg', 'jp2', 'j2k','ntf', 'nsf', 'grc', 'tab', 'grd',
                   'png', 'ppm', 'pgm', 'prf', 'rik', 'rsw', 'mtw', 'xml',
                   'safe', 'ter', 'TIL', 'vrt', 'xpm']

    invalid = False

    # Check the input is a file 
    if '.' not in filename:
        print('\n\nThat is not a file.')
        invalid = True

    # If it is a file check it's a valid file type
    else:
        filetype = filename[filename.rfind('.')+1:]
        if filetype not in valid_filetypes:
            invalid = True
            print('\n\nInvalid filetype. Your filetype is ', filetype, '.\n\nValid filetypes are:', '\n\n', valid_filetypes)
    
    return invalid


# ________________________________________________


# This function checks if the doi the user has supplied is invalid
def check_invalid_doi(doi):

    if ('10.' not in doi) or ('/' not in doi):
        print('\n\nThat is an invalid doi, please supply a valid doi.')
        invalid = True
    else:
        invalid = False

    return invalid

# ________________________________________________

'''
This funtction asks the user for:
-The name of the file to be converted
-The doi of the dataset
-The doi of the publication

It also sanity-check the supplied information e.g. valid filetype,
And keeps asking until a reasonable answer has been provided.
'''
def info_from_user():

    # Ask the user for their filename
    # Keep asking until a valid file has been given
    
    ask = True
    while ask:

        # Get name from user
        filename = input('\n\nInput the filename. ')

        ask = check_invalid_filename(filename)

    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    # Ask the user for the doi of their dataset
    # Keep asking until a valid doi has been given
    
    ask = True
    while ask:

        # Get doi from user
        doi_dataset = input('\n\nInput the dataset doi. ')
        ask = check_invalid_doi(doi_dataset)


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    # Ask the user for the doi of their publication
    # Keep asking until a valid doi has been given
    ask = True
    while ask:

        # Get doi from user
        doi_pub = input('\n\nInput the publication doi. ')
        ask = check_invalid_doi(doi_pub)

    return filename, doi_dataset, doi_pub


# Get required information from the user.
filename, doi_dataset, doi_pub = info_from_user()

