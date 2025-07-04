# {py:mod}`pycitydata.map.format_converter`

```{py:module} pycitydata.map.format_converter
```

```{autodoc2-docstring} pycitydata.map.format_converter
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`pb2json <pycitydata.map.format_converter.pb2json>`
  - ```{autodoc2-docstring} pycitydata.map.format_converter.pb2json
    :summary:
    ```
* - {py:obj}`pb2dict <pycitydata.map.format_converter.pb2dict>`
  - ```{autodoc2-docstring} pycitydata.map.format_converter.pb2dict
    :summary:
    ```
* - {py:obj}`pb2coll <pycitydata.map.format_converter.pb2coll>`
  - ```{autodoc2-docstring} pycitydata.map.format_converter.pb2coll
    :summary:
    ```
* - {py:obj}`json2pb <pycitydata.map.format_converter.json2pb>`
  - ```{autodoc2-docstring} pycitydata.map.format_converter.json2pb
    :summary:
    ```
* - {py:obj}`dict2pb <pycitydata.map.format_converter.dict2pb>`
  - ```{autodoc2-docstring} pycitydata.map.format_converter.dict2pb
    :summary:
    ```
* - {py:obj}`coll2pb <pycitydata.map.format_converter.coll2pb>`
  - ```{autodoc2-docstring} pycitydata.map.format_converter.coll2pb
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__all__ <pycitydata.map.format_converter.__all__>`
  - ```{autodoc2-docstring} pycitydata.map.format_converter.__all__
    :summary:
    ```
* - {py:obj}`T <pycitydata.map.format_converter.T>`
  - ```{autodoc2-docstring} pycitydata.map.format_converter.T
    :summary:
    ```
````

### API

````{py:data} __all__
:canonical: pycitydata.map.format_converter.__all__
:value: >
   ['pb2json', 'pb2dict', 'pb2coll', 'json2pb', 'dict2pb', 'coll2pb']

```{autodoc2-docstring} pycitydata.map.format_converter.__all__
```

````

````{py:function} pb2json(pb: google.protobuf.message.Message)
:canonical: pycitydata.map.format_converter.pb2json

```{autodoc2-docstring} pycitydata.map.format_converter.pb2json
```
````

````{py:function} pb2dict(pb: google.protobuf.message.Message)
:canonical: pycitydata.map.format_converter.pb2dict

```{autodoc2-docstring} pycitydata.map.format_converter.pb2dict
```
````

````{py:function} pb2coll(pb: google.protobuf.message.Message, coll: pymongo.collection.Collection, insert_chunk_size: int = 0, drop: bool = False)
:canonical: pycitydata.map.format_converter.pb2coll

```{autodoc2-docstring} pycitydata.map.format_converter.pb2coll
```
````

````{py:data} T
:canonical: pycitydata.map.format_converter.T
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} pycitydata.map.format_converter.T
```

````

````{py:function} json2pb(json: str, pb: pycitydata.map.format_converter.T) -> pycitydata.map.format_converter.T
:canonical: pycitydata.map.format_converter.json2pb

```{autodoc2-docstring} pycitydata.map.format_converter.json2pb
```
````

````{py:function} dict2pb(d: dict, pb: pycitydata.map.format_converter.T) -> pycitydata.map.format_converter.T
:canonical: pycitydata.map.format_converter.dict2pb

```{autodoc2-docstring} pycitydata.map.format_converter.dict2pb
```
````

````{py:function} coll2pb(coll: pymongo.collection.Collection, pb: pycitydata.map.format_converter.T) -> pycitydata.map.format_converter.T
:canonical: pycitydata.map.format_converter.coll2pb

```{autodoc2-docstring} pycitydata.map.format_converter.coll2pb
```
````
