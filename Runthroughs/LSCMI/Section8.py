from Models.ExtractedModels.LSCMI.Section8.CommunityOffenders import CommunityOffenders
from Models.ExtractedModels.LSCMI.Section8.SummaryFindings import SummaryFindings

def section8(common_data):

    data = CommunityOffenders.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section8/CommunityOffenders', data=data, allow_redirects=True, verify=False)

    data = SummaryFindings.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section8/SummaryFindings', data=data, allow_redirects=True, verify=False)