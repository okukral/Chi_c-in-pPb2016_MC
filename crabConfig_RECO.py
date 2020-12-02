from CRABClient.UserUtilities import config

config = config()

config.section_("General")
config.General.requestName = 'Chi_c_pPb8TeV_MC_RECO_v5'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.section_("JobType")
config.JobType.allowUndistributedCMSSW = True #Allow SLC7
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'ChiCJpsiMuMu_Pythia8_8p16TeV_TuneCUETP8M1_RECO.py'
config.JobType.maxMemoryMB = 2000
config.JobType.maxJobRuntimeMin = 800
config.JobType.outputFiles = ['ChiCJpsiMuMu_Pythia8_8p16TeV_TuneCUETP8M1_RECO.root']

config.section_("Data")
config.Data.inputDataset = '/Chi_c_pPb8TeV_privateMC_GEN/okukral-Chi_c_pPb8TeV_MC_DIGI_v5-ad67f9fa96b42625e03746b1b4851542/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2
config.Data.outLFNDirBase = '/store/group/phys_heavyions/okukral/pPb/%s' % (config.General.requestName)
config.Data.publication = True
config.Data.outputDatasetTag = config.General.requestName

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
