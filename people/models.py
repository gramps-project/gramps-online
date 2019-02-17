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

from enum import Enum

from django.db import models


class Person(models.Model):
    """
    A natural person,
    modeled after GEDCOM X Person
    http://www.gedcomx.org/v1/Person
    """

    # Choices for Person 'sex' field
    # using 'sex' to conform to contemporary distinction of 'sex' and 'gender' while aligning with GEDCOM X 2.0 roadmap
    # see: https://github.com/FamilySearch/gedcomx/issues/318
    # https://github.com/FamilySearch/gedcomx/issues/319
    # using Enum data structure in accordance with Two Scoops of Django 1.11 (ch. 6.4.8) and the following article
    # https://hackernoon.com/using-enum-as-model-field-choice-in-django-92d8b97aaa63
    class SEX_CHOICES(Enum):
        female = ("female", "Female")
        intersex = ("interses", "Intersex")
        male = ("male", "Male")
        unknown = ("unknown", "Unknown")

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    private = models.BooleanField(
        help_text="Whether this person has been designated for limited distribution or display."
    )
    sex = models.CharField(
        max_length=8,
        choices=[choice.value for choice in SEX_CHOICES],
        null=True,
    )


class Name(models.Model):
    """
    Name of a natural person.
    Modeled after GEDCOM X Name
    https://github.com/FamilySearch/gedcomx/blob/master/specifications/conceptual-model-specification.md#name-conclusion
    """

    # GEDCOM X known name types
    # https://github.com/FamilySearch/gedcomx/blob/master/specifications/conceptual-model-specification.md#known-name-types
    TYPE_BIRTH_NAME = "birth_name"
    TYPE_MARRIED_NAME = "married_name"
    TYPE_ALSO_KNOWN_AS = "also_known_as"
    TYPE_ADOPTIVE_NAME = "adoptive_name"
    TYPE_FORMAL_NAME = "formal_name"
    TYPE_RELIGIOUS_NAME = "religious_name"

    NAME_TYPE_CHOICES = (
        (TYPE_BIRTH_NAME, "Birth name"),
        (TYPE_MARRIED_NAME, "Married name"),
        (TYPE_ALSO_KNOWN_AS, "Also known as"),
        (TYPE_ADOPTIVE_NAME, "Adoptive name"),
        (TYPE_FORMAL_NAME, "Formal name"),
        (TYPE_RELIGIOUS_NAME, "Religious name"),
    )

    person = models.ForeignKey(
        Person,
        null=False,
        on_delete=models.CASCADE,
    )
    type = models.CharField(
        max_length=255,
        choices=NAME_TYPE_CHOICES,
        null=True,
    )
    # TODO: determine how best to model the date field
    # https://github.com/FamilySearch/gedcomx/blob/master/specifications/conceptual-model-specification.md#conclusion-date

# TODO: add NameForms model
