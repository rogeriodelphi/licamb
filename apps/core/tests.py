import pytest
from django.test import TestCase


def test_status_code(resp):
    assert resp.status_code == 200
