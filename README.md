# COMP5001 Artificial Intelligence: Practical Code

Code for the weekly practicals of **COMP5001 Artificial Intelligence** at the University of Winchester, 2026–27. Each week has its own folder. Part 1 of the portfolio also starts from this code.

**Module website** (slides, notes, seminar sheets and the assessment brief): <https://sakibanwar.github.io/COMP5001-Artificial-Intelligence-26-27/>

**Lecture notes** (every week's notes in one place, to read online or as PDFs): <https://sakibanwar.github.io/COMP5001-Artificial-Intelligence-26-27/notes/>

## Download

- **Easiest:** click the green **Code** button above, choose **Download ZIP**, then unzip it.
- **With Git:** `git clone https://github.com/sakibanwar/comp5001-ai-code.git`

## Set up

1. Install Python 3 from [python.org](https://www.python.org).
2. In a terminal, go into the week's folder and install its packages:

   ```
   cd week02-search
   pip install -r requirements.txt
   ```

3. Run the programs as shown in the practical, for example `python maze/maze.py maze/maze1.txt`.

## Weeks

| Week | Topic | Folder | What you use | Packages |
|---|---|---|---|---|
| 1 | Introduction | none | Week 1 has no code | |
| 2 | Search | [`week02-search`](week02-search) | `maze.py` and `maze1.txt` to `maze3.txt` | pillow |
| 3 | Heuristics and Logic | [`week04-knowledge/logic`](week04-knowledge/logic) and [`week02-search`](week02-search) | `logic.py` and `harry.py`; `maze4.txt`, the greedy best-first trap | termcolor; pillow |
| 4 | Knowledge and Planning | [`week04-knowledge/logic`](week04-knowledge/logic) and [`week03-planning/blocks`](week03-planning/blocks) | `clue.py` (also `mastermind.py` and `puzzle.py`); `blocks.py`, problem files, PDDL files | termcolor; none |
| 5 | Uncertainty, Part 1: probability | none | the practical is on paper | |
| 6, Lecture 1 | Uncertainty, Part 2: Bayesian networks and Markov models | [`week05-uncertainty`](week05-uncertainty) | Bayesian network (`bayesnet`), Markov chain (`chain`), hidden Markov model (`hmm`) | pomegranate (below 1.0) |
| 6, Lecture 2 | Optimization | [`week06-optimization`](week06-optimization) | hill climbing (`hospitals`), linear programming (`production`), constraint satisfaction (`scheduling`) | pillow, scipy, python-constraint |
| 7 | Learning | [`week07-learning`](week07-learning) | banknote classifiers in scikit-learn | scikit-learn |
| 8 | Neural Networks | [`week08-neural-networks`](week08-neural-networks) | banknotes, image convolution, handwritten digits | tensorflow, scikit-learn, pillow, pygame |
| 9 | Language | [`week09-language`](week09-language) | grammars, n-grams, Markov text, sentiment, word vectors | nltk, markovify, scipy, numpy |
| 10 | AI in practice and revision | none | no new code; portfolio clinic | |

The folder names follow an earlier order of topics, so they do not always match the teaching week: Week 3 uses `week04-knowledge`, Week 4 also uses `week03-planning`, and Week 6 (Lecture 1) uses `week05-uncertainty`. Go by the table above.

**Notes**

- **Week 6, Lecture 1** (`week05-uncertainty`): the code uses the old pomegranate library (`pip install "pomegranate<1.0"`), which may not install on the newest versions of Python. If it will not install, tell us in the practical: the paper exercise works without it.
- **Week 8:** if `model.h5` will not load in your version of TensorFlow, run `handwriting.py` to train a new model first.
- **Week 9:** the first run may ask for NLTK data. In Python, run `import nltk; nltk.download("punkt")` (or `"punkt_tab"` on newer versions of NLTK).

## Using this code in your portfolio

Part 1 of the portfolio asks you to adapt one of these programs. Say in your write-up which program you started from and what you changed. Generative AI tools are **not permitted** in the portfolio: see the assessment brief for the full policy.

Data for the portfolio is in the [`portfolio`](portfolio) folder: [`deliveries.csv`](portfolio/deliveries.csv) is the data for Part 1, problem 4 (Late deliveries), which starts from `week07-learning/banknotes/banknotes0.py`.

## Credits and licence

The code in every folder except `week03-planning` is the lecture source code from **CS50's Introduction to Artificial Intelligence with Python** by Brian Yu and David J. Malan, Harvard University ([cs50.harvard.edu/ai](https://cs50.harvard.edu/ai)). It is used here unchanged, apart from the folder layout and the `requirements.txt` files.

The planning code in `week03-planning` (`blocks.py` and the problem and PDDL files), used in Week 4, was written for COMP5001 and adapts CS50's `maze.py`. `maze4.txt` in `week02-search` was also made for COMP5001.

`portfolio/deliveries.csv` was made up for the COMP5001 assessment.

All of this material is shared under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International licence](https://creativecommons.org/licenses/by-nc-sa/4.0/) (CC BY-NC-SA 4.0), the same licence as CS50's materials. You may share and adapt it for non-commercial purposes, as long as you give credit and share your adaptations under the same licence. See [LICENSE.md](LICENSE.md).
