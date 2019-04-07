#  Gramps Online - an online version of the Gramps genealogy program
#
#  Copyright (C) 2018-2019 Brylie Christopher Oxley
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
from datetime import datetime

from neomodel import (StructuredNode, StringProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom, DateTimeProperty)


class Person(StructuredNode):
    uid = UniqueIdProperty()
    names = RelationshipTo("PersonName", "NAME")

    created = DateTimeProperty(default=datetime.utcnow)

    class Meta:
        app_label = "person"


class PersonName(StructuredNode):
    uid = UniqueIdProperty()
    given_name = StringProperty(index=True)
    family_name = RelationshipTo("FamilyName", "FAMILY_NAME")


class FamilyName(StructuredNode):
    uid = UniqueIdProperty()
    title = StringProperty(index=True)
