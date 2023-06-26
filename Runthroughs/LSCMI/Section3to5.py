from Models.ExtractedModels.LSCMI.Section4.OtherClientIssues import OtherClientIssues
from Models.ExtractedModels.LSCMI.Section5.SpecialResponsivityConsideration import SpecialResponsivityConsideration

def section3to5(common_data):

    data = OtherClientIssues.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section3to5/OtherClientIssues', data=data, allow_redirects=True, verify=False)

    data = SpecialResponsivityConsideration.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section3to5/SpecialResponsivityConsideration', data=data, allow_redirects=True, verify=False)