"""
settings.py Documentation
"""
import os

STATIC_VERSION_NUMBER = 1

ENVIRONMENT = "PROD"
SERVER_ADDRESS = "http://po.cdac.ca/"
if os.environ['APPLICATION_ID'].find("cdac-demo-purchaseorder") >= 0:
    SERVER_ADDRESS = "http://cdac-demo-purchaseorder.appspot.com/"
    ENVIRONMENT = "DEMO"
if 'SERVER_SOFTWARE' in os.environ and os.environ['SERVER_SOFTWARE'].startswith('Development'):
    SERVER_ADDRESS = "http://localhost:8080/"
    ENVIRONMENT = "LOCAL"

APPROVAL_ADMINS = [
    "gdholtslander",
    "gholtslander",
    # "lkrieg",
    "smyhre",
    "test@example.com"
]

FINANCE_ADMINS = [
    "dwiebe",
    "gdholtslander",
    "test@example.com"
]

POS_FOR_PURCHASER_MEMCACHE_KEY = 'all-pos-for-{}'
ALL_POS_ORDERED_MEMCACHE_KEY = 'all-pos-for-order-{}'
