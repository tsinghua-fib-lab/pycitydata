# {py:mod}`pycitydata.streetview.google`

```{py:module} pycitydata.streetview.google
```

```{autodoc2-docstring} pycitydata.streetview.google
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Panorama <pycitydata.streetview.google.Panorama>`
  - ```{autodoc2-docstring} pycitydata.streetview.google.Panorama
    :summary:
    ```
* - {py:obj}`GoogleStreetView <pycitydata.streetview.google.GoogleStreetView>`
  - ```{autodoc2-docstring} pycitydata.streetview.google.GoogleStreetView
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__all__ <pycitydata.streetview.google.__all__>`
  - ```{autodoc2-docstring} pycitydata.streetview.google.__all__
    :summary:
    ```
````

### API

````{py:data} __all__
:canonical: pycitydata.streetview.google.__all__
:value: >
   ['Panorama', 'GoogleStreetView']

```{autodoc2-docstring} pycitydata.streetview.google.__all__
```

````

`````{py:class} Panorama
:canonical: pycitydata.streetview.google.Panorama

```{autodoc2-docstring} pycitydata.streetview.google.Panorama
```

````{py:attribute} pano_id
:canonical: pycitydata.streetview.google.Panorama.pano_id
:type: str
:value: >
   None

```{autodoc2-docstring} pycitydata.streetview.google.Panorama.pano_id
```

````

````{py:attribute} lat
:canonical: pycitydata.streetview.google.Panorama.lat
:type: float
:value: >
   None

```{autodoc2-docstring} pycitydata.streetview.google.Panorama.lat
```

````

````{py:attribute} lon
:canonical: pycitydata.streetview.google.Panorama.lon
:type: float
:value: >
   None

```{autodoc2-docstring} pycitydata.streetview.google.Panorama.lon
```

````

````{py:attribute} heading
:canonical: pycitydata.streetview.google.Panorama.heading
:type: float
:value: >
   None

```{autodoc2-docstring} pycitydata.streetview.google.Panorama.heading
```

````

````{py:attribute} pitch
:canonical: pycitydata.streetview.google.Panorama.pitch
:type: typing.Optional[float]
:value: >
   None

```{autodoc2-docstring} pycitydata.streetview.google.Panorama.pitch
```

````

````{py:attribute} roll
:canonical: pycitydata.streetview.google.Panorama.roll
:type: typing.Optional[float]
:value: >
   None

```{autodoc2-docstring} pycitydata.streetview.google.Panorama.roll
```

````

````{py:attribute} date
:canonical: pycitydata.streetview.google.Panorama.date
:type: typing.Optional[str]
:value: >
   None

```{autodoc2-docstring} pycitydata.streetview.google.Panorama.date
```

````

`````

`````{py:class} GoogleStreetView(meta: pycitydata.streetview.google.Panorama, zoom: int = 4, headers: typing.Optional[typing.Dict[str, str]] = None, proxies: typing.Optional[typing.Dict[str, str]] = None)
:canonical: pycitydata.streetview.google.GoogleStreetView

```{autodoc2-docstring} pycitydata.streetview.google.GoogleStreetView
```

```{rubric} Initialization
```

```{autodoc2-docstring} pycitydata.streetview.google.GoogleStreetView.__init__
```

````{py:property} heading
:canonical: pycitydata.streetview.google.GoogleStreetView.heading
:type: float

```{autodoc2-docstring} pycitydata.streetview.google.GoogleStreetView.heading
```

````

````{py:method} _extract_meta(text: str) -> typing.List[pycitydata.streetview.google.Panorama]
:canonical: pycitydata.streetview.google.GoogleStreetView._extract_meta
:staticmethod:

```{autodoc2-docstring} pycitydata.streetview.google.GoogleStreetView._extract_meta
```

````

````{py:method} search(lng: float, lat: float, zoom: int = 4, headers: typing.Optional[typing.Dict[str, str]] = None, proxies: typing.Optional[typing.Dict[str, str]] = None, cache_dir: typing.Union[str, pathlib.Path, None] = None) -> pycitydata.streetview.google.GoogleStreetView
:canonical: pycitydata.streetview.google.GoogleStreetView.search
:staticmethod:

```{autodoc2-docstring} pycitydata.streetview.google.GoogleStreetView.search
```

````

````{py:method} _query_img()
:canonical: pycitydata.streetview.google.GoogleStreetView._query_img

```{autodoc2-docstring} pycitydata.streetview.google.GoogleStreetView._query_img
```

````

`````
