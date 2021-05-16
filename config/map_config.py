{
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "8gtn60h",
          "type": "line",
          "config": {
            "dataId": "data",
            "label": "end -> start arc",
            "color": [
              24,
              38,
              77
            ],
            "columns": {
              "lat0": "end_latitude",
              "lng0": "end_longitude",
              "lat1": "start_latitude",
              "lng1": "start_longitude"
            },
            "isVisible": False,
            "visConfig": {
              "opacity": 0.1,
              "thickness": 2,
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#FFC300",
                  "#F1920E",
                  "#E3611C",
                  "#C70039",
                  "#900C3F",
                  "#5A1846"
                ],
                "reversed": True
              },
              "sizeRange": [
                0,
                5
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
            "colorField": {
              "name": "count",
              "type": "integer"
            },
            "colorScale": "quantile",
            "sizeField": {
              "name": "count",
              "type": "integer"
            },
            "sizeScale": "sqrt"
          }
        },
        {
          "id": "84fysc6",
          "type": "line",
          "config": {
            "dataId": "data",
            "label": "start -> end arc",
            "color": [
              24,
              38,
              77
            ],
            "columns": {
              "lat0": "start_latitude",
              "lng0": "start_longitude",
              "lat1": "end_latitude",
              "lng1": "end_longitude"
            },
            "isVisible": False,
            "visConfig": {
              "opacity": 0.1,
              "thickness": 2,
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#FFC300",
                  "#F1920E",
                  "#E3611C",
                  "#C70039",
                  "#900C3F",
                  "#5A1846"
                ],
                "reversed": True
              },
              "sizeRange": [
                0,
                5
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
            "colorField": {
              "name": "count",
              "type": "integer"
            },
            "colorScale": "quantile",
            "sizeField": {
              "name": "count",
              "type": "integer"
            },
            "sizeScale": "sqrt"
          }
        },
        {
          "id": "or8khy8",
          "type": "heatmap",
          "config": {
            "dataId": "data",
            "label": "end heat",
            "color": [
              130,
              154,
              227
            ],
            "columns": {
              "lat": "end_latitude",
              "lng": "end_longitude"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
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
              "radius": 10
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
            "weightField": {
              "name": "count",
              "type": "integer"
            },
            "weightScale": "linear"
          }
        },
        {
          "id": "p2k711u",
          "type": "heatmap",
          "config": {
            "dataId": "data",
            "label": "start heat",
            "color": [
              119,
              110,
              87
            ],
            "columns": {
              "lat": "start_latitude",
              "lng": "start_longitude"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
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
              "radius": 10
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
            "weightField": {
              "name": "count",
              "type": "integer"
            },
            "weightScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "data": [
              {
                "name": "start_station_id",
                "format": None
              },
              {
                "name": "end_station_id",
                "format": None
              },
              {
                "name": "count",
                "format": None
              },
              {
                "name": "start_station_name",
                "format": None
              },
              {
                "name": "end_station_name",
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
      "latitude": 53.55361226963469,
      "longitude": 9.952289196980285,
      "pitch": 0,
      "zoom": 10.355464221229035,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "muted",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": False,
        "road": True,
        "border": True,
        "building": False,
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
