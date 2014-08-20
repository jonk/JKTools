import sublime, sublime_plugin

found_regions = []

#Jumps down function by function and loops at bottom
class JumpDownFuncCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        region = self.view.sel()[0]
        point = region.a

        next_region = self.view.find(r'def \w+\(.*\):', point)

        if not next_region:
            next_region = self.view.find(r'def \w+\(.*\):', 0)

        if next_region:
            next_point = next_region.end()
        
            self.view.sel().clear()
            self.view.sel().add(sublime.Region(next_point))

#TODO
class JumpUpFuncCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        pass