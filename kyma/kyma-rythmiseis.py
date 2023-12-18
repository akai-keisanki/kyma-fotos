# Kyma Rythmiseis Package For LuxOS 1.0 ( Unfinished )
# Kyma's Settings And Configuration For LuxOS 1.0

from lux_packages.kyma_mod_core import lux_pack as kymapack

class lux_pack:
  name="kyma-rythmiseis"
  version="1.0"
  aditionaldata={"datalist":[None]}
  def startscript():
    {}
  def pexcm(cmd, cliv):
    cliv2=cliv
    splitcmd=cmd.split(" ")
    r=1
    if splitcmd[0] == "k-r" or splitcmd[0] == "k-rythmiseis" or splitcmd[0] == "rythmiseis" or splitcmd[0] == "kyma-rythmiseis" or splitcmd[0] == "kyma-rythmiseis-kosmos":
      try:
        if splitcmd[1] == "#version":
          print("Κύμα Ρυθμίσεις 1.0 - \" Κόσμος \" with "+kymapack.packvars.kyma_fullname)
        elif splitcmd[1] == "update":
          print("Κύμα Ρυθμίσεις 1.0 - \" Κόσμος \"")
          print("To update \" kyma-rythmiseis \", input")
          print("\" fluctus packer fetch kyma-rythmiseis.py from akai-keisanki/kyma-fotos/All/kyma \"")
          print("On the command line interface.")
        elif splitcmd[1] == "help":
          print(" --- kyma help --- ")
          print("kyma-kosmos - kyma-rythmiseis main command")
      except:
          print(cmd+" >> kyma-rythmiseis-kosmos failed.")
    else:
      r=0
    return [cliv2, r]
  class packvars:
    {}
