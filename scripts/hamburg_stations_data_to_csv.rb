require "json"
require "csv"

JSON_FILE = "./data/hamburg/stations.geojson"
CSV_FILE = "./data/hamburg/stations.csv"

HEADERS = [
  "name",
  "longitude",
  "latitude",
]

hash = JSON.parse(File.read(JSON_FILE))

CSV.open(CSV_FILE, "wb") do |csv|
  csv << HEADERS
  hash["features"].each do |station_hash|
    name = station_hash["properties"]["name"]
    coordinates = station_hash["geometry"]["coordinates"]
    csv << [
      name,
      coordinates[0].round(6),
      coordinates[1].round(6),
    ]
  end
end
