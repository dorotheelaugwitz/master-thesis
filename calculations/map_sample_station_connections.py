{
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "57kzr3",
          "type": "line",
          "config": {
            "dataId": "sample_a_diff_pos",
            "label": "positive",
            "color": [
              136,
              87,
              44
            ],
            "columns": {
              "lat0": "latitude_x",
              "lng0": "longitude_x",
              "lat1": "latitude_y",
              "lng1": "longitude_y"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 1,
              "thickness": 3,
              "colorRange": {
                "name": "ColorBrewer YlGn-6",
                "type": "sequential",
                "category": "ColorBrewer",
                "colors": [
                  "#ffffcc",
                  "#d9f0a3",
                  "#addd8e",
                  "#78c679",
                  "#31a354",
                  "#006837"
                ]
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
              "name": "diff",
              "type": "integer"
            },
            "colorScale": "quantile",
            "sizeField": {
              "name": "diff",
              "type": "integer"
            },
            "sizeScale": "sqrt"
          }
        },
        {
          "id": "6ltvnf",
          "type": "line",
          "config": {
            "dataId": "sample_a_diff_neg",
            "label": "negative",
            "color": [
              130,
              154,
              227
            ],
            "columns": {
              "lat0": "latitude_x",
              "lng0": "longitude_x",
              "lat1": "latitude_y",
              "lng1": "longitude_y"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 1,
              "thickness": 3,
              "colorRange": {
                "name": "ColorBrewer OrRd-6",
                "type": "sequential",
                "category": "ColorBrewer",
                "colors": [
                  "#b30000",
                  "#e34a33",
                  "#fc8d59",
                  "#fdbb84",
                  "#fdd49e",
                  "#fef0d9"
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
              "name": "diff",
              "type": "integer"
            },
            "colorScale": "quantile",
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
            "sample_a_diff_pos": [
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
            ],
            "sample_a_diff_neg": [
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
            ],
            "sample_b_diff_pos": [
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
            ],
            "sample_b_diff_neg": [
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
            ],
            "sample_c_diff_pos": [
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
            ],
            "sample_c_diff_neg": [
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
      "latitude": 53.54384889787453,
      "longitude": 9.990413907251181,
      "pitch": 0,
      "zoom": 14.18533410244427,
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
