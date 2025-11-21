# Pokemon Graph Visualization

This project visualizes pokemon data from "pokemon_data.csv" using d3.js and Python. 
It includes a dashboard with three main interactive views:

- **graph view**  
  - pokemon nodes are positioned using a force-directed layout  
  - edges connect pokemon that share at least one type  
  - zoomable and pannable  
  - click nodes to view detailed information, including stats, types, abilities, and sprite  

- **chord view**  
  - visualizes type interactions  
  - hover over chords to see the number of pokemon for each type combination  

- **splatter plot**  
  - compare stats (atk/def or sp atk/sp def)  
  - toggle between normal and special stats  
  - contour density overlay highlights pokemon distributions  
  - nodes color-coded by type, with gradients for dual types  
  - click nodes to see detailed info  

---

## project structure

Hannah_Facci_Final/
|-- pokemon_d3.html # main d3.js visualization
|-- graph_script.py # python script for processing CSV into JSON
|-- pokemon_data.csv # original pokemon dataset
|-- pokemon_graph_fixed.json # preprocessed JSON for visualization
|-- README.md # project description

## how to run

1. download zip file
2. unzip files
3. copy unzipped folder path 
4. run a local server using python (ensure you are in the same drive as the unzipped folder):

```bash
cd # paste path here
python -m http.server
```
    then visit http://localhost:8000 in your browser. 
    all project files should be visible. 
    click on the hyperlink for pokemon_d3.html to open it

## data source

The data for this project comes from hg-engine, 
a C-injection community project that aims to implement all modern Pokemon game features into older early 2000s Nintendo DS hacks. 
Binary, assembly, and C injection are all utilized to accomplish this.

The original .txt file was converted to .db by first creating an empty sqlite schema, 
then populating it by using python to parse through the .txt file. 
This was an intensive process done locally in command line. 
The .db file was converted into a DataFrame, cleaned further, and had sprites added as part of a previous project.
The .df was download as the "pokemon_data.csv" used for this project.

original txt source: https://github.com/blurosie/hg-engine

each node includes: 
    ID
    name
    type1 (type2 if applicable)
    stats(hp, atk, def, spd, sp atk, sp def)
    ability1 (ability2 if applicable)
    sprite URL

## technologies used

- d3.js v7
- html and css
- python and networkx - local
- python - Google Colaboratory 
- JSON
- D3 Gallery https://observablehq.com/@d3/gallery
- The D3.js Graph Gallery https://d3-graph-gallery.com/index.html
- ChatGPT for formatting and debugging


## author

Hannah Facci
created for DATA 760 Visualization and Communication