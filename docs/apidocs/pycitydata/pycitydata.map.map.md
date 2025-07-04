# {py:mod}`pycitydata.map.map`

```{py:module} pycitydata.map.map
```

```{autodoc2-docstring} pycitydata.map.map
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Map <pycitydata.map.map.Map>`
  - ```{autodoc2-docstring} pycitydata.map.map.Map
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`__all__ <pycitydata.map.map.__all__>`
  - ```{autodoc2-docstring} pycitydata.map.map.__all__
    :summary:
    ```
````

### API

````{py:data} __all__
:canonical: pycitydata.map.map.__all__
:value: >
   ['Map']

```{autodoc2-docstring} pycitydata.map.map.__all__
```

````

`````{py:class} Map(mongo_uri: typing.Optional[str] = None, mongo_db: typing.Optional[str] = None, mongo_coll: typing.Optional[str] = None, cache_dir: typing.Optional[str] = None, cache_path: typing.Optional[str] = None, pb_path: typing.Optional[str] = None)
:canonical: pycitydata.map.map.Map

```{autodoc2-docstring} pycitydata.map.map.Map
```

```{rubric} Initialization
```

```{autodoc2-docstring} pycitydata.map.map.Map.__init__
```

````{py:attribute} header
:canonical: pycitydata.map.map.Map.header
:type: dict
:value: >
   None

```{autodoc2-docstring} pycitydata.map.map.Map.header
```

````

````{py:attribute} juncs
:canonical: pycitydata.map.map.Map.juncs
:type: typing.Dict[int, dict]
:value: >
   None

```{autodoc2-docstring} pycitydata.map.map.Map.juncs
```

````

````{py:attribute} lanes
:canonical: pycitydata.map.map.Map.lanes
:type: typing.Dict[int, dict]
:value: >
   None

```{autodoc2-docstring} pycitydata.map.map.Map.lanes
```

````

````{py:attribute} roads
:canonical: pycitydata.map.map.Map.roads
:type: typing.Dict[int, dict]
:value: >
   None

```{autodoc2-docstring} pycitydata.map.map.Map.roads
```

````

````{py:attribute} aois
:canonical: pycitydata.map.map.Map.aois
:type: typing.Dict[int, dict]
:value: >
   None

```{autodoc2-docstring} pycitydata.map.map.Map.aois
```

````

````{py:attribute} pois
:canonical: pycitydata.map.map.Map.pois
:type: typing.Dict[int, dict]
:value: >
   None

```{autodoc2-docstring} pycitydata.map.map.Map.pois
```

````

````{py:attribute} projector
:canonical: pycitydata.map.map.Map.projector
:type: pyproj.Proj
:value: >
   None

```{autodoc2-docstring} pycitydata.map.map.Map.projector
```

````

````{py:method} _parse_map(m: typing.List[typing.Any]) -> typing.Dict[str, typing.Any]
:canonical: pycitydata.map.map.Map._parse_map

```{autodoc2-docstring} pycitydata.map.map.Map._parse_map
```

````

````{py:method} _download_map_with_cache(uri: str, db: str, coll: str, cache_dir: typing.Optional[str]) -> typing.Dict[str, typing.Any]
:canonical: pycitydata.map.map.Map._download_map_with_cache

```{autodoc2-docstring} pycitydata.map.map.Map._download_map_with_cache
```

````

````{py:method} _build_geo_index()
:canonical: pycitydata.map.map.Map._build_geo_index

```{autodoc2-docstring} pycitydata.map.map.Map._build_geo_index
```

````

````{py:method} _get_lane_s(position: pycityproto.city.geo.v2.geo_pb2.Position, lane_id: int) -> float
:canonical: pycitydata.map.map.Map._get_lane_s

```{autodoc2-docstring} pycitydata.map.map.Map._get_lane_s
```

````

````{py:method} _get_driving_geo(road_id: int)
:canonical: pycitydata.map.map.Map._get_driving_geo

```{autodoc2-docstring} pycitydata.map.map.Map._get_driving_geo
```

````

````{py:method} _get_walking_geo(segment: pycityproto.city.routing.v2.routing_pb2.WalkingRouteSegment)
:canonical: pycitydata.map.map.Map._get_walking_geo

```{autodoc2-docstring} pycitydata.map.map.Map._get_walking_geo
```

````

````{py:method} lnglat2xy(lng: float, lat: float) -> typing.Tuple[float, float]
:canonical: pycitydata.map.map.Map.lnglat2xy

```{autodoc2-docstring} pycitydata.map.map.Map.lnglat2xy
```

````

````{py:method} xy2lnglat(x: float, y: float) -> typing.Tuple[float, float]
:canonical: pycitydata.map.map.Map.xy2lnglat

```{autodoc2-docstring} pycitydata.map.map.Map.xy2lnglat
```

````

````{py:method} position2xy(position: typing.Union[pycityproto.city.geo.v2.geo_pb2.Position, typing.Dict[str, typing.Any]]) -> typing.Tuple[float, float]
:canonical: pycitydata.map.map.Map.position2xy

```{autodoc2-docstring} pycitydata.map.map.Map.position2xy
```

````

````{py:method} get_header()
:canonical: pycitydata.map.map.Map.get_header

```{autodoc2-docstring} pycitydata.map.map.Map.get_header
```

````

````{py:method} get_aoi(id: int, include_unused: bool = False) -> typing.Optional[typing.Any]
:canonical: pycitydata.map.map.Map.get_aoi

```{autodoc2-docstring} pycitydata.map.map.Map.get_aoi
```

````

````{py:method} get_poi(id: int, include_unused: bool = False) -> typing.Optional[typing.Any]
:canonical: pycitydata.map.map.Map.get_poi

```{autodoc2-docstring} pycitydata.map.map.Map.get_poi
```

````

````{py:method} get_lane(id: int, include_unused: bool = False) -> typing.Optional[typing.Any]
:canonical: pycitydata.map.map.Map.get_lane

```{autodoc2-docstring} pycitydata.map.map.Map.get_lane
```

````

````{py:method} get_road(id: int, include_unused: bool = False) -> typing.Optional[typing.Any]
:canonical: pycitydata.map.map.Map.get_road

```{autodoc2-docstring} pycitydata.map.map.Map.get_road
```

````

````{py:method} get_junction(id: int, include_unused: bool = False) -> typing.Optional[typing.Any]
:canonical: pycitydata.map.map.Map.get_junction

```{autodoc2-docstring} pycitydata.map.map.Map.get_junction
```

````

````{py:method} export_aoi_center_as_geojson(id: int, properties: typing.Union[typing.Dict[str, typing.Any], typing.Literal[auto]] = 'auto') -> dict
:canonical: pycitydata.map.map.Map.export_aoi_center_as_geojson

```{autodoc2-docstring} pycitydata.map.map.Map.export_aoi_center_as_geojson
```

````

````{py:method} export_aoi_as_geojson(id: int, properties: typing.Union[typing.Dict[str, typing.Any], typing.Literal[auto]] = 'auto') -> dict
:canonical: pycitydata.map.map.Map.export_aoi_as_geojson

```{autodoc2-docstring} pycitydata.map.map.Map.export_aoi_as_geojson
```

````

````{py:method} export_poi_as_geojson(id: int, properties: typing.Union[typing.Dict[str, typing.Any], typing.Literal[auto]] = 'auto') -> dict
:canonical: pycitydata.map.map.Map.export_poi_as_geojson

```{autodoc2-docstring} pycitydata.map.map.Map.export_poi_as_geojson
```

````

````{py:method} export_lane_as_geojson(id: int, properties: typing.Union[typing.Dict[str, typing.Any], typing.Literal[auto]] = 'auto') -> dict
:canonical: pycitydata.map.map.Map.export_lane_as_geojson

```{autodoc2-docstring} pycitydata.map.map.Map.export_lane_as_geojson
```

````

````{py:method} export_road_as_geojson(id: int, properties: typing.Dict[str, typing.Any] = {}) -> dict
:canonical: pycitydata.map.map.Map.export_road_as_geojson

```{autodoc2-docstring} pycitydata.map.map.Map.export_road_as_geojson
```

````

````{py:method} _route_to_xys(route_req: pycityproto.city.routing.v2.routing_service_pb2.GetRouteRequest, route_res: pycityproto.city.routing.v2.routing_service_pb2.GetRouteResponse) -> numpy.ndarray
:canonical: pycitydata.map.map.Map._route_to_xys

```{autodoc2-docstring} pycitydata.map.map.Map._route_to_xys
```

````

````{py:method} export_route_as_geojson(route_req: typing.Union[pycityproto.city.routing.v2.routing_service_pb2.GetRouteRequest, dict], route_res: typing.Union[pycityproto.city.routing.v2.routing_service_pb2.GetRouteResponse, dict], properties: dict = {}) -> dict
:canonical: pycitydata.map.map.Map.export_route_as_geojson

```{autodoc2-docstring} pycitydata.map.map.Map.export_route_as_geojson
```

````

````{py:method} estimate_route_time(route_req: typing.Union[pycityproto.city.routing.v2.routing_service_pb2.GetRouteRequest, dict], route_res: typing.Union[pycityproto.city.routing.v2.routing_service_pb2.GetRouteResponse, dict]) -> float
:canonical: pycitydata.map.map.Map.estimate_route_time

```{autodoc2-docstring} pycitydata.map.map.Map.estimate_route_time
```

````

````{py:method} query_pois(center: typing.Union[typing.Tuple[float, float], shapely.geometry.Point], radius: typing.Optional[float] = None, category_prefix: typing.Optional[str] = None, limit: typing.Optional[int] = None, return_distance: bool = True) -> typing.Union[typing.List[typing.Tuple[typing.Any, float]], typing.List[typing.Any]]
:canonical: pycitydata.map.map.Map.query_pois

```{autodoc2-docstring} pycitydata.map.map.Map.query_pois
```

````

````{py:method} query_aois(center: typing.Union[typing.Tuple[float, float], shapely.geometry.Point], radius: float, urban_land_uses: typing.Optional[typing.List[str]] = None, limit: typing.Optional[int] = None) -> typing.List[typing.Tuple[typing.Any, float]]
:canonical: pycitydata.map.map.Map.query_aois

```{autodoc2-docstring} pycitydata.map.map.Map.query_aois
```

````

````{py:method} query_lane(xy: typing.Union[typing.Tuple[float, float], shapely.geometry.Point], radius: float, lane_type: int = 1)
:canonical: pycitydata.map.map.Map.query_lane

```{autodoc2-docstring} pycitydata.map.map.Map.query_lane
```

````

`````
