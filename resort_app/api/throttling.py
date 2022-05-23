from rest_framework.throttling import UserRateThrottle


class ResortListThrottle(UserRateThrottle):
    scope = 'resort-list'


class PointofInterestThrottle(UserRateThrottle):
    scope = 'poi-list'
