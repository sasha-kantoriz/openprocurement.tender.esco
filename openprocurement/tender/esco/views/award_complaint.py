# -*- coding: utf-8 -*-
from openprocurement.api.utils import opresource
from openprocurement.tender.openua.views.award_complaint import TenderUaAwardComplaintResource
from openprocurement.tender.openeu.views.award_complaint import TenderEUAwardComplaintResource


@opresource(name='Tender ESCO UA Award Complaints',
            collection_path='/tenders/{tender_id}/awards/{award_id}/complaints',
            path='/tenders/{tender_id}/awards/{award_id}/complaints/{complaint_id}',
            procurementMethodType='esco.UA',
            description="Tender ESCO UA Award complaints")
class TenderESCOUAAwardComplaintResource(TenderUaAwardComplaintResource):
    """ Tender ESCO UA Award Complaint Resource """


@opresource(name='Tender ESCO EU Award Complaints',
            collection_path='/tenders/{tender_id}/awards/{award_id}/complaints',
            path='/tenders/{tender_id}/awards/{award_id}/complaints/{complaint_id}',
            procurementMethodType='esco.EU',
            description="Tender ESCO EU Award complaints")
class TenderESCOEUAwardComplaintResource(TenderEUAwardComplaintResource):
    """ Tender ESCO EU Award Complaint Resource """