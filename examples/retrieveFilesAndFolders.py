# Print all files / folders within a directory (using recursion)
# https://github.com/essejhsif

import os
 
def processFile(currentDir):
    ''' Process video files within this directory. '''
    # Get the absolute path of the currentDir parameter
    currentDir = os.path.abspath(currentDir)
 
    # Get a list of files in currentDir
    filesInCurDir = os.listdir(currentDir)
 
    # Traverse through all files
    for file in filesInCurDir:
        curFile = os.path.join(currentDir, file)
 
        # Check if it's a normal file or directory
        if os.path.isfile(curFile):
            # Get the file extension
            curFileExtension = curFile[-3:]
 
            # Check if the file has an extension of typical video files
            # if curFileExtension in ['avi', 'dat', 'mp4', 'mkv', 'vob']:
            # Increment the counter
            processFile.counter += 1
 
            # Print it's name
            print('\n%s' % curFile)
        else:
            # We got a directory, enter into it for further processing
            processFile(curFile)

if __name__ == '__main__':
    # Get the current working directory
    currentDir = os.getcwd()
 
    print('Starting processing in %s' % currentDir)
 
    # Set the number of processed files equal to zero
    processFile.counter = 0
 
    # Start Processing
    processFile(currentDir)
 
    # We are done. Exit now.
    print('\n -- %s Movie File(s) found in directory %s --' \
          % (processFile.counter, currentDir))
    print('\n Press ENTER to exit!')
 
    # Wait until the user presses enter/return
    input()
