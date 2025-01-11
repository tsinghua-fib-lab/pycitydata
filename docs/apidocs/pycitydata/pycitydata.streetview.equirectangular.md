# {py:mod}`pycitydata.streetview.equirectangular`

```{py:module} pycitydata.streetview.equirectangular
```

```{autodoc2-docstring} pycitydata.streetview.equirectangular
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Equirectangular <pycitydata.streetview.equirectangular.Equirectangular>`
  - ```{autodoc2-docstring} pycitydata.streetview.equirectangular.Equirectangular
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__all__ <pycitydata.streetview.equirectangular.__all__>`
  - ```{autodoc2-docstring} pycitydata.streetview.equirectangular.__all__
    :summary:
    ```
````

### API

````{py:data} __all__
:canonical: pycitydata.streetview.equirectangular.__all__
:value: >
   ['Equirectangular']

```{autodoc2-docstring} pycitydata.streetview.equirectangular.__all__
```

````

`````{py:class} Equirectangular(sv: typing.Union[pycitydata.streetview.baidu.BaiduStreetView, pycitydata.streetview.google.GoogleStreetView])
:canonical: pycitydata.streetview.equirectangular.Equirectangular

```{autodoc2-docstring} pycitydata.streetview.equirectangular.Equirectangular
```

```{rubric} Initialization
```

```{autodoc2-docstring} pycitydata.streetview.equirectangular.Equirectangular.__init__
```

````{py:method} pil2cv(img: PIL.Image.Image)
:canonical: pycitydata.streetview.equirectangular.Equirectangular.pil2cv
:staticmethod:

```{autodoc2-docstring} pycitydata.streetview.equirectangular.Equirectangular.pil2cv
```

````

````{py:method} cv2pil(img: numpy.ndarray)
:canonical: pycitydata.streetview.equirectangular.Equirectangular.cv2pil
:staticmethod:

```{autodoc2-docstring} pycitydata.streetview.equirectangular.Equirectangular.cv2pil
```

````

````{py:method} _xyz2lonlat(xyz)
:canonical: pycitydata.streetview.equirectangular.Equirectangular._xyz2lonlat
:staticmethod:

```{autodoc2-docstring} pycitydata.streetview.equirectangular.Equirectangular._xyz2lonlat
```

````

````{py:method} _lonlat2XY(lonlat, shape)
:canonical: pycitydata.streetview.equirectangular.Equirectangular._lonlat2XY
:staticmethod:

```{autodoc2-docstring} pycitydata.streetview.equirectangular.Equirectangular._lonlat2XY
```

````

````{py:method} get_perspective(fov: float, heading: float, pitch: float, height: float, width: float)
:canonical: pycitydata.streetview.equirectangular.Equirectangular.get_perspective

```{autodoc2-docstring} pycitydata.streetview.equirectangular.Equirectangular.get_perspective
```

````

`````
