library(httr)
library(jsonlite)

# Reddit API endpoint
url <- "https://www.reddit.com/r/SideProject/.json"

# Set headers to mimic a browser request
headers <- add_headers(
    "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:143.0) Gecko/20100101 Firefox/143.0"
)

# Make the GET request
r <- GET(url, headers)

# Check if request was successful
if (status_code(r) == 200) {
    # Parse JSON response
    c <- fromJSON(rawToChar(r$content), flatten = TRUE)
    
    # Extract posts data
    df <- c$data$children$data
    
    # Display basic info about scraped data
    cat("Successfully scraped", nrow(df), "posts from r/SideProject\n")
    cat("Columns available:", paste(names(df), collapse = ", "), "\n")
    
    # Show first few posts
    print(head(df[, c("title", "author", "score", "num_comments")], 5))
    
    # Save to CSV
    write.csv(df, "reddit_data.csv", row.names = FALSE)
    cat("Data saved to reddit_data.csv\n")
    
} else {
    cat("Error: HTTP", status_code(r), "\n")
    cat("Response:", rawToChar(r$content), "\n")
}

