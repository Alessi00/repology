# Copyright (C) 2016-2020 Dmitry Marakasov <amdmi3@amdmi3.ru>
#
# This file is part of repology
#
# repology is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# repology is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with repology.  If not, see <http://www.gnu.org/licenses/>.

__all__ = ['is_fallback_maintainer', 'for_page', 'has_flag', 'has_flag_at']


def is_fallback_maintainer(maintainer: str) -> bool:
    return maintainer.startswith('fallback-mnt-') and maintainer.endswith('@repology')


def for_page(value: str, letter: str | None = None) -> bool:
    if letter is None or letter == '0':
        return not value or value < 'a'
    elif letter >= 'z':
        return bool(value and value >= 'z')
    else:
        return bool(value and value >= letter and value < chr(ord(letter) + 1))


def has_flag(value: int, flag: int) -> bool:
    return bool(value & flag)


def has_flag_at(value: int, bitpos: int) -> bool:
    return bool(value & (1 << bitpos))
