{
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "rf7j5ch",
          "type": "point",
          "config": {
            "dataId": "negative",
            "label": "negative",
            "color": [
              119,
              110,
              87
            ],
            "columns": {
              "lat": "latitude",
              "lng": "longitude",
              "altitude": None
            },
            "isVisible": True,
            "visConfig": {
              "radius": 15,
              "fixedRadius": False,
              "opacity": 0.7,
              "outline": True,
              "thickness": 2,
              "strokeColor": [
                25,
                20,
                16
              ],
              "colorRange": {
                "name": "ColorBrewer Reds-9",
                "type": "singlehue",
                "category": "ColorBrewer",
                "colors": [
                  "#67000d",
                  "#a50f15",
                  "#cb181d",
                  "#ef3b2c",
                  "#fb6a4a",
                  "#fc9272",
                  "#fcbba1",
                  "#fee0d2",
                  "#fff5f0"
                ],
                "reversed": True
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
              "name": "check_outs",
              "type": "integer"
            },
            "colorScale": "quantile",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear"
          }
        },
        {
          "id": "yt1is8n",
          "type": "point",
          "config": {
            "dataId": "positive",
            "label": "positive",
            "color": [
              77,
              193,
              156
            ],
            "columns": {
              "lat": "latitude",
              "lng": "longitude",
              "altitude": None
            },
            "isVisible": True,
            "visConfig": {
              "radius": 15,
              "fixedRadius": False,
              "opacity": 0.7,
              "outline": True,
              "thickness": 2,
              "strokeColor": [
                25,
                20,
                16
              ],
              "colorRange": {
                "name": "ColorBrewer YlGn-9",
                "type": "sequential",
                "category": "ColorBrewer",
                "colors": [
                  "#ffffe5",
                  "#f7fcb9",
                  "#d9f0a3",
                  "#addd8e",
                  "#78c679",
                  "#41ab5d",
                  "#238443",
                  "#006837",
                  "#004529"
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
            "colorField": {
              "name": "check_ins",
              "type": "integer"
            },
            "colorScale": "quantile",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "positive": [
              {
                "name": "station_id",
                "format": None
              },
              {
                "name": "name",
                "format": None
              },
              {
                "name": "check_outs",
                "format": None
              },
              {
                "name": "check_ins",
                "format": None
              },
              {
                "name": "diff",
                "format": None
              }
            ],
            "negative": [
              {
                "name": "station_id",
                "format": None
              },
              {
                "name": "name",
                "format": None
              },
              {
                "name": "check_outs",
                "format": None
              },
              {
                "name": "check_ins",
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
      "latitude": 53.5307819179127,
      "longitude": 9.994552194624756,
      "pitch": 0,
      "zoom": 10.684632274109424,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "light",
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
