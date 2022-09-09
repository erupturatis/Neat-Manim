
# Neat Manim

A repository made for visualizing the neat algorithm 
networks evolving over the course of multiple generations. 
This is an attempt to reproduce videos like 
[this one](https://www.youtube.com/watch?v=j8oU0ksQ3Bc&t=0s) 
that unfortunately haven't published their repositories



## Run Locally

Clone the project

```bash
  git clone https://github.com/erupturatis/Neat-Manim
```

Go to the project directory

```bash
  cd Neat-Manim
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Note that you have to have manim already installed on your local machine in order to install it with pip. This project uses [manim community](https://github.com/ManimCommunity/manim). You can see how to install it [here](https://docs.manim.community/en/stable/installation.html).
For a quick startup on the manim library you should check [this playlist](https://www.youtube.com/watch?v=rUsUrbWb2D4&list=PLsMrDyoG1sZm6-jIUQCgN3BVyEVOZz3LQ)



### Folder structure and usage

To start with working with this project you should run:
```bash
  cd NeatManim
```
And then:
```bash
  manim -pql manim-visualization.py VisualizeNetwork
```
This will run the main scene that will run all the other scrips.
Your winner files should be placed in 

```
./NeatManim/winners/winner_list/...(here are the winners)
```
The folder should also contain a contain a config.txt file corresponding to the winners in
```
./NeatManim/winners/...(here is the config)
```
And a winners_names.txt file in the same place as the config
```
./NeatManim/winners/...(winners_names)
```
You have some boilerplate winner already placed in there as an example
. If for any reason you can't get this to work feel free to open an issue

## Results
This is the kind of result you should expect
![App Screenshot](https://cdn.discordapp.com/attachments/867039131917090816/1016744132158427257/unknown.png)


## Contributing

All contributions are always welcome! I would like to expand the functionality of this repo for more machine and deep learning algorithms and eventually turn it into a library.

You could start by editing  `contributing.md`

