# Copyright (C) 2023 Gerard Roche
#
# This file is part of NeoVintageousHighlightLine.
#
# NeoVintageousHighlightLine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# NeoVintageousHighlightLine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NeoVintageousHighlightLine.  If not, see <https://www.gnu.org/licenses/>.

import sublime
import sublime_plugin

try:
    from NeoVintageous.nv.listener import register

    class Listener():

        def on_insert_enter(self, view, from_mode: str) -> None:
            _highlight_line(view, False)

        def on_insert_leave(self, view, new_mode: str) -> None:
            _highlight_line(view, True)

    register(Listener())

except ImportError:

    # Support for NeoVintageous < 1.32.0

    class NeovintageousLineHighlightCompat(sublime_plugin.EventListener):

        def on_post_text_command(self, view, command_name, args):
            if _is_normal_view(view):
                highlight_line = view.settings().get('highlight_line')
                if view.settings().get('command_mode'):
                    if highlight_line is False:
                        _highlight_line(view, True)
                elif highlight_line is True:
                    _highlight_line(view, False)


if int(sublime.version()) >= 4050:
    def _is_normal_view(view) -> bool:
        return view and view.element() is None
else:
    def _is_normal_view(view) -> bool:
        if not view:
            return False

        settings = view.settings()

        return settings and not settings.get('is_widget', False)


def _highlight_line(view, flag: bool) -> None:
    view.settings().set('highlight_line', flag)
    view.settings().set('highlight_gutter', flag)


class NeovintageousLineHighlight(sublime_plugin.EventListener):

    def on_deactivated(self, view):
        if _is_normal_view(view):
            _highlight_line(view, False)

    def on_activated(self, view):
        if _is_normal_view(view):
            _highlight_line(view, True)
