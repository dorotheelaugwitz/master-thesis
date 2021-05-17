{
  "version": "v1",
  "config": {
    "visState": {
      "filters": [
        {
          "dataId": [
            "data"
          ],
          "id": "k3htm9tg2",
          "name": [
            "datetime"
          ],
          "type": "range",
          "value": [
            5.24,
            12.07
          ],
          "enlarged": False,
          "plotType": "histogram",
          "animationWindow": "free",
          "yAxis": None
        }
      ],
      "layers": [
        {
          "id": "5hdg1jh",
          "type": "heatmap",
          "config": {
            "dataId": "data",
            "label": "Check-Ins",
            "color": [
              18,
              147,
              154
            ],
            "columns": {
              "lat": "latitude",
              "lng": "longitude"
            },
            "isVisible": False,
            "visConfig": {
              "opacity": 1,
              "colorRange": {
                "name": "Purple Blue Yellow 6",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#2B1E3E",
                  "#343D5E",
                  "#4F777E",
                  "#709E87",
                  "#99BE95",
                  "#D6DEBF"
                ]
              },
              "radius": 30
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
              "name": "check_ins",
              "type": "integer"
            },
            "weightScale": "linear"
          }
        },
        {
          "id": "sy67j6u",
          "type": "heatmap",
          "config": {
            "dataId": "data",
            "label": "Check-Outs",
            "color": [
              34,
              63,
              154
            ],
            "columns": {
              "lat": "latitude",
              "lng": "longitude"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 1,
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
              "radius": 30
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
              "name": "check_outs",
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
                "name": "datetime",
                "format": None
              },
              {
                "name": "station_name",
                "format": None
              },
              {
                "name": "check_ins",
                "format": None
              },
              {
                "name": "check_outs",
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
      "latitude": 53.555822807040556,
      "longitude": 9.976688183112852,
      "pitch": 0,
      "zoom": 10.911094653332931,
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
