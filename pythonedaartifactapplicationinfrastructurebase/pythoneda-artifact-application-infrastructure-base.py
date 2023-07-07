#!/usr/bin/env python3
"""
pythonedaartifactapplicationinfrastructurebase/pythoneda-artifact-application-infrastructure-base.py

This file defines InfrastructureBase.

Copyright (C) 2023-today rydnr's pythoneda-artifact-application/infrastructure-base

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythonedaapplication.pythoneda import PythonEDA

import asyncio

class InfrastructureBase(PythonEDA):
    """
    PythonEDA application that runs Infrastructure-Base artifact space.

    Class name: InfrastructureBase

    Responsibilities:
        - Runs Infrastructure-Base artifact space.

    Collaborators:
        - None
    """
    def __init__(self):
        """
        Creates a new InfrastructureBase instance.
        """
        super().__init__(__file__)

if __name__ == "__main__":

    asyncio.run(InfrastructureBase.main())
