#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

library('textshaping')
library('ragg')
library('tidyverse')
library('tm')
library('SnowballC')
library('wordcloud')
library('RColorBrewer')
library('ggplot2')
library('magrittr')
library('quanteda')
library('rainette')
library('syuzhet')

text <- readLines(args[1])
TextDoc <- Corpus(VectorSource(text))

toSpace <- content_transformer(function (x , pattern ) gsub(pattern, " ", x))
TextDoc <- tm_map(TextDoc, toSpace, "/")
TextDoc <- tm_map(TextDoc, toSpace, "@")
TextDoc <- tm_map(TextDoc, toSpace, "\\|")
TextDoc <- tm_map(TextDoc, content_transformer(tolower))
TextDoc <- tm_map(TextDoc, removeNumbers)
TextDoc <- tm_map(TextDoc, removeWords, stopwords(args[2]))
TextDoc <- tm_map(TextDoc, removePunctuation)
TextDoc <- tm_map(TextDoc, stripWhitespace)
TextDoc <- tm_map(TextDoc, stemDocument)

TextDoc_dtm <- TermDocumentMatrix(TextDoc)
dtm_m <- as.matrix(TextDoc_dtm)
dtm_v <- sort(rowSums(dtm_m),decreasing=TRUE)
dtm_d <- data.frame(word = names(dtm_v),freq=dtm_v)

d <- get_nrc_sentiment(text)
td <- data.frame(t(d))
td_new <- data.frame(rowSums(td[2:ncol(td)]))
names(td_new)[1] <- "count"
td_new <- cbind("sentiment" = rownames(td_new), td_new)
rownames(td_new) <- NULL
td_new2 <- td_new[1:8,]

sentiments_1 <- function(name) {
    plotname_sents_1 <- paste(gsub('.{0,4}$', '', name), "_sents_1.jpeg", sep = "")
    path_file_name <- paste('media/image/plots/sents_1/', plotname_sents_1, sep = "")
    plot <- qplot(sentiment, data = td_new2, weight = count, geom = "bar", fill = sentiment, ylab = "count") + ggtitle("Survey sentiments")
    ggsave(filename=path_file_name, plot = plot)
}
sentiments_1(args[1])