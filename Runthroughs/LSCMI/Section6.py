from Models.ExtractedModels.LSCMI.Section6.ScoreBasedRiskLevel import ScoreBasedRiskLevel
from Models.ExtractedModels.LSCMI.Section6.ClientBasedClinicalOverride import ClientBasedClinicalOverride
from Models.ExtractedModels.LSCMI.Section6.AdministrativePolicyOverride import AdministrativePolicyOverride
from Models.ExtractedModels.LSCMI.Section6.FinalRiskNeedLevel import FinalRiskNeedLevel

def section6(common_data):

    data = ScoreBasedRiskLevel.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section6/ScoreBasedRiskLevel', data=data, allow_redirects=True, verify=False)

    data = ClientBasedClinicalOverride.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section6/ClientBasedClinicalOverride', data=data, allow_redirects=True, verify=False)

    data = AdministrativePolicyOverride.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section6/AdministrativePolicyOverride', data=data, allow_redirects=True, verify=False)

    data = FinalRiskNeedLevel.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section6/FinalRiskNeedLevel', data=data, allow_redirects=True, verify=False)