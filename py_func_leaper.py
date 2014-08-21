import sublime, sublime_plugin

#Jumps down function by function and loops at bottom
class JumpDownFuncCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        region = self.view.sel()[0]
        point = region.begin()

        next_region = self.view.find(r'def \w+\(.*\):', point)

        if not next_region:
            next_region = self.view.find(r'def \w+\(.*\):', 0)

        if next_region:
            next_point = next_region.end()
        
            self.view.sel().clear()
            self.view.sel().add(sublime.Region(next_point))


class JumpUpFuncCommand(sublime_plugin.TextCommand):

    func_lines = None

    def run(self, edit):
        if not self.func_lines:
            self.func_lines = self.view.find_all(r'def \w+\(.*\):')

        region = self.view.sel()[0]

        new_region = -1

        for reg in self.func_lines:
            if reg.begin() < region.begin():
                new_region = sublime.Region(reg.begin())

        if new_region == -1:
            new_region = sublime.Region(self.func_lines[-1].begin())

        self.view.sel().clear()
        self.view.sel().add(new_region)

