{
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "xuhfn9",
          "type": "line",
          "config": {
            "dataId": "data",
            "label": "new layer",
            "color": [
              255,
              248,
              51
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
              "targetColor": [
                227,
                26,
                26
              ]
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
              "name": "diff",
              "type": "integer"
            },
            "sizeScale": "linear"
          }
        },
        {
          "id": "pxy0hq9",
          "type": "point",
          "config": {
            "dataId": "data",
            "label": "new layer",
            "color": [
              30,
              150,
              190
            ],
            "columns": {
              "lat": "latitude_x",
              "lng": "longitude_x",
              "altitude": None
            },
            "isVisible": False,
            "visConfig": {
              "radius": 10,
              "fixedRadius": False,
              "opacity": 1,
              "outline": False,
              "thickness": 2,
              "strokeColor": None,
              "colorRange": {
                "name": "Uber Viz Sequential 4",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#E6FAFA",
                  "#C1E5E6",
                  "#9DD0D4",
                  "#75BBC1",
                  "#4BA7AF",
                  "#00939C"
                ],
                "reversed": False
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
            "colorField": {
              "name": "diff",
              "type": "integer"
            },
            "colorScale": "quantile",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "sizeField": {
              "name": "diff",
              "type": "integer"
            },
            "sizeScale": "sqrt"
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
                "name": "checkout_count",
                "format": None
              },
              {
                "name": "checkin_count",
                "format": None
              },
              {
                "name": "diff",
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
      "latitude": 53.55972266426729,
      "longitude": 9.994493023861432,
      "pitch": 0,
      "zoom": 11.56938284358558,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "dark",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        9.665468314072013,
        17.18305478057247,
        31.1442867897876
      ],
      "mapStyles": {}
    }
  }
}
