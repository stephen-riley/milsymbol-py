from ..metadata import metadata as metadata_letter
from ..geticons import geticons as getIcons_letter
from ...iconparts.tactical_points import tacticalPoints as iconParts
from ..labels.tactical_points_2525 import tactical_points_2525 as labels


def tactical_points_2525(ms, sId, bbox, icn, _STD2525):
    # Tactical Point Symbols =========================================================================
    sId["G-T-D-----"] = icn["TP.DESTROY"]  # TACGRP.TSK.DSTY
    bbox["G-T-D-----"] = {"x1": 0, "x2": 200, "y1": 40, "y2": 160}
    sId["G-T-I-----"] = icn["TP.INTERDICT"]  # TACGRP.TSK.ITDT
    bbox["G-T-I-----"] = {"x1": 0, "x2": 200, "y1": 40, "y2": 160}
    sId["G-T-N-----"] = icn["TP.NEUTRALIZE"]  # TACGRP.TSK.NEUT
    bbox["G-T-N-----"] = {"x1": 0, "x2": 200, "y1": 40, "y2": 160}
    sId["G-G-GPUUD-"] = icn["TP.DATUM"]  # TACGRP.C2GM.GNL.PNT.USW.UH2.DTM
    bbox["G-G-GPUUD-"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-G-GPUUB-"] = icn["TP.BRIEF CONTACT"]  # TACGRP.C2GM.GNL.PNT.USW.UH2.BCON
    bbox["G-G-GPUUB-"] = {"x1": 50, "x2": 150, "y1": 0, "y2": 100}
    sId["G-G-GPUUL-"] = icn["TP.LOST CONTACT"]  # TACGRP.C2GM.GNL.PNT.USW.UH2.LCON
    bbox["G-G-GPUUL-"] = {"x1": 50, "x2": 150, "y1": 0, "y2": 100}
    sId["G-G-GPUUS-"] = icn["TP.SINKER"]  # TACGRP.C2GM.GNL.PNT.USW.UH2.SNK
    bbox["G-G-GPUUS-"] = {"x1": 50, "x2": 150, "y1": 0, "y2": 100}
    sId["G-G-GPUY--"] = icn["TP.SONOBUOY"]  # TACGRP.C2GM.GNL.PNT.USW.SNBY
    bbox["G-G-GPUY--"] = {"x1": 60, "x2": 140, "y1": -10, "y2": 160}
    sId["G-G-GPUYP-"] = icn[
        "TP.SONOBUOY PATTERN CENTER"
    ]  # TACGRP.C2GM.GNL.PNT.USW.SNBY.PTNCTR
    bbox["G-G-GPUYP-"] = {"x1": 60, "x2": 140, "y1": -10, "y2": 160}
    sId["G-G-GPUYD-"] = icn["TP.SONOBUOY DIFAR"]  # TACGRP.C2GM.GNL.PNT.USW.SNBY.DIFAR
    bbox["G-G-GPUYD-"] = {"x1": 60, "x2": 140, "y1": -10, "y2": 160}
    sId["G-G-GPUYL-"] = icn["TP.SONOBUOY LOFAR"]  # TACGRP.C2GM.GNL.PNT.USW.SNBY.LOFAR
    bbox["G-G-GPUYL-"] = {"x1": 60, "x2": 140, "y1": -10, "y2": 160}
    sId["G-G-GPUYC-"] = icn["TP.SONOBUOY CASS"]  # TACGRP.C2GM.GNL.PNT.USW.SNBY.CASS
    bbox["G-G-GPUYC-"] = {"x1": 60, "x2": 140, "y1": -10, "y2": 160}
    sId["G-G-GPUYS-"] = icn["TP.SONOBUOY DICASS"]  # TACGRP.C2GM.GNL.PNT.USW.SNBY.DICASS
    bbox["G-G-GPUYS-"] = {"x1": 60, "x2": 140, "y1": -10, "y2": 160}
    sId["G-G-GPUYB-"] = icn["TP.SONOBUOY BT"]  # TACGRP.C2GM.GNL.PNT.USW.SNBY.BT
    bbox["G-G-GPUYB-"] = {"x1": 60, "x2": 140, "y1": -10, "y2": 160}
    sId["G-G-GPUYA-"] = icn["TP.SONOBUOY ANM"]  # TACGRP.C2GM.GNL.PNT.USW.SNBY.ANM
    bbox["G-G-GPUYA-"] = {"x1": 60, "x2": 140, "y1": -10, "y2": 160}
    sId["G-G-GPUYV-"] = icn["TP.SONOBUOY VLAD"]  # TACGRP.C2GM.GNL.PNT.USW.SNBY.VLAD
    bbox["G-G-GPUYV-"] = {"x1": 60, "x2": 140, "y1": -10, "y2": 160}
    sId["G-G-GPUYT-"] = icn["TP.SONOBUOY ATAC"]  # TACGRP.C2GM.GNL.PNT.USW.SNBY.ATAC
    bbox["G-G-GPUYT-"] = {"x1": 60, "x2": 140, "y1": -10, "y2": 160}
    sId["G-G-GPUYR-"] = icn["TP.SONOBUOY RO"]  # TACGRP.C2GM.GNL.PNT.USW.SNBY.RO
    bbox["G-G-GPUYR-"] = {"x1": 60, "x2": 140, "y1": -10, "y2": 160}
    sId["G-G-GPUYK-"] = icn["TP.SONOBUOY KINGPIN"]  # TACGRP.C2GM.GNL.PNT.USW.SNBY.KGP
    bbox["G-G-GPUYK-"] = {"x1": 60, "x2": 140, "y1": -10, "y2": 160}
    sId["G-G-GPUYX-"] = icn["TP.SONOBUOY EXPIRED"]  # TACGRP.C2GM.GNL.PNT.USW.SNBY.EXP
    bbox["G-G-GPUYX-"] = {"x1": 40, "x2": 160, "y1": -10, "y2": 160}
    sId["G-G-GPUS--"] = icn["TP.SEARCH"]  # TACGRP.C2GM.GNL.PNT.USW.SRH
    bbox["G-G-GPUS--"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-G-GPUSA-"] = icn["TP.SEARCH AREA"]  # TACGRP.C2GM.GNL.PNT.USW.SRH.ARA
    bbox["G-G-GPUSA-"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-G-GPUSD-"] = icn["TP.DIP POSITION"]  # TACGRP.C2GM.GNL.PNT.USW.SRH.DIPPSN
    bbox["G-G-GPUSD-"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-G-GPUSC-"] = icn["TP.SEARCH CENTER"]  # TACGRP.C2GM.GNL.PNT.USW.SRH.CTR
    bbox["G-G-GPUSC-"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-G-GPR---"] = icn["TP.REFERENCE POINT"]  # TACGRP.C2GM.GNL.PNT.REFPNT
    bbox["G-G-GPR---"] = {"x1": 40, "x2": 160, "y1": 40, "y2": 160}
    sId["G-G-GPRN--"] = icn[
        "TP.NAVIGATIONAL REFERENCE"
    ]  # TACGRP.C2GM.GNL.PNT.REFPNT.NAVREF
    bbox["G-G-GPRN--"] = {"x1": 40, "x2": 160, "y1": 40, "y2": 160}
    sId["G-G-GPRS--"] = icn["TP.SPECIAL POINT"]  # TACGRP.C2GM.GNL.PNT.REFPNT.SPLPNT
    bbox["G-G-GPRS--"] = {"x1": 40, "x2": 160, "y1": 40, "y2": 160}
    sId["G-G-GPRD--"] = icn["TP.DLRP"]  # TACGRP.C2GM.GNL.PNT.REFPNT.DLRP
    bbox["G-G-GPRD--"] = {"x1": 40, "x2": 160, "y1": 40, "y2": 160}
    sId["G-G-GPRP--"] = icn[
        "TP.POINT OF INTENDED MOVEMENT"
    ]  # TACGRP.C2GM.GNL.PNT.REFPNT.PIM
    bbox["G-G-GPRP--"] = {"x1": 40, "x2": 160, "y1": 40, "y2": 160}
    sId["G-G-GPRM--"] = icn["TP.MARSHALL POINT"]  # TACGRP.C2GM.GNL.PNT.REFPNT.MRSH
    bbox["G-G-GPRM--"] = {"x1": 40, "x2": 160, "y1": 40, "y2": 160}
    sId["G-G-GPRW--"] = icn[
        "TP.REFERENCE POINT WAYPOINT"
    ]  # TACGRP.C2GM.GNL.PNT.REFPNT.WAP
    bbox["G-G-GPRW--"] = {"x1": 40, "x2": 160, "y1": 40, "y2": 160}
    sId["G-G-GPRC--"] = icn["TP.CORRIDOR TAB"]  # TACGRP.C2GM.GNL.PNT.REFPNT.CRDRTB
    bbox["G-G-GPRC--"] = {"x1": 40, "x2": 160, "y1": 40, "y2": 160}
    sId["G-G-GPRI--"] = icn["TP.POINT OF INTEREST"]  # TACGRP.C2GM.GNL.PNT.REFPNT.PNTINR
    bbox["G-G-GPRI--"] = {"x1": 50, "x2": 150, "y1": -25}
    sId["G-G-GPWA--"] = icn["TP.AIM POINT"]  # TACGRP.C2GM.GNL.PNT.WPN.AIMPNT
    bbox["G-G-GPWA--"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-G-GPWD--"] = icn["TP.DROP POINT"]  # TACGRP.C2GM.GNL.PNT.WPN.DRPPNT
    bbox["G-G-GPWD--"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 120}
    sId["G-G-GPWE--"] = icn["TP.ENTRY POINT"]  # TACGRP.C2GM.GNL.PNT.WPN.ENTPNT
    bbox["G-G-GPWE--"] = {"x1": 50, "x2": 150, "y1": 50}
    sId["G-G-GPWG--"] = icn["TP.GROUND ZERO"]  # TACGRP.C2GM.GNL.PNT.WPN.GRDZRO
    bbox["G-G-GPWG--"] = {"x1": 50, "x2": 150, "y1": 30}
    sId["G-G-GPWM--"] = icn["TP.MSL DETECT POINT"]  # TACGRP.C2GM.GNL.PNT.WPN.MSLPNT
    bbox["G-G-GPWM--"] = {"x1": 50, "x2": 150, "y1": 30}
    sId["G-G-GPWI--"] = icn["TP.IMPACT POINT"]  # TACGRP.C2GM.GNL.PNT.WPN.IMTPNT
    bbox["G-G-GPWI--"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-G-GPWP--"] = icn[
        "TP.PREDICTED IMPACT POINT"
    ]  # TACGRP.C2GM.GNL.PNT.WPN.PIPNT
    bbox["G-G-GPWP--"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-G-GPF---"] = icn["TP.FORMATION"]  # TACGRP.C2GM.GNL.PNT.FRMN
    bbox["G-G-GPF---"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-G-GPH---"] = icn["TP.HARBOR"]  # TACGRP.C2GM.GNL.PNT.HBR
    bbox["G-G-GPH---"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-G-GPHQ--"] = icn["TP.HARBOR POINT Q"]  # TACGRP.C2GM.GNL.PNT.HBR.PNTQ
    bbox["G-G-GPHQ--"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-G-GPHA--"] = icn["TP.HARBOR POINT A"]  # TACGRP.C2GM.GNL.PNT.HBR.PNTA
    bbox["G-G-GPHA--"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-G-GPHY--"] = icn["TP.HARBOR POINT Y"]  # TACGRP.C2GM.GNL.PNT.HBR.PNTY
    bbox["G-G-GPHY--"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-G-GPHX--"] = icn["TP.HARBOR POINT X"]  # TACGRP.C2GM.GNL.PNT.HBR.PNTX
    bbox["G-G-GPHX--"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-G-GPO---"] = icn["TP.ROUTE"]  # TACGRP.C2GM.GNL.PNT.RTE
    bbox["G-G-GPO---"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 140}
    sId["G-G-GPOZ--"] = icn["TP.ROUTE RENDEZVOUS"]  # TACGRP.C2GM.GNL.PNT.RTE.RDV
    bbox["G-G-GPOZ--"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 170}
    sId["G-G-GPOD--"] = icn["TP.ROUTE DIVERSIONS"]  # TACGRP.C2GM.GNL.PNT.RTE.DVSN
    bbox["G-G-GPOD--"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 170}
    sId["G-G-GPOW--"] = icn["TP.ROUTE WAYPOINT"]  # TACGRP.C2GM.GNL.PNT.RTE.WAP
    bbox["G-G-GPOW--"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 170}
    sId["G-G-GPOP--"] = icn["TP.ROUTE PIM"]  # TACGRP.C2GM.GNL.PNT.RTE.PIM
    bbox["G-G-GPOP--"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 170}
    sId["G-G-GPOR--"] = icn["TP.ROUTE POINT R"]  # TACGRP.C2GM.GNL.PNT.RTE.PNTR
    bbox["G-G-GPOR--"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 170}
    sId["G-G-GPA---"] = icn["TP.AIR CONTROL POINT"]  # TACGRP.C2GM.GNL.PNT.ACTL
    bbox["G-G-GPA---"] = {"x1": 60, "x2": 140, "y1": 40, "y2": 160}
    sId["G-G-GPAP--"] = icn[
        "TP.COMBAT AIR PATROL (CAP)"
    ]  # TACGRP.C2GM.GNL.PNT.ACTL.CAP
    bbox["G-G-GPAP--"] = {"x1": 60, "x2": 140, "y1": 40, "y2": 160}
    sId["G-G-GPAW--"] = icn[
        "TP.AIRBORNE EARLY WARNING (AEW)"
    ]  # TACGRP.C2GM.GNL.PNT.ACTL.ABNEW
    bbox["G-G-GPAW--"] = {"x1": 60, "x2": 140, "y1": 40, "y2": 160}
    sId["G-G-GPAK--"] = icn["TP.TANKING"]  # TACGRP.C2GM.GNL.PNT.ACTL.TAK
    bbox["G-G-GPAK--"] = {"x1": 60, "x2": 140, "y1": 40, "y2": 160}
    sId["G-G-GPAA--"] = icn["TP.ASW FIXED WING"]  # TACGRP.C2GM.GNL.PNT.ACTL.ASBWF
    bbox["G-G-GPAA--"] = {"x1": 60, "x2": 140, "y1": 40, "y2": 160}
    sId["G-G-GPAH--"] = icn["TP.ASW ROTARY WING"]  # TACGRP.C2GM.GNL.PNT.ACTL.ASBWR
    bbox["G-G-GPAH--"] = {"x1": 60, "x2": 140, "y1": 40, "y2": 160}
    sId["G-G-GPAB--"] = icn["TP.SUCAP - FIXED WING"]  # TACGRP.C2GM.GNL.PNT.ACTL.SUWF
    bbox["G-G-GPAB--"] = {"x1": 60, "x2": 140, "y1": 40, "y2": 160}
    sId["G-G-GPAC--"] = icn["TP.SUCAP - ROTARY WING"]  # TACGRP.C2GM.GNL.PNT.ACTL.SUWR
    bbox["G-G-GPAC--"] = {"x1": 60, "x2": 140, "y1": 40, "y2": 160}
    sId["G-G-GPAD--"] = icn["TP.MIW - FIXED WING"]  # TACGRP.C2GM.GNL.PNT.ACTL.MIWF
    bbox["G-G-GPAD--"] = {"x1": 60, "x2": 140, "y1": 40, "y2": 160}
    sId["G-G-GPAE--"] = icn["TP.MIW - ROTARY WING"]  # TACGRP.C2GM.GNL.PNT.ACTL.MIWR
    bbox["G-G-GPAE--"] = {"x1": 60, "x2": 140, "y1": 40, "y2": 160}
    sId["G-G-GPAS--"] = icn["TP.STRIKE IP"]  # TACGRP.C2GM.GNL.PNT.ACTL.SKEIP
    bbox["G-G-GPAS--"] = {"x1": 60, "x2": 140, "y1": 30, "y2": 170}
    sId["G-G-GPAT--"] = icn["TP.TACAN"]  # TACGRP.C2GM.GNL.PNT.ACTL.TCN
    bbox["G-G-GPAT--"] = {"x1": 60, "x2": 140, "y1": 30, "y2": 170}
    sId["G-G-GPAO--"] = icn["TP.TOMCAT"]  # TACGRP.C2GM.GNL.PNT.ACTL.TMC
    bbox["G-G-GPAO--"] = {"x1": 60, "x2": 140, "y1": 30, "y2": 170}
    sId["G-G-GPAR--"] = icn["TP.RESCUE"]  # TACGRP.C2GM.GNL.PNT.ACTL.RSC
    bbox["G-G-GPAR--"] = {"x1": 60, "x2": 140, "y1": 30, "y2": 170}
    sId["G-G-GPAL--"] = icn["TP.REPLENISH"]  # TACGRP.C2GM.GNL.PNT.ACTL.RPH
    bbox["G-G-GPAL--"] = {"x1": 60, "x2": 140, "y1": 30, "y2": 170}
    sId["G-G-GPAF--"] = icn["TP.UNMANNED AERIAL SYSTEM"]  # TACGRP.C2GM.GNL.PNT.ACTL.UA
    bbox["G-G-GPAF--"] = {"x1": 60, "x2": 140, "y1": 30, "y2": 170}
    sId["G-G-GPAG--"] = icn["TP.VTUA"]  # TACGRP.C2GM.GNL.PNT.ACTL.VTUA
    bbox["G-G-GPAG--"] = {"x1": 60, "x2": 140, "y1": 30, "y2": 170}
    sId["G-G-GPAI--"] = icn["TP.ORBIT"]  # TACGRP.C2GM.GNL.PNT.ACTL.ORB
    bbox["G-G-GPAI--"] = {"x1": 60, "x2": 140, "y1": 30, "y2": 170}
    sId["G-G-GPAJ--"] = icn["TP.ORBIT - FIGURE EIGHT"]  # TACGRP.C2GM.GNL.PNT.ACTL.ORBF8
    bbox["G-G-GPAJ--"] = {"x1": 60, "x2": 140, "y1": 30, "y2": 170}
    sId["G-G-GPAM--"] = icn["TP.ORBIT - RACE TRACK"]  # TACGRP.C2GM.GNL.PNT.ACTL.ORBRT
    bbox["G-G-GPAM--"] = {"x1": 60, "x2": 140, "y1": 30, "y2": 170}
    sId["G-G-GPAN--"] = icn[
        "TP.ORBIT - RANDOM, CLOSED"
    ]  # TACGRP.C2GM.GNL.PNT.ACTL.ORBRD
    bbox["G-G-GPAN--"] = {"x1": 60, "x2": 140, "y1": 30, "y2": 170}
    sId["G-G-GPP---"] = icn["TP.ACTION POINT"]  # TACGRP.C2GM.GNL.PNT.ACTPNT
    bbox["G-G-GPP---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-G-GPPK--"] = icn[
        "TP.ACTION CHECK POINT"
    ]  # TACGRP.C2GM.GNL.PNT.ACTPNT.CHKPNT
    bbox["G-G-GPPK--"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-G-GPPC--"] = icn["TP.CONTACT POINT"]  # TACGRP.C2GM.GNL.PNT.ACTPNT.CONPNT
    bbox["G-G-GPPC--"] = {"x1": 55, "x2": 145, "y1": -10}
    sId["G-G-GPPO--"] = icn[
        "TP.COORDINATION POINT"
    ]  # TACGRP.C2GM.GNL.PNT.ACTPNT.CRDPNT
    bbox["G-G-GPPO--"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-G-GPPD--"] = icn["TP.DECISION POINT"]  # TACGRP.C2GM.GNL.PNT.ACTPNT.DCNPNT
    bbox["G-G-GPPD--"] = {"x1": 30, "x2": 170, "y1": 25, "y2": 160}
    sId["G-G-GPPL--"] = icn[
        "TP.ACTION LINKUP POINT"
    ]  # TACGRP.C2GM.GNL.PNT.ACTPNT.LNKUPT
    bbox["G-G-GPPL--"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-G-GPPP--"] = icn[
        "TP.ACTION PASSAGE POINT"
    ]  # TACGRP.C2GM.GNL.PNT.ACTPNT.PSSPNT
    bbox["G-G-GPPP--"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-G-GPPR--"] = icn[
        "TP.ACTION RALLY POINT"
    ]  # TACGRP.C2GM.GNL.PNT.ACTPNT.RAYPNT
    bbox["G-G-GPPR--"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-G-GPPE--"] = icn[
        "TP.ACTION RELEASE POINT"
    ]  # TACGRP.C2GM.GNL.PNT.ACTPNT.RELPNT
    bbox["G-G-GPPE--"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-G-GPPS--"] = icn[
        "TP.ACTION START POINT"
    ]  # TACGRP.C2GM.GNL.PNT.ACTPNT.STRPNT
    bbox["G-G-GPPS--"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-G-GPPA--"] = icn[
        "TP.ACTION AMNESTY POINT"
    ]  # TACGRP.C2GM.GNL.PNT.ACTPNT.AMNPNT
    bbox["G-G-GPPA--"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-G-GPPW--"] = icn["TP.WAYPOINT"]  # TACGRP.C2GM.GNL.PNT.ACTPNT.WAP
    bbox["G-G-GPPW--"] = {"x1": 60, "x2": 140, "y1": 60, "y2": 140}
    sId["G-G-GPC---"] = icn[
        "TP.SEA SURFACE CONTROL STATION"
    ]  # TACGRP.C2GM.GNL.PNT.SCTL
    bbox["G-G-GPC---"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 140}
    sId["G-G-GPCU--"] = icn["TP.(USV) CONTROL STATION"]  # TACGRP.C2GM.GNL.PNT.SCTL.USV
    bbox["G-G-GPCU--"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 140}
    sId["G-G-GPCUR-"] = icn[
        "TP.(RMV) USV CONTROL STATION"
    ]  # TACGRP.C2GM.GNL.PNT.SCTL.USV.RMV
    bbox["G-G-GPCUR-"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 140}
    sId["G-G-GPCUA-"] = icn[
        "TP.USV - ASW CONTROL STATION"
    ]  # TACGRP.C2GM.GNL.PNT.SCTL.USV.ASW
    bbox["G-G-GPCUA-"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 140}
    sId["G-G-GPCUS-"] = icn[
        "TP.USV - SUW CONTROL STATION"
    ]  # TACGRP.C2GM.GNL.PNT.SCTL.USV.SUW
    bbox["G-G-GPCUS-"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 140}
    sId["G-G-GPCUM-"] = icn[
        "TP.USV - MIW CONTROL STATION"
    ]  # TACGRP.C2GM.GNL.PNT.SCTL.USV.MIW
    bbox["G-G-GPCUM-"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 140}
    sId["G-G-GPCA--"] = icn["TP.ASW CONTROL STATION"]  # TACGRP.C2GM.GNL.PNT.SCTL.ASW
    bbox["G-G-GPCA--"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 140}
    sId["G-G-GPCS--"] = icn["TP.SUW CONTROL STATION"]  # TACGRP.C2GM.GNL.PNT.SCTL.SUW
    bbox["G-G-GPCS--"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 140}
    sId["G-G-GPCM--"] = icn["TP.MIW CONTROL STATION"]  # TACGRP.C2GM.GNL.PNT.SCTL.MIW
    bbox["G-G-GPCM--"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 140}
    sId["G-G-GPCP--"] = icn["TP.PICKET CONTROL STATION"]  # TACGRP.C2GM.GNL.PNT.SCTL.PKT
    bbox["G-G-GPCP--"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 140}
    sId["G-G-GPCR--"] = icn[
        "TP.RENDEZVOUS CONTROL POINT"
    ]  # TACGRP.C2GM.GNL.PNT.SCTL.RDV
    bbox["G-G-GPCR--"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 140}
    sId["G-G-GPCC--"] = icn["TP.RESCUE CONTROL POINT"]  # TACGRP.C2GM.GNL.PNT.SCTL.RSC
    bbox["G-G-GPCC--"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 140}
    sId["G-G-GPCE--"] = icn[
        "TP.REPLENISHMENT CONTROL POINT"
    ]  # TACGRP.C2GM.GNL.PNT.SCTL.REP
    bbox["G-G-GPCE--"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 140}
    sId["G-G-GPCN--"] = icn[
        "TP.NONCOMBATANT CONTROL STATION"
    ]  # TACGRP.C2GM.GNL.PNT.SCTL.NCBTT
    bbox["G-G-GPCN--"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 140}
    sId["G-G-GPB---"] = icn[
        "TP.SUB SURFACE CONTROL STATION"
    ]  # TACGRP.C2GM.GNL.PNT.UCTL
    bbox["G-G-GPB---"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 140}
    sId["G-G-GPBU--"] = icn["TP.(UUV) CONTROL STATION"]  # TACGRP.C2GM.GNL.PNT.UCTL.UUV
    bbox["G-G-GPBU--"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 140}
    sId["G-G-GPBUA-"] = icn[
        "TP.UUV - ASW CONTROL STATION"
    ]  # TACGRP.C2GM.GNL.PNT.UCTL.UUV.ASW
    bbox["G-G-GPBUA-"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 140}
    sId["G-G-GPBUS-"] = icn[
        "TP.UUV - SUW CONTROL STATION"
    ]  # TACGRP.C2GM.GNL.PNT.UCTL.UUV.SUW
    bbox["G-G-GPBUS-"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 140}
    sId["G-G-GPBUM-"] = icn[
        "TP.UUV - MIW CONTROL STATION"
    ]  # TACGRP.C2GM.GNL.PNT.UCTL.UUV.MIW
    bbox["G-G-GPBUM-"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 140}
    sId["G-G-GPBS--"] = icn[
        "TP.SUBMARINE CONTROL STATION"
    ]  # TACGRP.C2GM.GNL.PNT.UCTL.SBSTN
    bbox["G-G-GPBS--"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 140}
    sId["G-G-GPBSA-"] = icn[
        "TP.ASW SUBMARINE CONTROL STATION"
    ]  # TACGRP.C2GM.GNL.PNT.UCTL.SBSTN.ASW
    bbox["G-G-GPBSA-"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 140}
    sId["G-G-APP---"] = icn["TP.AIR CONTROL POINT (ACP)"]  # TACGRP.C2GM.AVN.PNT.ACP
    bbox["G-G-APP---"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-G-APC---"] = icn[
        "TP.COMMUNICATIONS CHECKPOINT"
    ]  # TACGRP.C2GM.AVN.PNT.COMMCP
    bbox["G-G-APC---"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-G-APU---"] = icn["TP.PULL-UP POINT"]  # TACGRP.C2GM.AVN.PNT.PUP
    bbox["G-G-APU---"] = {"x1": 50, "x2": 240, "y1": 50, "y2": 150}
    sId["G-G-APD---"] = icn[
        "TP.DOWNED AIRCREW PICKUP POINT"
    ]  # TACGRP.C2GM.AVN.PNT.DAPP
    bbox["G-G-APD---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-G-PN----"] = icn["TP.DUMMY MINEFIELD (STATIC)"]  # TACGRP.C2GM.DCPN.DMYMS
    bbox["G-G-PN----"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-G-DPT---"] = icn["TP.TARGET REFERENCE POINT"]  # TACGRP.C2GM.DEF.PNT.TGTREF
    bbox["G-G-DPT---"] = {"x1": 40, "x2": 160, "y1": 40, "y2": 160}
    sId["G-G-DPO---"] = icn["TP.OBSERVATION POST/OUTPOST"]  # TACGRP.C2GM.DEF.PNT.OBSPST
    bbox["G-G-DPO---"] = {"x1": 40, "x2": 160, "y1": 40, "y2": 160}
    sId["G-G-DPOC--"] = icn["TP.COMBAT OUTPOST"]  # TACGRP.C2GM.DEF.PNT.OBSPST.CBTPST
    bbox["G-G-DPOC--"] = {"x1": 40, "x2": 160, "y1": 40, "y2": 160}
    sId["G-G-DPOR--"] = icn[
        "TP.OBSERVATION POST - RECON"
    ]  # TACGRP.C2GM.DEF.PNT.OBSPST.RECON
    bbox["G-G-DPOR--"] = {"x1": 40, "x2": 160, "y1": 40, "y2": 160}
    sId["G-G-DPOF--"] = icn[
        "TP.FORWARD OBSERVATION POST"
    ]  # TACGRP.C2GM.DEF.PNT.OBSPST.FWDOP
    bbox["G-G-DPOF--"] = {"x1": 40, "x2": 160, "y1": 40, "y2": 160}
    sId["G-G-DPOS--"] = icn["TP.SENSOR OUTPOST"]  # TACGRP.C2GM.DEF.PNT.OBSPST.SOP
    bbox["G-G-DPOS--"] = {"x1": 40, "x2": 160, "y1": 40, "y2": 160}
    sId["G-G-DPON--"] = icn[
        "TP.CBRN OBSERVATION POST"
    ]  # TACGRP.C2GM.DEF.PNT.OBSPST.CBRNOP
    bbox["G-G-DPON--"] = {"x1": 40, "x2": 160, "y1": 40, "y2": 160}
    sId["G-G-OPP---"] = icn["TP.POINT OF DEPARTURE"]  # TACGRP.C2GM.DEF.PNT.OBSPST.POD
    bbox["G-G-OPP---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-M-OAOF--"] = icn[
        "TP.FOXHOLE, EMPLACEMENT OR WEAPON SITE"
    ]  # TACGRP.MOBSU.OBST.ATO.TDTSM.FIXPFD
    bbox["G-M-OAOF--"] = {"x1": 30, "x2": 170, "y1": 60, "y2": 110}
    sId["G-M-OAOM--"] = icn["TP.MINEFIELDS"]  # TACGRP.MOBSU.OBST.ATO.TDTSM.MVB
    bbox["G-M-OAOM--"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-M-OAOP--"] = icn["TP.MINEFIELDS"]  # TACGRP.MOBSU.OBST.ATO.TDTSM.MVBPFD
    bbox["G-M-OAOP--"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-M-OB----"] = icn["TP.BOOBY TRAP"]  # TACGRP.MOBSU.OBST.BBY
    bbox["G-M-OB----"] = {"x1": 60, "x2": 140, "y1": 0}
    sId["G-M-OMU---"] = icn["TP.UNSPECIFIED MINE"]  # TACGRP.MOBSU.OBST.MNE.USPMNE
    bbox["G-M-OMU---"] = {"x1": 60, "x2": 140, "y1": 0, "y2": 140}
    sId["G-M-OMT---"] = icn["TP.ANTITANK MINE"]  # TACGRP.MOBSU.OBST.MNE.ATMNE
    bbox["G-M-OMT---"] = {"x1": 60, "x2": 140, "y1": 0, "y2": 140}
    sId["G-M-OMD---"] = icn[
        "TP.ANTITANK MINE WITH ANTIHANDLING DEVICE"
    ]  # TACGRP.MOBSU.OBST.MNE.ATMAHD
    bbox["G-M-OMD---"] = {"x1": 60, "x2": 140, "y1": 0, "y2": 140}
    sId["G-M-OME---"] = icn["TP.DIRECTIONAL MINE"]  # TACGRP.MOBSU.OBST.MNE.ATMDIR
    bbox["G-M-OME---"] = {"x1": 60, "x2": 140, "y1": 0, "y2": 140}
    sId["G-M-OMP---"] = icn["TP.ANTIPERSONNEL MINE"]  # TACGRP.MOBSU.OBST.MNE.APMNE
    bbox["G-M-OMP---"] = {"x1": 60, "x2": 140, "y1": 0, "y2": 140}
    sId["G-M-OMW---"] = icn["TP.WIDE AREA MINE"]  # TACGRP.MOBSU.OBST.MNE.WAMNE
    bbox["G-M-OMW---"] = {"x1": 60, "x2": 140, "y1": 0, "y2": 140}
    sId["G-M-OFS---"] = icn["TP.STATIC MINEFIELD"]  # TACGRP.MOBSU.OBST.MNEFLD.STC
    bbox["G-M-OFS---"] = {"x1": -10, "x2": 210, "y1": 60, "y2": 140}
    sId["G-M-OHTL--"] = icn["TP.AVIATION TOWER (LOW)"]  # TACGRP.MOBSU.OBST.AVN.TWR.LOW
    bbox["G-M-OHTL--"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-M-OHTH--"] = icn[
        "TP.AVIATION TOWER (HIGH)"
    ]  # TACGRP.MOBSU.OBST.AVN.TWR.HIGH
    bbox["G-M-OHTH--"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-M-BCP---"] = icn[
        "TP.ENGINEER REGULATING POINT"
    ]  # TACGRP.MOBSU.OBSTBP.CSGSTE.ERP
    bbox["G-M-BCP---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-M-SE----"] = icn[
        "TP.EARTHWORK, SMALL TRENCH OR FORTIFICATION"
    ]  # TACGRP.MOBSU.SU.ESTOF
    bbox["G-M-SE----"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-M-SF----"] = icn["TP.FORT"]  # TACGRP.MOBSU.SU.FRT
    bbox["G-M-SF----"] = {"x1": 40, "x2": 160, "y1": 40, "y2": 160}
    sId["G-M-SS----"] = icn["TP.SURFACE SHELTER"]  # TACGRP.MOBSU.SU.SUFSHL
    bbox["G-M-SS----"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-M-SU----"] = icn["TP.UNDERGROUND SHELTER"]  # TACGRP.MOBSU.SU.UGDSHL
    bbox["G-M-SU----"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-M-NZ----"] = icn[
        "TP.NUCLEAR DETONATIONS GROUND ZERO"
    ]  # TACGRP.MOBSU.CBRN.NDGZ
    bbox["G-M-NZ----"] = {"x1": 50, "x2": 150, "y1": 0}
    sId["G-M-NF----"] = icn["TP.FALLOUT PRODUCING"]  # TACGRP.MOBSU.CBRN.FAOTP
    bbox["G-M-NF----"] = {"x1": 0, "x2": 200, "y1": 0, "y2": 200}
    sId["G-M-NEB---"] = icn["TP.BIOLOGICAL"]  # TACGRP.MOBSU.CBRN.REEVNT.BIO
    bbox["G-M-NEB---"] = {"x1": 50, "x2": 150, "y1": -10, "y2": 160}
    sId["G-M-NEC---"] = icn["TP.CHEMICAL"]  # TACGRP.MOBSU.CBRN.REEVNT.CML
    bbox["G-M-NEC---"] = {"x1": 50, "x2": 150, "y1": -10, "y2": 160}
    sId["G-M-NDP---"] = icn[
        "TP.DECONTAMINATION POINT (UNSPECIFIED)"
    ]  # TACGRP.MOBSU.CBRN.DECONP.USP
    bbox["G-M-NDP---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-M-NDA---"] = icn[
        "TP.ALTERNATE DECONTAMINATION POINT (UNSPECIFIED)"
    ]  # TACGRP.MOBSU.CBRN.DECONP.ALTUSP
    bbox["G-M-NDA---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-M-NDT---"] = icn[
        "TP.DECONTAMINATION POINT (TROOPS)"
    ]  # TACGRP.MOBSU.CBRN.DECONP.TRP
    bbox["G-M-NDT---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-M-NDE---"] = icn[
        "TP.DECONTAMINATION POINT (EQUIPMENT)"
    ]  # TACGRP.MOBSU.CBRN.DECONP.EQT
    bbox["G-M-NDE---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-M-NDB---"] = icn[
        "TP.DECONTAMINATION POINT (EQUIPMENT AND TROOPS)"
    ]  # TACGRP.MOBSU.CBRN.DECONP.EQTTRP
    bbox["G-M-NDB---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-M-NDO---"] = icn[
        "TP.OPERATIONAL DECONTAMINATION"
    ]  # TACGRP.MOBSU.CBRN.DECONP.OPDECN
    bbox["G-M-NDO---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-M-NDD---"] = icn[
        "TP.THOROUGH DECONTAMINATION"
    ]  # TACGRP.MOBSU.CBRN.DECONP.TRGH
    bbox["G-M-NDD---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-F-PTS---"] = icn["TP.POINT TARGET"]  # TACGRP.FSUPP.PNT.TGT.PTGT
    bbox["G-F-PTS---"] = {"x1": 0, "x2": 200, "y1": 0, "y2": 200}
    sId["G-F-PTN---"] = icn["TP.NUCLEAR TARGET"]  # TACGRP.FSUPP.PNT.TGT.NUCTGT
    bbox["G-F-PTN---"] = {"x1": 0, "x2": 200, "y1": 0, "y2": 200}
    sId["G-F-PCF---"] = icn["TP.FIRE SUPPORT STATION"]  # TACGRP.FSUPP.PNT.C2PNT.FSS
    bbox["G-F-PCF---"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-F-PCS---"] = icn["TP.SURVEY CONTROL POINT"]  # TACGRP.FSUPP.PNT.C2PNT.SCP
    bbox["G-F-PCS---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-F-PCB---"] = icn["TP.FIRING POINT"]  # TACGRP.FSUPP.PNT.C2PNT.FP
    bbox["G-F-PCB---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-F-PCR---"] = icn["TP.RELOAD POINT"]  # TACGRP.FSUPP.PNT.C2PNT.RP
    bbox["G-F-PCR---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-F-PCH---"] = icn["TP.HIDE POINT"]  # TACGRP.FSUPP.PNT.C2PNT.HP
    bbox["G-F-PCH---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-F-PCL---"] = icn["TP.LAUNCH POIN"]  # TACGRP.FSUPP.PNT.C2PNT.LP
    bbox["G-F-PCL---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PX----"] = icn["TP.AMBULANCE EXCHANGE POINT"]  # TACGRP.CSS.PNT.AEP
    bbox["G-S-PX----"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PC----"] = icn["TP.CANNIBALIZATION POINT"]  # TACGRP.CSS.PNT.CBNP
    bbox["G-S-PC----"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PY----"] = icn["TP.CASUALTY COLLECTION POINT"]  # TACGRP.CSS.PNT.CCP
    bbox["G-S-PY----"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PT----"] = icn["TP.CIVILIAN COLLECTION POINT"]  # TACGRP.CSS.PNT.CVP
    bbox["G-S-PT----"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PD----"] = icn["TP.DETAINEE COLLECTION POINT"]  # TACGRP.CSS.PNT.DCP
    bbox["G-S-PD----"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PE----"] = icn["TP.EPW COLLECTION POINT"]  # TACGRP.CSS.PNT.EPWCP
    bbox["G-S-PE----"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PL----"] = icn["TP.LOGISTICS RELEASE POINT"]  # TACGRP.CSS.PNT.LRP
    bbox["G-S-PL----"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PM----"] = icn["TP.MAINTENANCE COLLECTION POINT"]  # TACGRP.CSS.PNT.MCP
    bbox["G-S-PM----"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PR----"] = icn[
        "TP.REARM, REFUEL AND RESUPPLY POINT"
    ]  # TACGRP.CSS.PNT.RRRP
    bbox["G-S-PR----"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PU----"] = icn["TP.REFUEL ON THE MOVE POINT"]  # TACGRP.CSS.PNT.ROM
    bbox["G-S-PU----"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PO----"] = icn["TP.TRAFFIC CONTROL POST (TCP)"]  # TACGRP.CSS.PNT.TCP
    bbox["G-S-PO----"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PI----"] = icn["TP.TRAILER TRANSFER POINT"]  # TACGRP.CSS.PNT.TTP
    bbox["G-S-PI----"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PN----"] = icn[
        "TP.UNIT MAINTENANCE COLLECTION POINT"
    ]  # TACGRP.CSS.PNT.UMC
    bbox["G-S-PN----"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PS----"] = icn["TP.SUPPLY POINT"]  # TACGRP.CSS.PNT.SPT
    bbox["G-S-PS----"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-S-PSZ---"] = icn["TP.SP (GENERAL)"]  # TACGRP.CSS.PNT.SPT.GNL
    bbox["G-S-PSZ---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PSA---"] = icn["TP.SP CLASS I"]  # TACGRP.CSS.PNT.SPT.CLS1
    bbox["G-S-PSA---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PSB---"] = icn["TP.SP CLASS II"]  # TACGRP.CSS.PNT.SPT.CLS2
    bbox["G-S-PSB---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PSC---"] = icn["TP.SP CLASS III"]  # TACGRP.CSS.PNT.SPT.CLS3
    bbox["G-S-PSC---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PSD---"] = icn["TP.SP CLASS IV"]  # TACGRP.CSS.PNT.SPT.CLS4
    bbox["G-S-PSD---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PSE---"] = icn["TP.SP CLASS V"]  # TACGRP.CSS.PNT.SPT.CLS5
    bbox["G-S-PSE---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PSF---"] = icn["TP.SP CLASS VI"]  # TACGRP.CSS.PNT.SPT.CLS6
    bbox["G-S-PSF---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PSG---"] = icn["TP.SP CLASS VII"]  # TACGRP.CSS.PNT.SPT.CLS7
    bbox["G-S-PSG---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PSH---"] = icn["TP.SP CLASS VIII"]  # TACGRP.CSS.PNT.SPT.CLS8
    bbox["G-S-PSH---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PSI---"] = icn["TP.SP CLASS IX"]  # TACGRP.CSS.PNT.SPT.CLS9
    bbox["G-S-PSI---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PSJ---"] = icn["TP.SP CLASS X"]  # TACGRP.CSS.PNT.SPT.CLS10
    bbox["G-S-PSJ---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PA----"] = icn["TP.AMMUNITION SUPPLY POINT"]  # TACGRP.CSS.PNT.AP
    bbox["G-S-PA----"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-S-PAS---"] = icn["TP.AMMUNITION TRANSFER POINT"]  # TACGRP.CSS.PNT.AP.ASP
    bbox["G-S-PAS---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-S-PAT---"] = icn["TP.AMMUNITION TRANSFER POINT"]  # TACGRP.CSS.PNT.AP.ATP
    bbox["G-S-PAT---"] = {"x1": 60, "x2": 140, "y1": -60}
    sId["G-O-ED----"] = icn["TP.DITAK"]  # TACGRP.OTH.ER.DTHAC
    bbox["G-O-ED----"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-O-EP----"] = icn["TP.PIP"]  # TACGRP.OTH.ER.PIW
    bbox["G-O-EP----"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-O-EV----"] = icn["TP.DRP"]  # TACGRP.OTH.ER.DSTVES
    bbox["G-O-EV----"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-O-HM----"] = icn["TP.SEA MINE-LIKE"]  # TACGRP.OTH.HAZ.SML
    bbox["G-O-HM----"] = {"x1": 40, "x2": 160, "y1": 40, "y2": 160}
    sId["G-O-HI----"] = icn["TP.ICEBERG"]  # TACGRP.OTH.HAZ.IB
    bbox["G-O-HI----"] = {"x1": 40, "x2": 160, "y1": 30, "y2": 170}
    sId["G-O-HO----"] = icn["TP.OIL RIG"]  # TACGRP.OTH.HAZ.OLRG
    bbox["G-O-HO----"] = {"x1": 50, "x2": 150, "y1": 30, "y2": 130}
    sId["G-O-SB----"] = icn["TP.BOTTOM RETURN/NON-MILCO"]  # TACGRP.OTH.SSUBSR.BTMRTN
    bbox["G-O-SB----"] = {"x1": 30, "x2": 170, "y1": 40, "y2": 160}
    sId["G-O-SBM---"] = icn["TP.INSTALLATION/MANMADE"]  # TACGRP.OTH.SSUBSR.BTMRTN.INS
    bbox["G-O-SBM---"] = {"x1": 30, "x2": 170, "y1": 40, "y2": 160}
    sId["G-O-SBN---"] = icn["TP.SEABED ROCK/STONE"]  # TACGRP.OTH.SSUBSR.BTMRTN.SBRSOO
    bbox["G-O-SBN---"] = {"x1": 30, "x2": 170, "y1": 40, "y2": 160}
    sId["G-O-SBW---"] = icn["TP.WRECK, NON-DANGEROUS"]  # TACGRP.OTH.SSUBSR.BTMRTN.WRKND
    bbox["G-O-SBW---"] = {"x1": 30, "x2": 170, "y1": 40, "y2": 160}
    sId["G-O-SBX---"] = icn["TP.WRECK, DANGEROUS"]  # TACGRP.OTH.SSUBSR.BTMRTN.WRKD
    bbox["G-O-SBX---"] = {"x1": 30, "x2": 170, "y1": 40, "y2": 160}
    sId["G-O-SM----"] = icn["TP.MARINE LIFE"]  # TACGRP.OTH.SSUBSR.MARLFE
    bbox["G-O-SM----"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-O-SS----"] = icn["TP.SEA ANOMALY"]  # TACGRP.OTH.SSUBSR.SA
    bbox["G-O-SS----"] = {"x1": 50, "x2": 150, "y1": 50, "y2": 150}
    sId["G-O-FA----"] = icn["TP.ACOUSTIC FIX"]  # TACGRP.OTH.FIX.ACU
    bbox["G-O-FA----"] = {"x1": 0, "x2": 200, "y1": 0, "y2": 200}
    sId["G-O-FE----"] = icn["TP.ELECTROMAGNETIC FIX"]  # TACGRP.OTH.FIX.EM
    bbox["G-O-FE----"] = {"x1": 0, "x2": 200, "y1": 0, "y2": 200}
    sId["G-O-FO----"] = icn["TP.ELECTRO-OPTICAL FIX"]  # TACGRP.OTH.FIX.EOP
    bbox["G-O-FO----"] = {"x1": 0, "x2": 200, "y1": 0, "y2": 200}

    # ... rest of the file ...


exports = {
    "type": "letter",
    "getMetadata": metadata_letter,
    "getIcons": getIcons_letter,
    "iconParts": [iconParts],
    "labels": labels,
    "icons": tactical_points_2525,
}
