# Kyma Rythmiseis Package For LuxOS 1.0 ( Unfinished )
# Kyma's Settings And Configuration For LuxOS 1.0

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
          print("Κύμα Ρυθμίσεις 1.0 - \" Κόσμος \"")
      except:
          print(cmd+" >> kyma-rythmiseis-kosmos failed.")
    else:
      r=0
    return [cliv2, r]
  class packvars:
    kyma_name="Κύμα"
    kyma_codename="Κόσμος"