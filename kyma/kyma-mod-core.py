# Kyma Mod Core Package For LuxOS 1.0 ( Unfinished )
# Kyma's Modification Core For LuxOS 1.0 And Main Scripts

class lux_pack:
  name="kyma-mod-core"
  version="1.0"
  aditionaldata={"datalist":[None]}
  def startscript():
    print("\n--- > Κύμα < ---\n")
  def pexcm(cmd, cliv):
    cliv2=cliv
    splitcmd=cmd.split(" ")
    r=1
    if splitcmd[0] == "kyma" or splitcmd[0] == "kyma-kosmos":
      try:
        if self.splitcmd[1] == "#version":
          print("Κύμα 1.0 - \" Κόσμος\"")
        elif self.splitcmd[1] == "update":
          print("Κύμα 1.0 - \" Κόσμος\"")
          print("Updating to: Unknown")
          print("The updating system is broken")
      except:
          print(cmd+" >> kyma-kosmos failed.")
    elif splitcmd[0] == "kosmos" or splitcmd[0] == "kosmos-kosmos":
      try:
        if self.splitcmd[1] == "#version":
          print("Κόσμος 1.0 - \" Κόσμος\"")
        elif self.splitcmd[1] == "":
          print("Κόσμος 1.0 - \" Κόσμος\"")
      except:
          print(cmd+" >> kosmos-kosmos failed.")
    else:
      r=0
    return [cliv2, r]
  class packvars:
    kyma_name="Κύμα"
    kyma_codename="Κόσμος"
