import os, sys, traceback

def print_error(err_type, err_msg, err_tb) :
    fname = os.path.split(err_tb.tb_frame.f_code.co_filename)[1]
    lineno = str(err_tb.tb_lineno)
    print("")
    print("+--[ Exception | " + fname + ':' + lineno + " ]---------------------------------+")
    traceback.print_tb(err_tb)
    print( str(err_type) + ' : ' + str(err_msg))
    print("+------------------------------------------------------+")
    print("")
