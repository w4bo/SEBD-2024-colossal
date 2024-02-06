cd ..
latexpand main.tex > other/main.tex.all
cd other
git clone git@github.com:w4bo/CTM-paper.git
cd CTM-paper
git pull
git checkout 9238fd1005fa845a12485504539b21a759beaad5
latexpand main.tex > main.tex.all
cd ..
latexdiff CTM-paper/main.tex.all main.tex.all > ../diff.tex