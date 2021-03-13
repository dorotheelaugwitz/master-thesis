require "json"
require "date"
require "time"
require "csv"

JSON_FILE = "/Users/doro/HAWCloud/Masterarbeit/data/dark_sky_api/weather.json"
CSV_FILE = "/Users/doro/HAWCloud/Masterarbeit/data/dark_sky_api/weather.csv"
HEADERS = [
  "datetime",
  "precip_intensity",
  "precip_probability",
  "precip_type",
  "precip_accumulation",
  "temperature",
  "apparent_temperature",
  "dew_point",
  "humidity",
  "wind_speed",
  "wind_gust",
  "wind_bearing",
  "uv_index",
  "visibility",
  "cloud_cover",
  "pressure",
]

hash = JSON.parse(File.read(JSON_FILE))

CSV.open(CSV_FILE, "wb") do |csv|
  csv << HEADERS
  hash.each_pair do |date, daily_data|
    date = DateTime.parse(date)

    daily_data["hourly"]["data"].each do |hourly_data|
      time_at = Time.at(hourly_data["time"])

      csv << [
        time_at.strftime("%Y-%m-%d %H:%M:%S"),
        hourly_data["precipIntensity"],
        hourly_data["precipProbability"],
        hourly_data["precipType"],
        hourly_data["precipAccumulation"],
        hourly_data["temperature"],
        hourly_data["apparentTemperature"],
        hourly_data["dewPoint"],
        hourly_data["humidity"],
        hourly_data["windSpeed"],
        hourly_data["windGust"],
        hourly_data["windBearing"],
        hourly_data["uvIndex"],
        hourly_data["visibility"],
        hourly_data["cloudCover"],
        hourly_data["pressure"],
      ]
    end
  end
end
