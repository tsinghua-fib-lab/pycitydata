# {py:mod}`pycitydata.urbankg.kg`

```{py:module} pycitydata.urbankg.kg
```

```{autodoc2-docstring} pycitydata.urbankg.kg
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`UrbanKG <pycitydata.urbankg.kg.UrbanKG>`
  - ```{autodoc2-docstring} pycitydata.urbankg.kg.UrbanKG
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__all__ <pycitydata.urbankg.kg.__all__>`
  - ```{autodoc2-docstring} pycitydata.urbankg.kg.__all__
    :summary:
    ```
````

### API

````{py:data} __all__
:canonical: pycitydata.urbankg.kg.__all__
:value: >
   ['UrbanKG']

```{autodoc2-docstring} pycitydata.urbankg.kg.__all__
```

````

`````{py:class} UrbanKG(mongo_uri: str, mongo_db: str, mongo_entity_coll: str, mongo_relation_coll: str, cache_size: int = 100)
:canonical: pycitydata.urbankg.kg.UrbanKG

```{autodoc2-docstring} pycitydata.urbankg.kg.UrbanKG
```

```{rubric} Initialization
```

```{autodoc2-docstring} pycitydata.urbankg.kg.UrbanKG.__init__
```

````{py:attribute} CLASSES
:canonical: pycitydata.urbankg.kg.UrbanKG.CLASSES
:value: >
   ['Region', 'POI', 'Cate3', 'Brand', 'Ba', 'Cate2', 'Cate1']

```{autodoc2-docstring} pycitydata.urbankg.kg.UrbanKG.CLASSES
```

````

````{py:attribute} RELATIONS
:canonical: pycitydata.urbankg.kg.UrbanKG.RELATIONS
:value: >
   ['SubCateOf_3to2', 'RelatedBrand', 'NearBy', 'LocateAt', 'LargeOD', 'Competitive_zhishi', 'CoCheckin...

```{autodoc2-docstring} pycitydata.urbankg.kg.UrbanKG.RELATIONS
```

````

````{py:method} get_entity(id: str) -> typing.Optional[dict]
:canonical: pycitydata.urbankg.kg.UrbanKG.get_entity

```{autodoc2-docstring} pycitydata.urbankg.kg.UrbanKG.get_entity
```

````

````{py:method} query_object(subject_id: str, relation: str) -> typing.List[str]
:canonical: pycitydata.urbankg.kg.UrbanKG.query_object

```{autodoc2-docstring} pycitydata.urbankg.kg.UrbanKG.query_object
```

````

````{py:method} query_subject(object_id: str, relation: str) -> typing.List[str]
:canonical: pycitydata.urbankg.kg.UrbanKG.query_subject

```{autodoc2-docstring} pycitydata.urbankg.kg.UrbanKG.query_subject
```

````

````{py:method} explore(subject_id: str, relations: typing.List[str]) -> typing.List[typing.Tuple[str, dict]]
:canonical: pycitydata.urbankg.kg.UrbanKG.explore

```{autodoc2-docstring} pycitydata.urbankg.kg.UrbanKG.explore
```

````

`````
