import sublime, sublime_plugin
import re

class JumpToFuncCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        region = self.view.sel()[0]
        point = region.a

        next_region = self.view.find(r'def \w+\(.*\):', point)

        next_point = next_region.b
        
        self.view.sel().clear()
        self.view.sel().add(sublime.Region(next_point))