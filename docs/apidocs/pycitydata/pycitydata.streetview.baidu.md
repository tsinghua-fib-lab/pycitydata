# {py:mod}`pycitydata.streetview.baidu`

```{py:module} pycitydata.streetview.baidu
```

```{autodoc2-docstring} pycitydata.streetview.baidu
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaiduStreetView <pycitydata.streetview.baidu.BaiduStreetView>`
  - ```{autodoc2-docstring} pycitydata.streetview.baidu.BaiduStreetView
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__all__ <pycitydata.streetview.baidu.__all__>`
  - ```{autodoc2-docstring} pycitydata.streetview.baidu.__all__
    :summary:
    ```
````

### API

````{py:data} __all__
:canonical: pycitydata.streetview.baidu.__all__
:value: >
   ['BaiduStreetView']

```{autodoc2-docstring} pycitydata.streetview.baidu.__all__
```

````

`````{py:class} BaiduStreetView(sid: str, zoom: int = 4, headers: typing.Optional[typing.Dict[str, str]] = None, proxies: typing.Optional[typing.Dict[str, str]] = None)
:canonical: pycitydata.streetview.baidu.BaiduStreetView

```{autodoc2-docstring} pycitydata.streetview.baidu.BaiduStreetView
```

```{rubric} Initialization
```

```{autodoc2-docstring} pycitydata.streetview.baidu.BaiduStreetView.__init__
```

````{py:attribute} meta
:canonical: pycitydata.streetview.baidu.BaiduStreetView.meta
:value: >
   '_query_camera(...)'

```{autodoc2-docstring} pycitydata.streetview.baidu.BaiduStreetView.meta
```

````

````{py:attribute} panorama
:canonical: pycitydata.streetview.baidu.BaiduStreetView.panorama
:value: >
   '_query_img(...)'

```{autodoc2-docstring} pycitydata.streetview.baidu.BaiduStreetView.panorama
```

````

````{py:property} heading
:canonical: pycitydata.streetview.baidu.BaiduStreetView.heading
:type: float

```{autodoc2-docstring} pycitydata.streetview.baidu.BaiduStreetView.heading
```

````

````{py:method} search(x, y, headers: typing.Optional[typing.Dict[str, str]] = None, proxies: typing.Optional[typing.Dict[str, str]] = None, cache_dir: typing.Union[str, pathlib.Path, None] = None) -> pycitydata.streetview.baidu.BaiduStreetView
:canonical: pycitydata.streetview.baidu.BaiduStreetView.search
:staticmethod:

```{autodoc2-docstring} pycitydata.streetview.baidu.BaiduStreetView.search
```

````

````{py:method} _query_camera()
:canonical: pycitydata.streetview.baidu.BaiduStreetView._query_camera

```{autodoc2-docstring} pycitydata.streetview.baidu.BaiduStreetView._query_camera
```

````

````{py:method} _query_img()
:canonical: pycitydata.streetview.baidu.BaiduStreetView._query_img

```{autodoc2-docstring} pycitydata.streetview.baidu.BaiduStreetView._query_img
```

````

`````
