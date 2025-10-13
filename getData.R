library(httr)
library(jsonlite)
url <- "https://www.reddit.com/r/SideProject/.json"

headers <- add_headers(
    "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:143.0) Gecko/20100101 Firefox/143.0"

)

r <- GET(url, headers)
c <- fromJSON(rawToChar (r$content), flatten = TRUE)

df <- c$data$children

