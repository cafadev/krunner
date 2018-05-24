import subprocess


class Shell:

    def __init__(self, window, shell, command, main_file=str()):
        self.window = window
        self.shell = shell
        self.command = command
        self.main_file = main_file

    def get_shell_command(self):
        folder = self.window.extract_variables()['folder']
        if self.shell == 'deepin-terminal':
            return (
                "%s -w \"%s\" -e \"%s\"" %
                (self.shell, folder, "\" \"".join(self.command))
            )
        elif self.shell == 'gnome-terminal':
            return (
                "%s --working-directory=\"%s\" -- \"%s\"" %
                (self.shell, folder, "\" \"".join(self.command))
            )
        elif self.shell == 'xfce4-terminal':
            return (
                "%s --working-directory=\"%s\" -H -e '\"%s\"'" %
                (self.shell, folder, "\" \"".join(self.command))
            )
        elif self.shell == 'xterm':
            return (
                "%s -hold -T 'Running' -e 'cd %s && \"%s\" && echo \"\
                \t****Finished****\"'" %
                (self.shell, folder, "\" \"".join(self.command))
            )
        elif self.shell == 'konsole':
            return (
                "%s --hold --workdir \"%s\" -e \"%s\"" %
                (self.shell, folder, "\" \"".join(self.command))
            )
        #  elif self.shell == 'pantheon-terminal':
        #     return (
        #         "%s --working-directory=\"%s\" -e \"%s\"" %
        #         (self.shell, folder, "ls")
        #     )

        return None

    def run(self):
        execute = self.get_shell_command()

        if execute is None:
            return

        print(execute)
        subprocess.Popen(execute, shell=True)
        self.window.status_message(
            "\tPlease wait... Running %s" % self.main_file
        )
