# {py:mod}`pycitydata.sateimg._utils`

```{py:module} pycitydata.sateimg._utils
```

```{autodoc2-docstring} pycitydata.sateimg._utils
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_one_point <pycitydata.sateimg._utils.get_one_point>`
  - ```{autodoc2-docstring} pycitydata.sateimg._utils.get_one_point
    :summary:
    ```
* - {py:obj}`deg2XY <pycitydata.sateimg._utils.deg2XY>`
  - ```{autodoc2-docstring} pycitydata.sateimg._utils.deg2XY
    :summary:
    ```
* - {py:obj}`XY2deg <pycitydata.sateimg._utils.XY2deg>`
  - ```{autodoc2-docstring} pycitydata.sateimg._utils.XY2deg
    :summary:
    ```
* - {py:obj}`compute_tile_coordinates <pycitydata.sateimg._utils.compute_tile_coordinates>`
  - ```{autodoc2-docstring} pycitydata.sateimg._utils.compute_tile_coordinates
    :summary:
    ```
* - {py:obj}`XY2deg_batch <pycitydata.sateimg._utils.XY2deg_batch>`
  - ```{autodoc2-docstring} pycitydata.sateimg._utils.XY2deg_batch
    :summary:
    ```
* - {py:obj}`create_tile_polygons <pycitydata.sateimg._utils.create_tile_polygons>`
  - ```{autodoc2-docstring} pycitydata.sateimg._utils.create_tile_polygons
    :summary:
    ```
* - {py:obj}`geometry_to_listXY <pycitydata.sateimg._utils.geometry_to_listXY>`
  - ```{autodoc2-docstring} pycitydata.sateimg._utils.geometry_to_listXY
    :summary:
    ```
* - {py:obj}`get_YX_area <pycitydata.sateimg._utils.get_YX_area>`
  - ```{autodoc2-docstring} pycitydata.sateimg._utils.get_YX_area
    :summary:
    ```
````

### API

````{py:function} get_one_point(shp)
:canonical: pycitydata.sateimg._utils.get_one_point

```{autodoc2-docstring} pycitydata.sateimg._utils.get_one_point
```
````

````{py:function} deg2XY(lon_deg, lat_deg, zoom=15)
:canonical: pycitydata.sateimg._utils.deg2XY

```{autodoc2-docstring} pycitydata.sateimg._utils.deg2XY
```
````

````{py:function} XY2deg(x, y, zoom=15)
:canonical: pycitydata.sateimg._utils.XY2deg

```{autodoc2-docstring} pycitydata.sateimg._utils.XY2deg
```
````

````{py:function} compute_tile_coordinates(min_x, max_x, min_y, max_y)
:canonical: pycitydata.sateimg._utils.compute_tile_coordinates

```{autodoc2-docstring} pycitydata.sateimg._utils.compute_tile_coordinates
```
````

````{py:function} XY2deg_batch(x_arr, y_arr, zoom=15)
:canonical: pycitydata.sateimg._utils.XY2deg_batch

```{autodoc2-docstring} pycitydata.sateimg._utils.XY2deg_batch
```
````

````{py:function} create_tile_polygons(lon_arr, lat_arr, x_arr, y_arr)
:canonical: pycitydata.sateimg._utils.create_tile_polygons

```{autodoc2-docstring} pycitydata.sateimg._utils.create_tile_polygons
```
````

````{py:function} geometry_to_listXY(geometry)
:canonical: pycitydata.sateimg._utils.geometry_to_listXY

```{autodoc2-docstring} pycitydata.sateimg._utils.geometry_to_listXY
```
````

````{py:function} get_YX_area(area_shp)
:canonical: pycitydata.sateimg._utils.get_YX_area

```{autodoc2-docstring} pycitydata.sateimg._utils.get_YX_area
```
````
