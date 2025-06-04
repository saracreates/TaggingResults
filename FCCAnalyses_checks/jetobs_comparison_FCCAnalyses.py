import uproot 
import numpy as np
import matplotlib.pyplot as plt

from helper_jetobs import *

save_status = True  # Set to False if you do not want to save the plots

# change the paths here to use your own files 

path_1 = "/afs/cern.ch/work/s/saaumill/public/MyFCCAnalyses/outputs/treemaker/fullsimtagger_jetbased/Hbb.root"
# path_2 = "/eos/experiment/fcc/ee/datasets/CLD_fullsim_tagging_from_key4hep/CLD_v5/Hbb_0.root" #Hxx_0.root # full sim from key4hep
path_2 = "/afs/cern.ch/work/s/saaumill/public/MyFCCAnalyses/outputs/treemaker/fullsimtagger_jetbased/Hbb_from_key4hep.root"

print("Loading data for jet observables comparison...")

file_1 = uproot.open(path_1)
tree_1 = file_1["tree;1"]

file_2 = uproot.open(path_2)
tree_2 = file_2["JetConstituentObservables;1"]

# adapt the size of the data you want to load here
df_1 = tree_1.arrays(library="np", entry_start=0, entry_stop=2000) 
df_2 = tree_2.arrays(library="np", entry_start=0, entry_stop=2000)

key_map = { 
    "pfcand_erel_log": "pfcand_erel_log",
    "pfcand_thetarel": "pfcand_thetarel",
    "pfcand_phirel": "pfcand_phirel",
    "pfcand_dptdpt": "pfcand_cov_omegaomega",
    "pfcand_detadeta": "pfcand_cov_tanLambdatanLambda",
    "pfcand_dphidphi": "pfcand_cov_phiphi",
    "pfcand_dxydxy": "pfcand_cov_d0d0",
    "pfcand_dzdz": "pfcand_cov_z0z0",
    "pfcand_dxydz": "pfcand_cov_d0z0",
    "pfcand_dphidxy": "pfcand_cov_phid0",
    "pfcand_dlambdadz": "pfcand_cov_tanLambdaz0",
    "pfcand_dxyc": "pfcand_cov_d0omega",
    "pfcand_dxyctgtheta": "pfcand_cov_d0tanLambda",
    "pfcand_phic": "pfcand_cov_phiomega",
    "pfcand_phidz": "pfcand_cov_phiz0",
    "pfcand_phictgtheta": "pfcand_cov_phitanLambda",
    "pfcand_cdz": "pfcand_cov_omegaz0",
    "pfcand_cctgtheta": "pfcand_cov_omegatanLambda",
    "pfcand_dxy": "pfcand_d0",
    "pfcand_dz": "pfcand_z0",
    "pfcand_btagSip2dVal": "pfcand_Sip2dVal",
    "pfcand_btagSip2dSig": "pfcand_Sip2dSig",
    "pfcand_btagSip3dVal": "pfcand_Sip3dVal",
    "pfcand_btagSip3dSig": "pfcand_Sip3dSig",
    "pfcand_btagJetDistVal": "pfcand_JetDistVal",
    "pfcand_btagJetDistSig": "pfcand_JetDistSig",
    "pfcand_type": "pfcand_type",
    "pfcand_charge": "pfcand_charge",
    "pfcand_isEl": "pfcand_isEl",
    "pfcand_isMu": "pfcand_isMu",
    "pfcand_isGamma": "pfcand_isGamma",
    "pfcand_isChargedHad": "pfcand_isChargedHad",
    "pfcand_isNeutralHad": "pfcand_isNeutralHad",
    "pfcand_dndx": "pfcand_dndx",
    "pfcand_mtof": "pfcand_tof",
    "pfcand_e": "pfcand_e",
    "pfcand_p": "pfcand_p",
}
df_1 = {key_map.get(k): v for k, v in df_1.items() if key_map.get(k) is not None}
# df_2 = {key_map.get(k): v for k, v in df_2.items() if key_map.get(k) is not None}

print("Data loaded successfully.")

print("Plotting jet observables...")

plot_kinematics(df_1, df_2, l1="FCCAnalyses", l2="key4hep", save=save_status)
plot_pidflags(df_1, df_2, l1="FCCAnalyses", l2="key4hep", save=save_status)

print("Plotting impact parameter observables...")

# these are lists because there might not always be 3 charged particles
index_charged_3E_1 = get_value_highest_energy_particle(df_1)
index_charged_3E_2 = get_value_highest_energy_particle(df_2)

plot_IP(df_1, df_2, index_charged_3E_1, index_charged_3E_2, l1="FCCAnalyses", l2="key4hep", save=save_status)
plot_cov_matrix(df_1, df_2, index_charged_3E_1, index_charged_3E_2, l1="FCCAnalyses", l2="key4hep", save=save_status)

print("Plots generated successfully.")

