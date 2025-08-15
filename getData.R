library(httr)
library(jsonlite)

r <- GET("https://www.reddit.com/r/Scams/.json")

c <- fromJSON(rawToChar (r$content), flatten = TRUE)
c$data$after

df <- c$data$children