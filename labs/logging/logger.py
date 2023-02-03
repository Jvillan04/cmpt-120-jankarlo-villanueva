from datetime import datetime  # import your libraries here.


# the name of the log file to write to.
# Change this to be log-file-yyyy-mm-dd.log
log_file = "log-file-" + datetime.today().strftime('%Y-%m-%d') + ".log"


def log(text, log_file=log_file):
    # open up the log file in the correct mode.
    # 'a' stands for append, that way we only add to the file and not write over it.
    log_file = open(log_file, 'a')
    # create a string that has the current date and time in the beginning of the text. Syntax: datetime.today().strftime('%Y-%m-%d')
    # Ensure the string ends with a new line character. Syntax: /n
    # append the text to the end of the file.
    log_file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S') + text + '/n')
    # close the file.
    log_file.close()

    return None


def dump(log_file=log_file):
    '''
    This function prints out each line in the log file to the console
    '''
    log_file = open(log_file, 'r')  # open up the log file in the correct mode.
    loglist = []  # read the file into a list.
    # iterate through each item in the list and print out the results.
    log_file.read(loglist=log_file)
    for i in loglist:
        print(i)
    log_file.close()  # close the file.
    return None
