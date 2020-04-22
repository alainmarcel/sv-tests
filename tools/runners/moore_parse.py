#!/bin/false python3
#
# Copyright (C) 2020 The SymbiFlow Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC

from runners.moore import moore


class moore_parse(moore):
    def __init__(self):
        super().__init__("moore-parse")

    def prepare_run_cb(self, tmp_dir, params):
        self.cmd = [self.executable, '--syntax']

        for incdir in params['incdirs']:
            self.cmd.append('-I')
            self.cmd.append(incdir)

        self.cmd += params['files']
