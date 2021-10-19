-- Copyright (C) 2018-2020 Dmitry Marakasov <amdmi3@amdmi3.ru>
--
-- This file is part of repology
--
-- repology is free software: you can redistribute it and/or modify
-- it under the terms of the GNU General Public License as published by
-- the Free Software Foundation, either version 3 of the License, or
-- (at your option) any later version.
--
-- repology is distributed in the hope that it will be useful,
-- but WITHOUT ANY WARRANTY; without even the implied warranty of
-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
-- GNU General Public License for more details.
--
-- You should have received a copy of the GNU General Public License
-- along with repology.  If not, see <http://www.gnu.org/licenses/>.

--------------------------------------------------------------------------------
--
-- @returns array of dicts
--
--------------------------------------------------------------------------------
SELECT
	state != 'legacy'::repository_state AS active,

	name,
	"desc",

	metadata,

	COALESCE(used_package_fields, '{}'::text[]) AS used_package_fields,
	COALESCE(used_package_link_types, '{}'::int[]) AS used_package_link_types,

	num_metapackages,
	num_metapackages_newest
FROM repositories
ORDER BY sortname;
