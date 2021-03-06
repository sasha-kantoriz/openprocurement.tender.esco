# -*- coding: utf-8 -*-
import unittest

from openprocurement.api.tests.base import snitch

from openprocurement.tender.belowthreshold.tests.cancellation import (
    TenderCancellationResourceTestMixin,
    TenderCancellationDocumentResourceTestMixin
)
from openprocurement.tender.belowthreshold.tests.cancellation_blanks import (
    # TenderLotsCancellationResourceTest
    create_tender_lots_cancellation,
    patch_tender_lots_cancellation,
    # TenderLotCancellationResourceTest
    create_tender_lot_cancellation,
    patch_tender_lot_cancellation,
)

from openprocurement.tender.openua.tests.cancellation_blanks import (
    # TenderCancellationResourceTest
    create_tender_cancellation,
    patch_tender_cancellation,
)

from openprocurement.tender.esco.tests.base import (
    BaseESCOEUContentWebTest,
    test_bids,
    test_lots
)


class TenderCancellationResourceTest(BaseESCOEUContentWebTest, TenderCancellationResourceTestMixin):

    initial_auth = ('Basic', ('broker', ''))

    test_create_tender_cancellation = snitch(create_tender_cancellation)
    test_patch_tender_cancellation = snitch(patch_tender_cancellation)


class TenderLotCancellationResourceTest(BaseESCOEUContentWebTest):
    initial_lots = test_lots

    initial_auth = ('Basic', ('broker', ''))

    test_create_tender_cancellation = snitch(create_tender_lot_cancellation)
    test_patch_tender_cancellation = snitch(patch_tender_lot_cancellation)


class TenderLotsCancellationResourceTest(BaseESCOEUContentWebTest):
    initial_lots = 2 * test_lots

    initial_auth = ('Basic', ('broker', ''))
    test_create_tender_cancellation = snitch(create_tender_lots_cancellation)
    test_patch_tender_cancellation = snitch(patch_tender_lots_cancellation)


class TenderCancellationDocumentResourceTest(BaseESCOEUContentWebTest, TenderCancellationDocumentResourceTestMixin):

    initial_auth = ('Basic', ('broker', ''))

    def setUp(self):
        super(TenderCancellationDocumentResourceTest, self).setUp()
        # Create cancellation
        response = self.app.post_json('/tenders/{}/cancellations?acc_token={}'.format(
            self.tender_id, self.tender_token), {'data': {'reason': 'cancellation reason'}})
        cancellation = response.json['data']
        self.cancellation_id = cancellation['id']


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TenderCancellationDocumentResourceTest))
    suite.addTest(unittest.makeSuite(TenderCancellationResourceTest))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
