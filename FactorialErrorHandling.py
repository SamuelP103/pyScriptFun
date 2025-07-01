import logging

logging.basicConfig(filename= 'logfile.txt',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#Add this to disable the logging after debugging
logging.disable(logging.CRITICAL)
logging.debug('Start of program')
# With the logging.debug it will put into the log file due to the 'filename=' above. 
# It will return only 120 in the end for printing since that is the last in the loop
def factorial(n):
    logging.debug('Start of factorial(' +str(n)+ ')')
    total = 1
    for i in range (1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) +' ' +'total is ' + str(total))
    logging.debug('End of factorial(' + str(n) + ')')
    return total


print(factorial(5))
logging.debug('End of program')