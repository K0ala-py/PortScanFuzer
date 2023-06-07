import socket
import sys
from datetime import datetime
import threading
from rich import print
from rich.console import Console
from rich.style import Style

console = Console()


#-------------------------------------------
#     SYNTAX CODE AT LINE:   269
#-------------------------------------------

# TOTAL PORT : 65.535
# TIME TO SCAN ALL PORTS : 8 minutes and 30 seconds 


def p1_50():      # Port from 0 at 50 
  for port in range(1,50):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    
    connection = s.connect_ex((ip,port))
    #if connection != 0:
    #  print('Port: {}'.format(port))
    if connection == 0:
      print('[dark_goldenrod]Port :',port,'      [red]Status : [green]Open')

def p51_100():    # Port from 51 at 100
  for port in range(51,100):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)

    connection = s.connect_ex((ip,port))
    #if connection != 0:
    #  print('Port: {}'.format(port))
    if connection == 0:
      print('[dark_goldenrod]Port :',port,'      [red]Status : [green]Open')

def p101_150():    
  for port in range(101,150):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)

    connection = s.connect_ex((ip,port))
    #if connection != 0:
    #  print('Port: {}'.format(port))
    if connection == 0:
      print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')


def p151_200():    
  for port in range(151,200):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)

    connection = s.connect_ex((ip,port))
    #if connection != 0:
    #  print('Port: {}'.format(port))
    if connection == 0:
      print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def p201_250():    
  for port in range(201,250):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)

    connection = s.connect_ex((ip,port))
    #if connection != 0:
    #  print('Port: {}'.format(port))
    if connection == 0:
      print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def p251_300():    
  for port in range(251,300):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)

    connection = s.connect_ex((ip,port))
    #if connection != 0:
    #  print('Port: {}'.format(port))
    if connection == 0:
      print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def p301_350():    
  for port in range(301,350):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)

    connection = s.connect_ex((ip,port))
    #if connection != 0:
    #  print('Port: {}'.format(port))
    if connection == 0:
      print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def p351_400():    
  for port in range(351,400):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)

    connection = s.connect_ex((ip,port))
    #if connection != 0:
    #  print('Port: {}'.format(port))
    if connection == 0:
      print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def p401_450():    
  for port in range(401,450):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)

    connection = s.connect_ex((ip,port))
    #if connection != 0:
    #  print('Port: {}'.format(port))
    if connection == 0:
      print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def p451_500():    
  for port in range(451,500):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)

    connection = s.connect_ex((ip,port))
    #if connection != 0:
    #  print('Port: {}'.format(port))
    if connection == 0:
      print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def p501_550():    
  for port in range(501,550):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)

    connection = s.connect_ex((ip,port))
    #if connection != 0:
    #  print('Port: {}'.format(port))
    if connection == 0:
      print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def p551_600():    
  for port in range(551,600):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)

    connection = s.connect_ex((ip,port))
    #if connection != 0:
    #  print('Port: {}'.format(port))
    if connection == 0:
      print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def p601_650():   
  for port in range(601,650):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)

    connection = s.connect_ex((ip,port))
    #if connection != 0:
    #  print('Port: {}'.format(port))
    if connection == 0:
      print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def p651_700():    
  for port in range(651,700):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)

    connection = s.connect_ex((ip,port))
    #if connection != 0:
    #  print('Port: {}'.format(port))
    if connection == 0:
      print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def p701_750():    
  for port in range(701,750):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)

    connection = s.connect_ex((ip,port))
    #if connection != 0:
    #  print('Port: {}'.format(port))
    if connection == 0:
      print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def p751_800():    
  for port in range(751,800):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)

    connection = s.connect_ex((ip,port))
    #if connection != 0:
    #  print('Port: {}'.format(port))
    if connection == 0:
      print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def p801_850():    
  for port in range(801,850):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)

    connection = s.connect_ex((ip,port))
    #if connection != 0:
    #  print('Port: {}'.format(port))
    if connection == 0:
      print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def p851_900():   
  for port in range(851,900):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)

    connection = s.connect_ex((ip,port))
    #if connection != 0:
    #  print('Port: {}'.format(port))
    if connection == 0:
      print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def p901_950():   
  for port in range(901,950):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)

    connection = s.connect_ex((ip,port))
    #if connection != 0:
    #  print('Port: {}'.format(port))
    if connection == 0:
      print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def p951_1000():    
  for port in range(951,1000):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)

    connection = s.connect_ex((ip,port))
    #if connection != 0:
    #  print('Port: {}'.format(port))
    if connection == 0:
      print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

######
#OTHER
######

def port1001_1501():
    for port in range(1001,1501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
          print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port1501_2001():
    for port in range(1501,2001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
          print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port2001_2501():
    for port in range(2001,2501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
          print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port2501_3001():
    for port in range(2501,3001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
          print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port3001_3501():
    for port in range(3001,3501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
          print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port3501_4001():
    for port in range(3501,4001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
          print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port4001_4501():
    for port in range(4001,4501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
          print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port4501_5001():
    for port in range(4501,5001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
          print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port5001_5501():
    for port in range(5001,5501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
          print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port5501_6001():
    for port in range(5501,6001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
          print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port6001_6501():
    for port in range(6001,6501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
          print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port6501_7001():
    for port in range(6501,7001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
          print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port7001_7501():
    for port in range(7001,7501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
          print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port7501_8001():
    for port in range(7501,8001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
          print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port8001_8501():
    for port in range(8001,8501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
          print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port8501_9001():
    for port in range(8501,9001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
          print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port9001_9501():
    for port in range(9001,9501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
          print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port9501_10001():
    for port in range(9501,10001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
          print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port10001_10501():
    for port in range(10001,10501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port10501_11001():
    for port in range(10501,11001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port11001_11501():
    for port in range(11001,11501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port11501_12001():
    for port in range(11501,12001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port12001_12501():
    for port in range(12001,12501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port12501_13001():
    for port in range(12501,13001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port13001_13501():
    for port in range(13001,13501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port13501_14001():
    for port in range(13501,14001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port14001_14501():
    for port in range(14001,14501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port14501_15001():
    for port in range(14501,15001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port15001_15501():
    for port in range(15001,15501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port15501_16001():
    for port in range(15501,16001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port16001_16501():
    for port in range(16001,16501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port16501_17001():
    for port in range(16501,17001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port17001_17501():
    for port in range(17001,17501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port17501_18001():
    for port in range(17501,18001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port18001_18501():
    for port in range(18001,18501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port18501_19001():
    for port in range(18501,19001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port19001_19501():
    for port in range(19001,19501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port19501_20001():
    for port in range(19501,20001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port20001_20501():
    for port in range(20001,20501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port20501_21001():
    for port in range(20501,21001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port21001_21501():
    for port in range(21001,21501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port21501_22001():
    for port in range(21501,22001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port22001_22501():
    for port in range(22001,22501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port22501_23001():
    for port in range(22501,23001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port23001_23501():
    for port in range(23001,23501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port23501_24001():
    for port in range(23501,24001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port24001_24501():
    for port in range(24001,24501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port24501_25001():
    for port in range(24501,25001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port25001_25501():
    for port in range(25001,25501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port25501_26001():
    for port in range(25501,26001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port26001_26501():
    for port in range(26001,26501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port26501_27001():
    for port in range(26501,27001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port27001_27501():
    for port in range(27001,27501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port27501_28001():
    for port in range(27501,28001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port28001_28501():
    for port in range(28001,28501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port28501_29001():
    for port in range(28501,29001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port29001_29501():
    for port in range(29001,29501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port29501_30001():
    for port in range(29501,30001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port30001_30501():
    for port in range(30001,30501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port30501_31001():
    for port in range(30501,31001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port31001_31501():
    for port in range(31001,31501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port31501_32001():
    for port in range(31501,32001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port32001_32501():
    for port in range(32001,32501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port32501_33001():
    for port in range(32501,33001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port33001_33501():
    for port in range(33001,33501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port33501_34001():
    for port in range(33501,34001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port34001_34501():
    for port in range(34001,34501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port34501_35001():
    for port in range(34501,35001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port35001_35501():
    for port in range(35001,35501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port35501_36001():
    for port in range(35501,36001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port36001_36501():
    for port in range(36001,36501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port36501_37001():
    for port in range(36501,37001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port37001_37501():
    for port in range(37001,37501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port37501_38001():
    for port in range(37501,38001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port38001_38501():
    for port in range(38001,38501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port38501_39001():
    for port in range(38501,39001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port39001_39501():
    for port in range(39001,39501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port39501_40001():
    for port in range(39501,40001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port40001_40501():
    for port in range(40001,40501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port40501_41001():
    for port in range(40501,41001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port41001_41501():
    for port in range(41001,41501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port41501_42001():
    for port in range(41501,42001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port42001_42501():
    for port in range(42001,42501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port42501_43001():
    for port in range(42501,43001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port43001_43501():
    for port in range(43001,43501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port43501_44001():
    for port in range(43501,44001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port44001_44501():
    for port in range(44001,44501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port44501_45001():
    for port in range(44501,45001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port45001_45501():
    for port in range(45001,45501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port45501_46001():
    for port in range(45501,46001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port46001_46501():
    for port in range(46001,46501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port46501_47001():
    for port in range(46501,47001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port47001_47501():
    for port in range(47001,47501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port47501_48001():
    for port in range(47501,48001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port48001_48501():
    for port in range(48001,48501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port48501_49001():
    for port in range(48501,49001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port49001_49501():
    for port in range(49001,49501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port49501_50001():
    for port in range(49501,50001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port50001_50501():
    for port in range(50001,50501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port50501_51001():
    for port in range(50501,51001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port51001_51501():
    for port in range(51001,51501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port51501_52001():
    for port in range(51501,52001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port52001_52501():
    for port in range(52001,52501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port52501_53001():
    for port in range(52501,53001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port53001_53501():
    for port in range(53001,53501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port53501_54001():
    for port in range(53501,54001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port54001_54501():
    for port in range(54001,54501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port54501_55001():
    for port in range(54501,55001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port55001_55501():
    for port in range(55001,55501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port55501_56001():
    for port in range(55501,56001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port56001_56501():
    for port in range(56001,56501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port56501_57001():
    for port in range(56501,57001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port57001_57501():
    for port in range(57001,57501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port57501_58001():
    for port in range(57501,58001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port58001_58501():
    for port in range(58001,58501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port58501_59001():
    for port in range(58501,59001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port59001_59501():
    for port in range(59001,59501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port59501_60001():
    for port in range(59501,60001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port60001_60501():
    for port in range(60001,60501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port60501_61001():
    for port in range(60501,61001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port61001_61501():
    for port in range(61001,61501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port61501_62001():
    for port in range(61501,62001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port62001_62501():
    for port in range(62001,62501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port62501_63001():
    for port in range(62501,63001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port63001_63501():
    for port in range(63001,63501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port63501_64001():
    for port in range(63501,64001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port64001_64501():
    for port in range(64001,64501):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port64501_65001():
    for port in range(64501,65001):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port65001_65535():
    for port in range(65001,65535):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        connection = s.connect_ex((ip,port))
        if connection == 0:
            print('[dark_goldenrod]Port :',port,'     [red]Status : [green]Open')

def port_scan():
  threading.Thread(target=p1_50).start()
  threading.Thread(target=p51_100).start()
  threading.Thread(target=p101_150).start()
  threading.Thread(target=p151_200).start()
  threading.Thread(target=p201_250).start()
  threading.Thread(target=p251_300).start()
  threading.Thread(target=p301_350).start()
  threading.Thread(target=p351_400).start()
  threading.Thread(target=p401_450).start()
  threading.Thread(target=p451_500).start()
  threading.Thread(target=p501_550).start()
  threading.Thread(target=p551_600).start()
  threading.Thread(target=p601_650).start()
  threading.Thread(target=p651_700).start()
  threading.Thread(target=p701_750).start()
  threading.Thread(target=p751_800).start()
  threading.Thread(target=p801_850).start()
  threading.Thread(target=p851_900).start()
  threading.Thread(target=p901_950).start()
  threading.Thread(target=p951_1000).start()

  # OTHER PORTS
  threading.Thread(target=port1001_1501).start()
  threading.Thread(target=port1501_2001).start()
  threading.Thread(target=port2001_2501).start()
  threading.Thread(target=port2501_3001).start()
  threading.Thread(target=port3001_3501).start()
  threading.Thread(target=port3501_4001).start()
  threading.Thread(target=port4001_4501).start()
  threading.Thread(target=port4501_5001).start()
  threading.Thread(target=port5001_5501).start()
  threading.Thread(target=port5501_6001).start()
  threading.Thread(target=port6001_6501).start()
  threading.Thread(target=port6501_7001).start()
  threading.Thread(target=port7001_7501).start()
  threading.Thread(target=port7501_8001).start()
  threading.Thread(target=port8001_8501).start()
  threading.Thread(target=port8501_9001).start()
  threading.Thread(target=port9001_9501).start()
  threading.Thread(target=port9501_10001).start()
  threading.Thread(target=port10001_10501).start()
  threading.Thread(target=port10501_11001).start()
  threading.Thread(target=port11001_11501).start()
  threading.Thread(target=port11501_12001).start()
  threading.Thread(target=port12001_12501).start()
  threading.Thread(target=port12501_13001).start()
  threading.Thread(target=port13001_13501).start()
  threading.Thread(target=port13501_14001).start()
  threading.Thread(target=port14001_14501).start()
  threading.Thread(target=port14501_15001).start()
  threading.Thread(target=port15001_15501).start()
  threading.Thread(target=port15501_16001).start()
  threading.Thread(target=port16001_16501).start()
  threading.Thread(target=port16501_17001).start()
  threading.Thread(target=port17001_17501).start()
  threading.Thread(target=port17501_18001).start()
  threading.Thread(target=port18001_18501).start()
  threading.Thread(target=port18501_19001).start()
  threading.Thread(target=port19001_19501).start()
  threading.Thread(target=port19501_20001).start()
  threading.Thread(target=port20001_20501).start()
  threading.Thread(target=port20501_21001).start()
  threading.Thread(target=port21001_21501).start()
  threading.Thread(target=port21501_22001).start()
  threading.Thread(target=port22001_22501).start()
  threading.Thread(target=port22501_23001).start()
  threading.Thread(target=port23001_23501).start()
  threading.Thread(target=port23501_24001).start()
  threading.Thread(target=port24001_24501).start()
  threading.Thread(target=port24501_25001).start()
  threading.Thread(target=port25001_25501).start()
  threading.Thread(target=port25501_26001).start()
  threading.Thread(target=port26001_26501).start()
  threading.Thread(target=port26501_27001).start()
  threading.Thread(target=port27001_27501).start()
  threading.Thread(target=port27501_28001).start()
  threading.Thread(target=port28001_28501).start()
  threading.Thread(target=port28501_29001).start()
  threading.Thread(target=port29001_29501).start()
  threading.Thread(target=port29501_30001).start()
  threading.Thread(target=port30001_30501).start()
  threading.Thread(target=port30501_31001).start()
  threading.Thread(target=port31001_31501).start()
  threading.Thread(target=port31501_32001).start()
  threading.Thread(target=port32001_32501).start()
  threading.Thread(target=port32501_33001).start()
  threading.Thread(target=port33001_33501).start()
  threading.Thread(target=port33501_34001).start()
  threading.Thread(target=port34001_34501).start()
  threading.Thread(target=port34501_35001).start()
  threading.Thread(target=port35001_35501).start()
  threading.Thread(target=port35501_36001).start()
  threading.Thread(target=port36001_36501).start()
  threading.Thread(target=port36501_37001).start()
  threading.Thread(target=port37001_37501).start()
  threading.Thread(target=port37501_38001).start()
  threading.Thread(target=port38001_38501).start()
  threading.Thread(target=port38501_39001).start()
  threading.Thread(target=port39001_39501).start()
  threading.Thread(target=port39501_40001).start()
  threading.Thread(target=port40001_40501).start()
  threading.Thread(target=port40501_41001).start()
  threading.Thread(target=port41001_41501).start()
  threading.Thread(target=port41501_42001).start()
  threading.Thread(target=port42001_42501).start()
  threading.Thread(target=port42501_43001).start()
  threading.Thread(target=port43001_43501).start()
  threading.Thread(target=port43501_44001).start()
  threading.Thread(target=port44001_44501).start()
  threading.Thread(target=port44501_45001).start()
  threading.Thread(target=port45001_45501).start()
  threading.Thread(target=port45501_46001).start()
  threading.Thread(target=port46001_46501).start()
  threading.Thread(target=port46501_47001).start()
  threading.Thread(target=port47001_47501).start()
  threading.Thread(target=port47501_48001).start()
  threading.Thread(target=port48001_48501).start()
  threading.Thread(target=port48501_49001).start()
  threading.Thread(target=port49001_49501).start()
  threading.Thread(target=port49501_50001).start()
  threading.Thread(target=port50001_50501).start()
  threading.Thread(target=port50501_51001).start()
  threading.Thread(target=port51001_51501).start()
  threading.Thread(target=port51501_52001).start()
  threading.Thread(target=port52001_52501).start()
  threading.Thread(target=port52501_53001).start()
  threading.Thread(target=port53001_53501).start()
  threading.Thread(target=port53501_54001).start()
  threading.Thread(target=port54001_54501).start()
  threading.Thread(target=port54501_55001).start()
  threading.Thread(target=port55001_55501).start()
  threading.Thread(target=port55501_56001).start()
  threading.Thread(target=port56001_56501).start()
  threading.Thread(target=port56501_57001).start()
  threading.Thread(target=port57001_57501).start()
  threading.Thread(target=port57501_58001).start()
  threading.Thread(target=port58001_58501).start()
  threading.Thread(target=port58501_59001).start()
  threading.Thread(target=port59001_59501).start()
  threading.Thread(target=port59501_60001).start()
  threading.Thread(target=port60001_60501).start()
  threading.Thread(target=port60501_61001).start()
  threading.Thread(target=port61001_61501).start()
  threading.Thread(target=port61501_62001).start()
  threading.Thread(target=port62001_62501).start()
  threading.Thread(target=port62501_63001).start()
  threading.Thread(target=port63001_63501).start()
  threading.Thread(target=port63501_64001).start()
  threading.Thread(target=port64001_64501).start()
  threading.Thread(target=port64501_65001).start()
  threading.Thread(target=port65001_65535).start()

t1 = datetime.now()


try:
  target = sys.argv[1]
  ip = socket.gethostbyname(target)
  
  base_style = Style.parse("blue")
  console.print("""
   ____                  ____            _   _____                   
  / ___|  ___ __ _ _ __ |  _ \ ___  _ __| |_|  ___|   _ _______ _ __ 
  \___ \ / __/ _` | '_ \| |_) / _ \| '__| __| |_ | | | |_  / _ \ '__|
   ___) | (_| (_| | | | |  __/ (_) | |  | |_|  _|| |_| |/ /  __/ |   
  |____/ \___\__,_|_| |_|_|   \___/|_|   \__|_|   \__,_/___\___|_|   
                                            
  """,style=base_style + Style(bold=True))

  if target:
    print('[orange3]-'*50)
    print('[yellow]Scanning       :',ip)
    print('[yellow]Start at       :',t1)
    print('[orange3]-'*50)
    print('\n[dark_violet]Scanning...')
    port_scan()

except IndexError:
  print("Missing target")


# SYNTAX CODE:    python portscan.py  <IP or site(ex. www.google.com)>