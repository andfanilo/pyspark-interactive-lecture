# Quest for an interactive pyspark lecture

## Objective

I have one month to write a slidedeck for a hour and a half lecture to students about Spark and reproducible analysis with Python. It is a lecture I already did last year, so I have most of my ideas fleshed out. But I wanted to give my lecture more punch, and as I was reading "Resonate" from Nancy Duarte, I realized I didn't want to give a simple lecture with boring Spark MapReduce examples. 

Because of this book, I wanted this lecture to transform my students and have them wanting to go to the following tutorial lesson, wanting to learn how to do Spark and Python and pip and Jupyter.

## Interactive Pyspark inside the presentation

My very first idea was to have an interactive showoff of Pyspark, and have it fully integrated inside the presentation. With that, I would be able to ask questions in a cell, and in the following fragment try to interactively solve the problem with the students and show how we think about processing data in Spark.

After looking on the Internet, I came accross [RISE](https://damianavila.github.io/RISE/), a Jupyter notebook extension for converting it into a Reveal.js presentation, so my initial though would be to test it.

```
conda create -n pyspark-interactive-environment python=3
conda install -c damianavila82 rise
pip install pyspark
```

Installing RISE and Pyspark in a Conda environment proved easy, and my first steps with RISE seemed to work well.

## Exporting RISE Jupyter notebooks with Decktape

Even before writing anything in the presentation, I looked for a way to export the Reveal.js result as a PDF, because I know some students only want the PDF version.

I did a first experiment with `nbconvert` and the results were somewhat good, but the HTML file was not formatted as a Reveal.js file, so I looked into alternatives.

With a bit of Googling, I arrived on [decktape](https://github.com/astefanutti/decktape), a PDF exporter for HTML presentations, and it happens they had just integrated RISE. Thankfully I knew enough node to be able to install it in the same project folder through a `package.json` file. In the following I tried to launch a notebook and run dektape on it :

```
npm install
jupyter notebook
npm run export
```

I had some issues, first I had the following error:

```
Error: Unable to activate the RISE DeckTape plugin for the address: http://localhost:8888/notebooks/lecture.ipynb
```

Found it in [this issue](https://github.com/astefanutti/decktape/issues/110#issuecomment-327772410), and I was kind of in a hurry so I just deactivated token based authentication on my Jupyter notebook, as I am supposed to only work locally on this project I don't expect many people to connect to it :

```
jupyter notebook --NotebookApp.token=""
npm run export
```

A new problem emerged, because when running decktape on the notebook, I was supposed to see `RISE plugin activated` in the output. It never appeared, fortunately [a new comment from Github](https://github.com/astefanutti/decktape/issues/110#issuecomment-345213981) came to my help: I was using RISE 5.1.0 and decktape 2.6.1, and the button id for RISE changed from "start_livereveal" to "RISE". Replacing "start_livereveal" with "RISE" in the `node_modules/rise.js` file makes the export work. 

Last but not least, I did not want the browser to pop when I started Jupyter notebook for an export, so I added the `--no-browser` flag. At the end, this is our final command:

```
jupyter notebook --NotebookApp.token="" --no-browser
npm run export
```

## Automating tasks with Invoke

## Experimenting with Pyspark

