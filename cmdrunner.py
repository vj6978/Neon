from neonrunner import NeonRunner

runner = NeonRunner(".\\input.txt")
print(*runner(), sep="\n")