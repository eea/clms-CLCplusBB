# Landscape Fragmentation with CLCplus Backbone

Jupyter notebook for assessing landscape fragmentation using the [CLCplus Backbone 2023](https://land.copernicus.eu/en/products/clc-backbone) 10 m land cover dataset from the Copernicus Land Monitoring Service.

## What it does

- Visualises land cover for 23 Polish national parks on interactive maps
- Computes **boundary length** and **edge density** metrics for park and buffer zones
- Generates class-pair boundary matrices to identify dominant land cover transitions
- Compares fragmentation between park interiors and surrounding 1 km buffer areas

## Structure

- `landscape_fragmentation_with_CLCplusBB.ipynb` — main notebook
- `modules/` — analysis, mapping, and utility functions
- `aoi_rasters/` — pre-cropped CLCplus BB rasters (parks and buffers)
- `aoi_vectors/` — national park boundary GeoJSONs (EPSG:4326)

## Quick start

Open `landscape_fragmentation_with_CLCplusBB.ipynb` and run the cells sequentially. Dependencies (`rasterio`, `folium`, `geopandas`, etc.) are installed in the first cell.