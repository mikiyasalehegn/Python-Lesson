## Jupyter Notebook

**What it is**

An open-source tool for writing and running code in small chunks (cells) and seeing results right below each one. Notebooks are saved as `.ipynb` files. It runs locally on your machine; the browser is just the interface.

**Setup on your Mac**

Homebrew’s Python blocks global `pip install`, so use a virtual environment:

bash

```bash
cd ~/Desktop/python-for-data-sciencepython3 -m venv pdata        # "pdata" is just the venv's folder namesource pdata/bin/activate    # prompt shows (pdata)pip install notebookjupyter notebook
```

Next time, just activate the venv and run `jupyter notebook`.

**Key points**

- A virtual environment gives each project its own packages, avoids version conflicts, and protects system Python.
- The venv folder (`pdata`) is only the toolbox. Don’t edit its contents (`bin`, `lib`, etc.), and keep your notebooks next to it, not inside it.
- Jupyter’s file browser starts in the folder you launched it from.
- Install libraries with `pip install ...` while the venv is active, or `!pip install ...` inside a notebook.

**Essentials**

- **Shift + Enter:** run cell
- **Esc / Enter:** command mode / edit mode
- **A / B:** insert cell above / below
- **D, D:** delete cell
- **M / Y:** Markdown / code cell
- **Cmd + S:** save

**Strengths**

- Interactive exploration with instant feedback
- Code, notes, and charts in one document
- Great for learning, prototyping, and quick data checks

**Limitations**

- Cells can run out of order, causing hidden-state bugs
- Hard to test and awkward in Git (notebooks are JSON)
- Not suited for production code or scheduling

**For a data engineer**

Use Jupyter to explore data and prototype logic. Build real pipelines as `.py` scripts or packages, with tests and Git, and run them with an orchestrator such as Airflow, Dagster, or Prefect. A common workflow is: prototype in a notebook, move working logic into a `.py` module, add tests, then schedule it.

**Alternatives**

VS Code or Cursor (with the Jupyter extension) lets you run notebooks without the browser, and Google Colab runs them in the cloud with no setup.