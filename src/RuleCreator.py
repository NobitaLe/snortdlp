'''
Created on May 11, 2010

@author: Will, Tyler
'''

def addSnortRule(file, string):
    
    #open the snort file location for appending
    snortFile = open(file,'a')
    sid = 1000000 + len(snortFile.readlines()) + 1
    

def createRegex(string):
    """
    Input: string of standardized input to create the regex from
    Output: regex we can plug into a Snort rule
    
    ToDo: write the method
    """
    
    return ""