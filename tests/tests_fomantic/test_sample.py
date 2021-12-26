#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file was part of Flask-Bootstrap and was modified under the terms of
# its BSD License. Copyright (c) 2013, Marc Brinkmann. All rights reserved.
#
# This file was part of Bootstrap-Flask and was modified under the terms of
# its MIT License. Copyright (c) 2018 Grey Li. All rights reserved.
#
# This file is part of the
# Flask-FomanticUI Project (https://github.com/juniors90/Flask-FomanticUI/).
# Copyright (c) 2021, Ferreira Juan David
# License: MIT
# Full Text: https://github.com/juniors90/Flask-FomanticUI/blob/master/LICENSE

# =====================================================================
# TESTS
# =====================================================================


# =============================================================================
# TEST SAMPLE
# =============================================================================


def test_sample_request(app, client):
    @app.get("/sample")
    def sample():
        return "OK"

    r = client.get("/sample")
    assert r.status_code == 200
    assert r.data == b"OK"
