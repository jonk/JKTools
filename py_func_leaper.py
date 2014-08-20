import sublime, sublime_plugin

<<<<<<< HEAD
=======
found_regions = []

>>>>>>> 1593a2de5bd09e7e00f8309e24e2f9672db3194a
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