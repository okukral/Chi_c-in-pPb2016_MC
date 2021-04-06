from CRABClient.UserUtilities import config, getUsernameFromCRIC

config = config()

config.section_("General")
config.General.requestName = 'Chi_c_pPb8TeV_MC_DIGI_v7'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.section_("JobType")
config.JobType.allowUndistributedCMSSW = True #Allow SLC7
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'ChiCJpsiMuMu_Pythia8_8p16TeV_TuneCUETP8M1_DIGI.py'
config.JobType.maxMemoryMB = 2500 #needs ram
config.JobType.outputFiles = ['ChiCJpsiMuMu_Pythia8_8p16TeV_TuneCUETP8M1_DIGI.root']

config.section_("Data")
config.Data.inputDataset = '/Chi_c_pPb8TeV_privateMC_GEN/okukral-Chi_c_pPb8TeV_MC_GEN_v7-432ec51c3a3f7d296fef2030d9b28849/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 8
config.Data.outLFNDirBase = '/store/group/phys_heavyions/%s/pPb/%s' % (getUsernameFromCRIC(), config.General.requestName)
config.Data.publication = True
config.Data.outputDatasetTag = config.General.requestName
#config.Data.ignoreLocality = True

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
config.Site.blacklist = ['T2_US_Vanderbilt']
