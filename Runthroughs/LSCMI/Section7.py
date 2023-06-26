import utils
import json
from Models.ExtractedModels.LSCMI.Section7.RiskNeedProfile import RiskNeedProfile
from Models.ExtractedModels.LSCMI.Section7.Analysis import Analysis
from Models.ExtractedModels.LSCMI.Section7.Pattern import Pattern
from Models.ExtractedModels.LSCMI.Section7.Nature import Nature
from Models.ExtractedModels.LSCMI.Section7.Seriousness import Seriousness
from Models.ExtractedModels.LSCMI.Section7.Likelihood import Likelihood
from Models.ExtractedModels.LSCMI.Section7.S7Summary import S7Summary
from Models.ExtractedModels.LSCMI.Section7.S7Conclusion import S7Conclusion

def section7(common_data):

    data = RiskNeedProfile.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section7/RiskNeedProfile', data=data, allow_redirects=True, verify=False)

    data = Analysis.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section7/Analysis', data=data, allow_redirects=True, verify=False)

    data = Pattern.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section7/Pattern', data=data, allow_redirects=True, verify=False)

    data = Nature.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section7/Nature', data=data, allow_redirects=True, verify=False)

    data = Seriousness.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section7/Seriousness', data=data, allow_redirects=True, verify=False)

    data = Likelihood.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section7/Likelihood', data=data, allow_redirects=True, verify=False)

    data = S7Summary.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section7/S7Summary', data=data, allow_redirects=True, verify=False)

    data = S7Conclusion.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section7/S7Conclusion', data=data, allow_redirects=True, verify=False)