import subprocess

DEVNULL = {'stderr': subprocess.DEVNULL, 'stdout': subprocess.DEVNULL}


class Repository:

    def __init__(self, path):
        self.path = path

    def get_commits(self, path):
        cmd = ['git', 'log', '--format=%an\n%ae\n%at', path]
        out = subprocess.check_output(cmd, cwd=path).decode().split('\n')

        return [(out[i], out[i+1], int(out[i+2])) for i in range(0, len(out) // 3, 3)]

    def get_first_commit(self, path):
        return self.get_commits(path)[-1]

    def get_last_commit(self, path):
        return self.get_commits(path)[0]

    def check_tree_is_clean(self):

        clean = True

        try:
            subprocess.check_call(['git', 'diff-index', '--quiet', 'HEAD', '--'], cwd=self.path)
        except subprocess.CalledProcessError:
            clean = False

        return clean

    def list_branches(self):

        cmd = ['git', 'branch', '-a', '--format', '%(refname)']
        out = subprocess.check_output(cmd, cwd=self.path).decode().split('\n')
        branches = set(b.split('/')[-1] for b in out if b)

        for b in 'HEAD', 'master':
            if b in branches:
                branches.remove(b)

        return ['master'] + sorted(branches)

    def checkout_branch(self, branch):
        subprocess.check_call(['git', 'checkout', branch], **DEVNULL, cwd=self.path)

    def get_current_branch(self):
        for l in subprocess.check_output(['git', 'branch'], cwd=self.path).decode().split('\n'):
            if l.startswith('*'):
                return l[2:]

    def is_git_repo(self):
        try:
            subprocess.check_call(['git', 'status'], cwd=self.path, **DEVNULL)
            return True
        except subprocess.CalledProcessError:
            return False