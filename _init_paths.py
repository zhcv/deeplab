import sys, os


def add_path(path):
    if path not in sys.path:
        sys.path.append(path)


currentPath = os.path.dirname(os.path.realpath(__file__))

# Add lib to PYTHONPATH
libPath = '/home/zhang/learning/models/research/slim'
add_path(libPath)
