from Models.ExtractedModels.LSCMI.Section11.DischargeSummaryCommunity import DischargeSummaryCommunity
from Models.ExtractedModels.LSCMI.Section11.DischargeSummaryNarrative import DischargeSummaryNarrative

def section11(common_data):

    data = DischargeSummaryCommunity.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section11/DischargeSummaryCommunity', data=data, allow_redirects=True, verify=False)

    data = DischargeSummaryNarrative.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section11/DischargeSummaryNarrative', data=data, allow_redirects=True, verify=False)