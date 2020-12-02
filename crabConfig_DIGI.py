from CRABClient.UserUtilities import config#, getUsernameFromSiteDB

config = config()

config.section_("General")
config.General.requestName = 'Chi_c_pPb8TeV_MC_DIGI_v5'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.section_("JobType")
config.JobType.allowUndistributedCMSSW = True #Allow SLC7
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'ChiCJpsiMuMu_Pythia8_8p16TeV_TuneCUETP8M1_DIGI.py'
config.JobType.maxMemoryMB = 2500
config.JobType.outputFiles = ['ChiCJpsiMuMu_Pythia8_8p16TeV_TuneCUETP8M1_DIGI.root']

config.section_("Data")
config.Data.inputDataset = '/Chi_c_pPb8TeV_privateMC_GEN/okukral-Chi_c_pPb8TeV_MC_GEN_v5-580a003edec2ed9e80f877948512d143/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 20
config.Data.outLFNDirBase = '/store/group/phys_heavyions/okukral/pPb/%s' % (config.General.requestName)
config.Data.publication = True
config.Data.outputDatasetTag = config.General.requestName
#config.Data.ignoreLocality = True

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
config.Site.blacklist = ['T2_US_Vanderbilt']
