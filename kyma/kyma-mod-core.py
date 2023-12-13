# Kyma Mod Core Package For LuxOS 1.0 ( Unfinished )
# Kyma's Modification Core For LuxOS 1.0 And Main Scripts

class lux_pack:
  name="kyma-mod-core"
  version="1.0"
  aditionaldata={"datalist":[None]}
  def startscript():
    print("\n--- > Κύμα < ---\n")
  def pexcm(cmd, cliv):
    try:
      cliv["vars"]["kosmos"]
    except:
      cliv["vars"]["kosmos"] = "none"
    cliv2=cliv
    splitcmd=cmd.split(" ")
    r=1
    if splitcmd[0] == "kyma" or splitcmd[0] == "kyma-kosmos":
      try:
        if splitcmd[1] == "#version":
          print("Κύμα 1.0 - \" Κόσμος \"")
        elif splitcmd[1] == "update":
          print("Κύμα 1.0 - \" Κόσμος \"")
          print("To update \" kyma-mod-core \", input")
          print("\" fluctus packer fetch kyma-mod-core.py from akai-keisanki/kyma-fotos/All/kyma \"")
          print("On the command line interface.")
          print("The updating system is a work in progress.")
        elif splitcmd[1] == "help":
          print(" --- kyma help --- ")
          print("kyma-kosmos - kyma main command")
          print("kosmos-kosmos - kyma administration system")
        elif splitcmd[1] == "get-packs":
          print("Κύμα 1.0 - \" Κόσμος \"")
          print("To get all packs from kyma, input")
          print("\" fluctus packer fetch kyma-mod-core.py from akai-keisanki/kyma-fotos/All/kyma &&& fluctus packer fetch kyma-rythmiseis.py from akai-keisanki/kyma-fotos/All/kyma \"")
          print("On the command line interface.")
          print("The kyma pack installer system is a work in progress.")
      except:
          print(cmd+" >> kyma-kosmos failed.")
    elif splitcmd[0] == "kosmos" or splitcmd[0] == "kosmos-kosmos":
      try:
        if splitcmd[1] == "#version":
          print("Κόσμος 1.0 - \" Κόσμος \"")
        elif splitcmd[1] == "turn-on":
          cliv2["vars"]["kosmos"] = "kosmos-kosmos"
        elif splitcmd[1] == "check":
          print("Kosmos: "+cliv["vars"]["kosmos"])
      except:
          print(cmd+" >> kosmos-kosmos failed.")
    else:
      r=0
    return [cliv2, r]
  class packvars:
    kyma_name="Κύμα"
    kyma_codename="Κόσμος"
