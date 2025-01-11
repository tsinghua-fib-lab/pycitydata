# {py:mod}`pycitydata.sateimg.sateimg`

```{py:module} pycitydata.sateimg.sateimg
```

```{autodoc2-docstring} pycitydata.sateimg.sateimg
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_download_one_tile <pycitydata.sateimg.sateimg._download_one_tile>`
  - ```{autodoc2-docstring} pycitydata.sateimg.sateimg._download_one_tile
    :summary:
    ```
* - {py:obj}`download_all_tiles <pycitydata.sateimg.sateimg.download_all_tiles>`
  - ```{autodoc2-docstring} pycitydata.sateimg.sateimg.download_all_tiles
    :summary:
    ```
* - {py:obj}`_concat_img_one_region <pycitydata.sateimg.sateimg._concat_img_one_region>`
  - ```{autodoc2-docstring} pycitydata.sateimg.sateimg._concat_img_one_region
    :summary:
    ```
* - {py:obj}`_concatenate_tiles <pycitydata.sateimg.sateimg._concatenate_tiles>`
  - ```{autodoc2-docstring} pycitydata.sateimg.sateimg._concatenate_tiles
    :summary:
    ```
* - {py:obj}`download_sateimgs <pycitydata.sateimg.sateimg.download_sateimgs>`
  - ```{autodoc2-docstring} pycitydata.sateimg.sateimg.download_sateimgs
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__all__ <pycitydata.sateimg.sateimg.__all__>`
  - ```{autodoc2-docstring} pycitydata.sateimg.sateimg.__all__
    :summary:
    ```
````

### API

````{py:data} __all__
:canonical: pycitydata.sateimg.sateimg.__all__
:value: >
   ['download_sateimgs', 'download_all_tiles']

```{autodoc2-docstring} pycitydata.sateimg.sateimg.__all__
```

````

````{py:function} _download_one_tile(args)
:canonical: pycitydata.sateimg.sateimg._download_one_tile

```{autodoc2-docstring} pycitydata.sateimg.sateimg._download_one_tile
```
````

````{py:function} download_all_tiles(base_url: str, Z: int, Y_X: typing.List[str]) -> typing.Tuple[typing.Dict[str, PIL.Image.Image], typing.List[str]]
:canonical: pycitydata.sateimg.sateimg.download_all_tiles

```{autodoc2-docstring} pycitydata.sateimg.sateimg.download_all_tiles
```
````

````{py:function} _concat_img_one_region(args)
:canonical: pycitydata.sateimg.sateimg._concat_img_one_region

```{autodoc2-docstring} pycitydata.sateimg.sateimg._concat_img_one_region
```
````

````{py:function} _concatenate_tiles(region_list, area_shp: geopandas.GeoDataFrame, cached_tiles: typing.Dict[str, PIL.Image.Image])
:canonical: pycitydata.sateimg.sateimg._concatenate_tiles

```{autodoc2-docstring} pycitydata.sateimg.sateimg._concatenate_tiles
```
````

````{py:function} download_sateimgs(area_shp: geopandas.GeoDataFrame, base_url: str = 'https://wayback.maptiles.arcgis.com/arcgis/rest/services/World_Imagery/WMTS/1.0.0/default028mm/MapServer/tile/41468', Z: int = 15) -> typing.Dict[int, PIL.Image.Image]
:canonical: pycitydata.sateimg.sateimg.download_sateimgs

```{autodoc2-docstring} pycitydata.sateimg.sateimg.download_sateimgs
```
````
