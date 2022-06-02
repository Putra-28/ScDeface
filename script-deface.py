#WADUH WADUH DI INTIP DONG
#SCRIPTNYA GABUT GABUTAN KOK OM 
#PAKEK AJA CUY 
#NTAR DI UPDATE TAMPILAN HTML NYA KOK
#JANGAN NANGIS 🗿

import os, sys, time
HEADER = '\033[95m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
CYAN = '\033[96m'
RESET = '\033[0m'
def scv1():
  os.system('clear')
  logo = f'''{CYAN}
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  {RED}  ━━━━━━━━━━ {GREEN}SCRIPT DEFACE{RED} ━━━━━━━━━━━━
     ━━━━━━━━━━━ {YELLOW}By.putra{RED} ━━━━━━━━━━━━━━
  {CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  '''
  print(logo)
  title = input(HEADER+"Heacked By.: ")
  nama = input("Nama Samaran : ")
  color_name = input("Warna Teks : ")
  background = input("Warna Background : ")
  link_foto = input("Kirim Link Foto Kamu : ")
  teks = input("Ketik Teks/Kata Kata (ketik <br> untuk baris baru) : ")
  team = input("Nama-Nama Team : ")
  name_file = input(YELLOW+"Nama File : ")
  
  time.sleep(2)
  file = open(f"{name_file}.html", 'a')
  file.write(f'<html><head><title>HEACKED BY.'+title+'</title><style>body{background: '+background+';font-family: Courier;align-items: center;text-align: center;background-position: center;background-repeat: no-repeat;}.judul{position: relative;font-size: 25px;color: '+color_name+';text-shadow: 2px 2px 5px red;font-family: comic;top: 30px;}.foto{position: relative;top: 80px;width: 100%;overflow: hidden;}.paragraf{position: relative;color: white;overflow: scroll;width: 100%;height: 250px;}marquee{position: relative;color: #3ff7ff;font-size: 19px;float: right;top: 0;}.mar{font-size: 20px;color: red;float: left;}</style></head><body><div class="judul"><label class="judul"><b>'+nama+'</b></label></div><div class="foto"><img width="200px" height="200px" src="'+link_foto+'" alt="" /><div class="paragraf"><p align="center">'+teks+'</p></div></div><label class="mar"><b>MY TEAM :</b></label><marquee width="65%" height="35px" direction="right">'+team+'</marquee></body></html>')
  print(CYAN+"DONE FILE SUDAH TERSIMPAN... /sdcard/"+name_file)
##########################################
################# START ##################
##########################################
os.system('clear')
mulai = input(f"{RED}enter {RESET}untuk melanjutkan ke {CYAN}menu{GREEN}...")
if mulai == "":
  scv1(name_file)
  os.system('mv -t '+name_file+' /sdcard && rm -rf '+name_file)
