# Copyright (C) 2016-2019 Dmitry Marakasov <amdmi3@amdmi3.ru>
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

from typing import Any

from repologyapp.config import config
from repologyapp.fontmeasurer import FontMeasurer
from repologyapp.repometadata import RepositoryMetadata


__all__ = [
    'get_text_width',
    'repometadata',
]


_fontmeasurers: dict[tuple[int, bool], FontMeasurer] = {}

repometadata = RepositoryMetadata()


def get_text_width(text: Any, fontsize: int, bold: bool = False) -> int:
    fontpath = config['BADGE_FONT_BOLD'] if bold else config['BADGE_FONT']
    key = (fontsize, bold)

    if key not in _fontmeasurers:
        _fontmeasurers[key] = FontMeasurer(fontpath, fontsize)

    return _fontmeasurers[key].get_text_width(str(text))
