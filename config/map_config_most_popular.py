{
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "mz5vtjc",
          "type": "point",
          "config": {
            "dataId": "stations",
            "label": "Stations",
            "color": [
              25,
              20,
              16
            ],
            "columns": {
              "lat": "latitude",
              "lng": "longitude",
              "altitude": None
            },
            "isVisible": True,
            "visConfig": {
              "radius": 7,
              "fixedRadius": False,
              "opacity": 0.8,
              "outline": False,
              "thickness": 2,
              "strokeColor": None,
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radiusRange": [
                0,
                50
              ],
              "filled": True
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear"
          }
        },
        {
          "id": "o9o5xrq",
          "type": "arc",
          "config": {
            "dataId": "data",
            "label": "Routes",
            "color": [
              59,
              133,
              204
            ],
            "columns": {
              "lat0": "latitude_x",
              "lng0": "longitude_x",
              "lat1": "latitude_y",
              "lng1": "longitude_y"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "thickness": 2,
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "sizeRange": [
                0,
                10
              ],
              "targetColor": None
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "sizeField": {
              "name": "count",
              "type": "integer"
            },
            "sizeScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "data": [
              {
                "name": "station_x",
                "format": None
              },
              {
                "name": "station_y",
                "format": None
              },
              {
                "name": "count",
                "format": None
              }
            ],
            "stations": [
              {
                "name": "station_id",
                "format": None
              },
              {
                "name": "name",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": 0,
      "dragRotate": False,
      "latitude": 53.53367132327897,
      "longitude": 9.95383467310889,
      "pitch": 0,
      "zoom": 10.706122812119,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "muted",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": False,
        "road": True,
        "border": True,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        224.4071295378559,
        224.4071295378559,
        224.4071295378559
      ],
      "mapStyles": {}
    }
  }
}
