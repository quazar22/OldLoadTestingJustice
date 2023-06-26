from Models.ExtractedModels.LSCMI.Section2.PersonalProblem import PersonalProblem
from Models.ExtractedModels.LSCMI.Section2.HistoryOfPerpetrationSexualAssault import HistoryOfPerpetrationSexualAssault
from Models.ExtractedModels.LSCMI.Section2.HistoryOfPerpetrationNonSexualAssault import HistoryOfPerpetrationNonSexualAssault
from Models.ExtractedModels.LSCMI.Section2.HistoryOfPerpetrationOtherAntisocialBehaviour import HistoryOfPerpetrationOtherAntisocialBehaviour

def section2(common_data):

    data = PersonalProblem.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section2/PersonalProblem', data=data, allow_redirects=True, verify=False)

    data = HistoryOfPerpetrationSexualAssault.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section2/HistoryOfPerpetrationSexualAssault', data=data, allow_redirects=True, verify=False)

    data = HistoryOfPerpetrationNonSexualAssault.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section2/HistoryOfPerpetrationNonSexualAssault', data=data, allow_redirects=True, verify=False)

    data = HistoryOfPerpetrationOtherAntisocialBehaviour.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/Section2/HistoryOfPerpetrationOtherAntisocialBehaviour', data=data, allow_redirects=True, verify=False)

