import utils
import json
from Models.ExtractedModels.LSCMI.OffenderHistory.OffenderModel import OffenderModel
from Models.ExtractedModels.LSCMI.OffenderHistory.OffenderHistoryAModel import OffenderHistoryAModel
from Models.ExtractedModels.LSCMI.OffenderHistory.OffenderHistoryB1Model import OffenderHistoryB as OffenderHistoryB1Model
from Models.ExtractedModels.LSCMI.OffenderHistory.OffenderHistoryB2Model import OffenderHistoryB as OffenderHistoryB2Model
from Models.ExtractedModels.LSCMI.OffenderHistory.OffenderHistoryB3Model import OffenderHistoryB as OffenderHistoryB3Model

def offender_history(common_data):
    common_data.response = common_data.session.get(common_data.site + '/LSCMI/OffenderHistory/NewCase')

    chn = get_chn(common_data)

    data = OffenderModel.get_data(common_data.response, chn)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/OffenderHistory/UpdateOffender', data=data, allow_redirects=True, verify=False)

    data = OffenderHistoryAModel.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/OffenderHistory/UpdateOffenderHistoryA', data=data, allow_redirects=True, verify=False)

    data = OffenderHistoryB1Model.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/OffenderHistory/UpdateOffenderHistoryB1', data=data, allow_redirects=True, verify=False)

    data = OffenderHistoryB2Model.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/OffenderHistory/UpdateOffenderHistoryB2', data=data, allow_redirects=True, verify=False)

    data = OffenderHistoryB2Model.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/OffenderHistory/UpdateOffenderHistoryB24', data=data, allow_redirects=True, verify=False)

    data = OffenderHistoryB3Model.get_data(common_data.response)
    common_data.response = common_data.session.post(common_data.site + '/LSCMI/OffenderHistory/UpdateOffenderHistoryB3', data=data, allow_redirects=True, verify=False)

def get_chn(common_data):
    data = {
        'localAuthorityId': utils.get_local_authority(common_data.response),
        '__RequestVerificationToken': utils.get_verification_token(common_data.response)
    }

    response = common_data.session.post(common_data.site+'/LSCMI/OffenderHistory/GenerateCriminalHistoryNumber', data=data)
    return json.loads(response.text)['generatedCriminalHistoryNumber'][1:].split("/")