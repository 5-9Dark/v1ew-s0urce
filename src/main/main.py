#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-
#
# =========================================================
# .________     /\  ________________                __    
# |   ____/    / / /   __   \______ \ _____ _______|  | __
# |____  \    / /  \____    /|    |  \\__  \\_  __ \  |/ /
# /       \  / /      /    / |    `   \/ __ \|  | \/    < 
#/______  / / /      /____/ /_______  (____  /__|  |__|_ \
#       \/  \/                      \/     \/           \/
#  - Made with <3 by the FiveNineDark Dev team  


import os
import sys
import random
import time

class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'

color_random=[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.UNDERLINE,color.LOGGING]
random.shuffle(color_random)

def clearScr():
    os.system('clear')

####################


