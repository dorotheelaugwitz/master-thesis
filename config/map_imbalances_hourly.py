{
  "version": "v1",
  "config": {
    "visState": {
      "filters": [
        {
          "dataId": [
            "hourly_imbalances"
          ],
          "id": "2qc60eig9",
          "name": [
            "date_from"
          ],
          "type": "range",
          "value": [
            0,
            3.19
          ],
          "enlarged": False,
          "plotType": "histogram",
          "animationWindow": "free",
          "yAxis": None
        }
      ],
      "layers": [
        {
          "id": "ehygvp",
          "type": "arc",
          "config": {
            "dataId": "hourly_imbalances",
            "label": "imbalances",
            "color": [
              246,
              239,
              138
            ],
            "columns": {
              "lat0": "latitude_x",
              "lng0": "longitude_x",
              "lat1": "latitude_y",
              "lng1": "longitude_y"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.7,
              "thickness": 1,
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
                1,
                10
              ],
              "targetColor": [
                134,
                10,
                90
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
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "hourly_imbalances": [
              {
                "name": "date_from",
                "format": None
              },
              {
                "name": "start_station_name",
                "format": None
              },
              {
                "name": "end_station_name",
                "format": None
              },
              {
                "name": "checkin_count",
                "format": None
              },
              {
                "name": "checkout_count",
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
      "latitude": 53.561078796386305,
      "longitude": 9.988441894733983,
      "pitch": 0,
      "zoom": 11.114535195284688,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "dark",
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
        218.82023004728686,
        223.47597962276103,
        223.47597962276103
      ],
      "mapStyles": {}
    }
  }
}
