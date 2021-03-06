from uuid import uuid4

from openprocurement.api.utils import get_now

from openprocurement.auctions.core.tests.base import snitch
from openprocurement.auctions.core.plugins.awarding.v2.tests.blanks.award_blanks import (
    # AuctionAwardProcessTest
    invalid_patch_auction_award,
    patch_auction_award,
    patch_auction_award_admin,
    complate_auction_with_second_award1,
    complate_auction_with_second_award2,
    complate_auction_with_second_award3,
    unsuccessful_auction1,
    unsuccessful_auction2,
    unsuccessful_auction3,
    unsuccessful_auction4,
    unsuccessful_auction5,
    get_auction_awards,
    successful_second_auction_award,
    # CreateAuctionAwardTest
    create_auction_award_invalid,
    create_auction_award
)


def award_fixture(auction, status, bid_index):
    now = get_now()
    return {
        "id": uuid4().hex,
        "date": now.isoformat(),
        "bid_id": auction["bids"][bid_index]["id"],
        "status": status,
        "suppliers": auction["bids"][bid_index]["tenderers"],
        'value': auction['value'],
        "complaintPeriod": {
            "startDate": now.isoformat(),
        },
        "paymentPeriod": {
            "startDate": now.isoformat()
        },
        "signingPeriod": {
            "startDate": now.isoformat(),
            "endDate": now.isoformat(),
        },
        "verificationPeriod": {
            "startDate": now.isoformat()
        }
    }


class AuctionAwardProcessTestMixin(object):
    test_invalid_patch_auction_award = snitch(invalid_patch_auction_award)
    test_patch_auction_award = snitch(patch_auction_award)
    test_patch_auction_award_admin = snitch(patch_auction_award_admin)
    test_complate_auction_with_second_award1 = snitch(complate_auction_with_second_award1)
    test_complate_auction_with_second_award2 = snitch(complate_auction_with_second_award2)
    test_complate_auction_with_second_award3 = snitch(complate_auction_with_second_award3)
    test_successful_second_auction_award = snitch(successful_second_auction_award)
    test_unsuccessful_auction1 = snitch(unsuccessful_auction1)
    test_unsuccessful_auction2 = snitch(unsuccessful_auction2)
    test_unsuccessful_auction3 = snitch(unsuccessful_auction3)
    test_unsuccessful_auction4 = snitch(unsuccessful_auction4)
    test_unsuccessful_auction5 = snitch(unsuccessful_auction5)
    test_get_auction_awards = snitch(get_auction_awards)


class CreateAuctionAwardTestMixin(object):
    test_create_auction_award_invalid = snitch(create_auction_award_invalid)
    test_create_auction_award = snitch(create_auction_award)
