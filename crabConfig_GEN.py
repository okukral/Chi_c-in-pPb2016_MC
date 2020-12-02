from CRABClient.UserUtilities import config#, getUsernameFromSiteDB

config = config()

config.section_("General")
config.General.requestName = 'Chi_c_pPb8TeV_MC_GEN_v5'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.section_("JobType")
config.JobType.allowUndistributedCMSSW = True #Allow SLC7
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'ChiCJpsiMuMu_Pythia8_8p16TeV_TuneCUETP8M1_GEN.py'
config.JobType.maxMemoryMB = 2000
config.JobType.outputFiles = ['ChiCJpsiMuMu_Pythia8_8p16TeV_TuneCUETP8M1_GEN.root']

config.section_("Data")
#config.Data.inputDataset = '/PADoubleMuon/PARun2016C-PromptReco-v1/AOD'
#config.Data.inputDBS = 'global'
config.Data.outputPrimaryDataset = 'Chi_c_pPb8TeV_privateMC_GEN'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 5000
NJOBS = 200
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/phys_heavyions/okukral/pPb/%s' % (config.General.requestName)
config.Data.publication = True
config.Data.outputDatasetTag = config.General.requestName

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
config.Site.blacklist = ['T2_US_Vanderbilt']
